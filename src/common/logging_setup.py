"""Single entry point for all train-pipeline logging.

Every script (`scripts/train_prompt.py`, `src/kb/build_splits.py`,
`src/kb/train.py`, `src/common/evaluate.py`) calls `configure_logging(...)`
first thing in its `main()`. The function:

- installs one stdout `StreamHandler` and optionally one append-mode
  `FileHandler` (so all three sub-steps mirror into a single
  `runs/<id>/logs/pipeline.log`);
- normalises DSPy's own loggers to our format (drops their default handler
  + lets records propagate to root);
- silences known non-actionable warnings (LiteLLM bedrock/sagemaker
  pre-load, Optuna `multivariate` ExperimentalWarning);
- is idempotent — re-entrant calls only update the file handler.
"""
from __future__ import annotations

import logging
import sys
import warnings
from pathlib import Path

_FMT = "%(asctime)s [%(levelname)s] [%(name)s] %(message)s"
_DATEFMT = "%H:%M:%S"
_MARKER = "_am_best_offer_logging_configured"
_FILE_HANDLER_ATTR = "_am_best_offer_log_file_handler"

_LITELLM_BEDROCK_FRAGMENTS = (
    "could not pre-load bedrock-runtime",
    "could not pre-load sagemaker",
)


class _LiteLLMBedrockFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        try:
            msg = record.getMessage()
        except Exception:
            return True
        return not any(frag in msg for frag in _LITELLM_BEDROCK_FRAGMENTS)


def _silence_known_warnings() -> None:
    try:
        from optuna.exceptions import ExperimentalWarning  # type: ignore

        warnings.filterwarnings("ignore", category=ExperimentalWarning)
    except ImportError:
        pass

    litellm_logger = logging.getLogger("LiteLLM")
    if not any(isinstance(f, _LiteLLMBedrockFilter) for f in litellm_logger.filters):
        litellm_logger.addFilter(_LiteLLMBedrockFilter())


# Eagerly attach the LiteLLM bedrock/sagemaker filter — these warnings fire at
# `import dspy` time (before any main() can call configure_logging), so we have
# to install the filter at this module's import. Entry-point scripts must
# import this module BEFORE importing dspy.
_silence_known_warnings()


def _reformat_dspy_loggers() -> None:
    # DSPy attaches its own StreamHandler with a different timestamp format on
    # `dspy.teleprompt.*` / `dspy.evaluate.*`. Drop them and let records bubble
    # up to root so they pick up our formatter.
    for name in (
        "dspy",
        "dspy.teleprompt",
        "dspy.teleprompt.mipro_optimizer_v2",
        "dspy.teleprompt.mipro_v2",
        "dspy.evaluate",
        "dspy.evaluate.evaluate",
    ):
        lg = logging.getLogger(name)
        for h in list(lg.handlers):
            lg.removeHandler(h)
        lg.propagate = True


def configure_logging(
    component: str,
    log_file: Path | None = None,
    verbose: bool = False,
) -> logging.Logger:
    """Configure root logging and return a component-scoped logger.

    Idempotent: safe to call from multiple entry points / re-invocations.
    """
    root = logging.getLogger()
    level = logging.DEBUG if verbose else logging.INFO
    root.setLevel(level)

    if not getattr(root, _MARKER, False):
        formatter = logging.Formatter(_FMT, datefmt=_DATEFMT)
        stream = logging.StreamHandler(stream=sys.stdout)
        stream.setFormatter(formatter)
        root.addHandler(stream)
        _reformat_dspy_loggers()
        setattr(root, _MARKER, True)

    if log_file is not None:
        existing: logging.FileHandler | None = getattr(root, _FILE_HANDLER_ATTR, None)
        log_file = log_file.resolve()
        if existing is None or Path(existing.baseFilename) != log_file:
            if existing is not None:
                root.removeHandler(existing)
                existing.close()
            log_file.parent.mkdir(parents=True, exist_ok=True)
            fh = logging.FileHandler(log_file, mode="a", encoding="utf-8")
            fh.setFormatter(logging.Formatter(_FMT, datefmt=_DATEFMT))
            root.addHandler(fh)
            setattr(root, _FILE_HANDLER_ATTR, fh)

    return logging.getLogger(component)
