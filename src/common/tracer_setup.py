"""Phoenix (Arize) tracing setup for DSPy trainer.

Soft-degrades when optional `[tracing]` deps are not installed: returns None
and logs an install hint. The trainer keeps running (CostCallback +
PromptTracer continue to write JSONL).
"""
from __future__ import annotations

import logging
from typing import Any

_log = logging.getLogger("tracer_setup")


def setup_phoenix(project_name: str) -> Any | None:
    try:
        import phoenix as px
        from phoenix.otel import register
        from openinference.instrumentation.dspy import DSPyInstrumentor
    except ImportError:
        _log.info(
            "phoenix tracing disabled (install with: pip install -e '.[tracing]')"
        )
        return None

    px.launch_app()
    tp = register(project_name=project_name)
    DSPyInstrumentor().instrument(tracer_provider=tp)
    return tp


def shutdown_phoenix(tp: Any | None) -> None:
    if tp is None:
        return
    try:
        tp.shutdown()
    except Exception:
        pass
