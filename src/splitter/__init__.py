"""Transcript → Q&A splitter (Stage 1 of the live pipeline).

One LLM call turns a raw interview transcript into the splitter-schema items the
UI's ``QA`` objects are built from. The prompt and schema are reused verbatim
from the ``/splitter`` Claude Code skill (single source of truth).
"""
