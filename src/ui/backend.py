"""Pluggable backend for the demo UI (Strategy pattern).

The HTTP handler in ``app.py`` talks to a single ``Backend`` interface; the
concrete implementation is chosen once at startup via ``make_backend(mode)``:

* ``EmulatorBackend`` — replays pre-computed ``data/emulator-data`` files
  (stdlib only, no LLM, zero install — the default);
* ``LiveBackend`` — real per-item scoring through ``src.assessor`` (imports
  dspy/litellm; only loaded when ``mode == "live"``).

Both expose the same six methods plus a ``demo_delays`` flag the stream loop uses
to decide whether to insert the artificial per-item pauses (emulator only).
"""
from __future__ import annotations

from typing import Any, Protocol, runtime_checkable

from src.ui import emulator


@runtime_checkable
class Backend(Protocol):
    demo_delays: bool

    def list_interviews(self) -> list[dict[str, Any]]: ...
    def transcript_text(self, source_id: str) -> str: ...
    def match_source(self, uploaded_text: str) -> str | None: ...
    def split_items(self, source_id: str) -> list[dict[str, Any]]: ...
    def score_item(self, source_id: str, idx: int) -> dict[str, Any]: ...
    def report(self, source_id: str) -> dict[str, Any]: ...


class EmulatorBackend:
    """Thin object wrapper over the ``src.ui.emulator`` module functions."""

    demo_delays = True

    def list_interviews(self) -> list[dict[str, Any]]:
        return emulator.list_interviews()

    def transcript_text(self, source_id: str) -> str:
        return emulator.transcript_text(source_id)

    def match_source(self, uploaded_text: str) -> str | None:
        return emulator.match_source(uploaded_text)

    def split_items(self, source_id: str) -> list[dict[str, Any]]:
        return emulator.split_items(source_id)

    def score_item(self, source_id: str, idx: int) -> dict[str, Any]:
        return emulator.score_item(source_id, idx)

    def report(self, source_id: str) -> dict[str, Any]:
        return emulator.report(source_id)


def make_backend(mode: str) -> Backend:
    """``"emulator"`` → EmulatorBackend, ``"live"`` → LiveBackend; else ValueError.

    LiveBackend is imported lazily so the emulator path never pulls in dspy.
    """
    if mode == "emulator":
        return EmulatorBackend()
    if mode == "live":
        from src.ui.live_backend import LiveBackend  # lazy: avoids dspy on emulator

        return LiveBackend()
    raise ValueError(f"unknown backend mode {mode!r} (expected 'emulator' or 'live')")
