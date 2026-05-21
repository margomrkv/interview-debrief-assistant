"""Demo UI server — single-page UI + JSON/SSE API over a pluggable backend.

Run:  python3 src/ui/app.py              # emulator (stdlib only, zero install)
      python3 src/ui/app.py --mode live  # real per-item LLM scoring
      UI_BACKEND=live python3 src/ui/app.py 8011

The Splitter → Scoring pipeline is streamed over Server-Sent Events so each Q&A
and each score appears as soon as it is "ready" (async requirement in md/ui.md).
The backend is chosen at startup via ``make_backend`` (see ``src.ui.backend``):
``emulator`` replays ``data/emulator-data`` files; ``live`` sources Q&A from the
emulator and scores each via ``src.assessor``. The SSE contract is identical, so
the frontend is backend-agnostic.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from src.ui.backend import make_backend  # noqa: E402

HERE = Path(__file__).resolve().parent
STATIC = HERE / "static"

# Per-item delays (seconds) to make the streaming visible in a demo.
SPLIT_DELAY = 0.18
SCORE_DELAY = 0.32


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    @property
    def backend(self):
        return self.server.backend  # injected in main()

    # ---- helpers -----------------------------------------------------------
    def _send_json(self, obj, status=200):
        body = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_file(self, path: Path, content_type: str):
        data = path.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _sse_event(self, event: str, data: dict):
        chunk = f"event: {event}\ndata: {json.dumps(data, ensure_ascii=False)}\n\n"
        self.wfile.write(chunk.encode("utf-8"))
        self.wfile.flush()

    def log_message(self, *args):  # quieter console
        pass

    # ---- routing -----------------------------------------------------------
    def do_GET(self):
        parsed = urlparse(self.path)
        route = parsed.path

        if route == "/" or route == "/index.html":
            return self._send_file(STATIC / "index.html", "text/html; charset=utf-8")
        if route == "/static/app.js":
            return self._send_file(STATIC / "app.js", "application/javascript; charset=utf-8")
        if route == "/static/styles.css":
            return self._send_file(STATIC / "styles.css", "text/css; charset=utf-8")

        if route == "/api/interviews":
            return self._send_json(self.backend.list_interviews())

        if route == "/api/transcript":
            sid = parse_qs(parsed.query).get("source_id", [""])[0]
            return self._send_json({"source_id": sid, "text": self.backend.transcript_text(sid)})

        if route == "/api/stream":
            sid = parse_qs(parsed.query).get("source_id", [""])[0]
            return self._stream_pipeline(sid)

        self.send_error(404, "Not found")

    def do_POST(self):
        parsed = urlparse(self.path)
        if parsed.path == "/api/match":
            length = int(self.headers.get("Content-Length", 0))
            raw = self.rfile.read(length).decode("utf-8", errors="replace")
            try:
                text = json.loads(raw).get("text", "")
            except json.JSONDecodeError:
                text = raw
            sid = self.backend.match_source(text)
            return self._send_json({"source_id": sid})
        self.send_error(404, "Not found")

    # ---- the two-stage pipeline as an SSE stream ---------------------------
    def _stream_pipeline(self, source_id: str):
        backend = self.backend
        items = backend.split_items(source_id)
        if not items:
            return self.send_error(404, "Unknown source_id")

        delay = backend.demo_delays  # artificial pauses for the emulator only

        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream; charset=utf-8")
        self.send_header("Cache-Control", "no-cache")
        self.send_header("Connection", "close")
        self.end_headers()

        try:
            # Stage 1 — Splitter
            self._sse_event("stage", {"stage": "splitter", "status": "running",
                                      "total": len(items)})
            for it in items:
                if delay:
                    time.sleep(SPLIT_DELAY)
                self._sse_event("split_item", it)
            self._sse_event("stage", {"stage": "splitter", "status": "done"})

            # Stage 2 — Scoring (one LLM call per item in live mode)
            self._sse_event("stage", {"stage": "scoring", "status": "running",
                                      "total": len(items)})
            for it in items:
                if delay:
                    time.sleep(SCORE_DELAY)
                self._sse_event("score_item", backend.score_item(source_id, it["idx"]))
            self._sse_event("stage", {"stage": "scoring", "status": "done"})

            # Rollup
            self._sse_event("report", backend.report(source_id))
            self._sse_event("done", {})
        except (BrokenPipeError, ConnectionResetError):
            pass  # client navigated away mid-stream


def main():
    parser = argparse.ArgumentParser(description="Demo UI server (emulator or live LLM backend).")
    parser.add_argument("port", nargs="?", type=int, default=8000, help="listen port (default 8000)")
    parser.add_argument(
        "--mode",
        choices=["emulator", "live"],
        default=os.getenv("UI_BACKEND", "emulator"),
        help="backend: replay files (emulator) or call the real LLM (live). "
             "Default from $UI_BACKEND, else 'emulator'.",
    )
    args = parser.parse_args()

    server = ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    server.backend = make_backend(args.mode)
    print(f"Demo UI [{args.mode}] → http://127.0.0.1:{args.port}  (Ctrl-C to stop)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nbye")


if __name__ == "__main__":
    main()
