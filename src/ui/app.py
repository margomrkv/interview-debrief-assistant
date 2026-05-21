"""Demo UI server — stdlib only, zero install.

Run:  python3 src/ui/app.py    # then open http://127.0.0.1:8000

Serves a single-page UI and a small JSON/SSE API backed by ``src.ui.emulator``.
The Splitter → Scoring pipeline is *replayed* (no LLM calls) and streamed over
Server-Sent Events so each Q&A and each score appears as soon as it is "ready",
satisfying the async requirement in md/ui.md.
"""
from __future__ import annotations

import json
import sys
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from src.ui import emulator  # noqa: E402

HERE = Path(__file__).resolve().parent
STATIC = HERE / "static"

# Per-item delays (seconds) to make the streaming visible in a demo.
SPLIT_DELAY = 0.18
SCORE_DELAY = 0.32


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

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
            return self._send_json(emulator.list_interviews())

        if route == "/api/transcript":
            sid = parse_qs(parsed.query).get("source_id", [""])[0]
            return self._send_json({"source_id": sid, "text": emulator.transcript_text(sid)})

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
            sid = emulator.match_source(text)
            return self._send_json({"source_id": sid})
        self.send_error(404, "Not found")

    # ---- the two-stage pipeline as an SSE stream ---------------------------
    def _stream_pipeline(self, source_id: str):
        items = emulator.split_items(source_id)
        if not items:
            return self.send_error(404, "Unknown source_id")

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
                time.sleep(SPLIT_DELAY)
                self._sse_event("split_item", it)
            self._sse_event("stage", {"stage": "splitter", "status": "done"})

            # Stage 2 — Scoring
            self._sse_event("stage", {"stage": "scoring", "status": "running",
                                      "total": len(items)})
            for it in items:
                time.sleep(SCORE_DELAY)
                self._sse_event("score_item", emulator.score_item(source_id, it["idx"]))
            self._sse_event("stage", {"stage": "scoring", "status": "done"})

            # Rollup
            self._sse_event("report", emulator.report(source_id))
            self._sse_event("done", {})
        except (BrokenPipeError, ConnectionResetError):
            pass  # client navigated away mid-stream


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    print(f"Demo UI → http://127.0.0.1:{port}  (Ctrl-C to stop)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nbye")


if __name__ == "__main__":
    main()
