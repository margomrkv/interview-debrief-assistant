"""Sanity check that Phoenix + DSPyInstrumentor start without errors.

Run: `python -m src.common.phoenix_smoke`
Expected: prints "phoenix UI: http://localhost:6006" and "OK" (or an install
hint if the optional `[tracing]` extras are missing).

Does NOT make real LM calls — only verifies the tracing stack imports and
the Phoenix in-process app starts.
"""
from __future__ import annotations

import sys

from src.common.tracer_setup import setup_phoenix, shutdown_phoenix


def main() -> int:
    tp = setup_phoenix(project_name="phoenix-smoke")
    if tp is None:
        print("smoke: tracing extras not installed — that's OK, trainer degrades gracefully")
        return 0
    print("phoenix UI: http://localhost:6006")
    print("OK — tracer_provider registered, DSPyInstrumentor instrumented")
    shutdown_phoenix(tp)
    return 0


if __name__ == "__main__":
    sys.exit(main())
