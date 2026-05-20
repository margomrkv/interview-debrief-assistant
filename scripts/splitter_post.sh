#!/usr/bin/env bash
# Post-LLM splitter: JSON → xlsx → validation-report.md; step 5 prompt → pipeline-log.md (LLM via Cursor agent).
# Updates {basename}.vN.pipeline-log.md for steps 3–4.
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "Usage: splitter_post.sh <path/to/*.vN.qa-split.json> [--video path/to/video.md] [--section-config path.json]" >&2
  echo "       (legacy *.qa-split.vN.json also accepted)" >&2
  exit 1
fi

JSON_PATH="$1"
shift

VIDEO_PATH=""
SECTION_CONFIG=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --video)
      VIDEO_PATH="${2:?}"
      shift 2
      ;;
    --section-config)
      SECTION_CONFIG="${2:?}"
      shift 2
      ;;
    *)
      echo "Unknown argument: $1" >&2
      exit 1
      ;;
  esac
done

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SKILL="$REPO_ROOT/.claude/skills/splitter"

if [[ ! -f "$JSON_PATH" ]]; then
  echo "ERROR: JSON not found: $JSON_PATH" >&2
  exit 1
fi

if [[ "$JSON_PATH" != /* ]]; then
  JSON_PATH="$REPO_ROOT/$JSON_PATH"
fi

# New: {slug}.vN.qa-split.json  Legacy: {slug}.qa-split.vN.json
if [[ "$JSON_PATH" =~ \.v([0-9]+)\.qa-split\.json$ ]]; then
  VER="${BASH_REMATCH[1]}"
  BASE="${JSON_PATH%.v${VER}.qa-split.json}"
  XLSX_PATH="${BASE}.v${VER}.qa-split.xlsx"
  VALIDATION_PATH="${BASE}.v${VER}.validation-report.md"
  PIPELINE_LOG_MD="${BASE}.v${VER}.pipeline-log.md"
elif [[ "$JSON_PATH" =~ \.qa-split\.v([0-9]+)\.json$ ]]; then
  VER="${BASH_REMATCH[1]}"
  BASE="${JSON_PATH%.qa-split.v${VER}.json}"
  XLSX_PATH="${BASE}.qa-split.v${VER}.xlsx"
  VALIDATION_PATH="${BASE}.qa-split.validation.v${VER}.md"
  PIPELINE_LOG_MD="${BASE}.v${VER}.pipeline-log.md"
else
  XLSX_PATH="${JSON_PATH%.json}.xlsx"
  VALIDATION_PATH="${JSON_PATH%.json}.validation-report.md"
  PIPELINE_LOG_MD="${JSON_PATH%.json}.pipeline-log.md"
fi

T0=$(date +%s)

python3 "$SKILL/step3-excel/splitter_json_to_excel.py" \
  "$JSON_PATH" \
  --out "$XLSX_PATH"

T1=$(date +%s)
EXCEL_SEC=$((T1 - T0))

if [[ -n "$VIDEO_PATH" ]]; then
  if [[ "$VIDEO_PATH" != /* ]]; then
    VIDEO_PATH="$REPO_ROOT/$VIDEO_PATH"
  fi
  if [[ ! -f "$VIDEO_PATH" ]]; then
    echo "ERROR: video.md not found: $VIDEO_PATH" >&2
    exit 1
  fi
  VAL_ARGS=(
    --splitter "$JSON_PATH"
    --video "$VIDEO_PATH"
    --tolerance 120
    --out "$VALIDATION_PATH"
    --prepare-llm
  )
  if [[ -n "$SECTION_CONFIG" ]]; then
    if [[ "$SECTION_CONFIG" != /* ]]; then
      SECTION_CONFIG="$REPO_ROOT/$SECTION_CONFIG"
    fi
    VAL_ARGS+=(--section-config "$SECTION_CONFIG")
  fi
  T2=$(date +%s)
  python3 "$SKILL/step4-validate-chapters/splitter_validate_video.py" "${VAL_ARGS[@]}"
  T3=$(date +%s)
  VAL_SEC=$((T3 - T2))
  echo "Validation: $VALIDATION_PATH"
  echo "Step 5: LLM_INPUT_STEP_5 in ${PIPELINE_LOG_MD:-pipeline-log} — agent runs next (same chat as step 2)."
else
  VAL_SEC=0
  echo "Skip validation (no --video)."
fi

if [[ -f "$PIPELINE_LOG_MD" ]]; then
  python3 "$SKILL/scripts/splitter_run_log.py" \
    --pipeline-log "$PIPELINE_LOG_MD" \
    --step 3 \
    --name "excel" \
    --input "$JSON_PATH" \
    --output "$XLSX_PATH" \
    --duration-sec "$EXCEL_SEC"
  if [[ -n "$VIDEO_PATH" ]]; then
    python3 "$SKILL/scripts/splitter_run_log.py" \
      --pipeline-log "$PIPELINE_LOG_MD" \
      --step 4 \
      --name "validate_chapters" \
      --input "$JSON_PATH" \
      --input "$VIDEO_PATH" \
      --output "$VALIDATION_PATH" \
      --duration-sec "$VAL_SEC"
  fi
  echo "Pipeline log: $PIPELINE_LOG_MD"
fi

echo "Excel: $XLSX_PATH"
