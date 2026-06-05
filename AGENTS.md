# Agent Instructions

## Splitter pipeline

Reproducible Q&A split: **`.claude/skills/splitter/SKILL.md`** (Cursor `/splitter` + Claude Code `/splitter`) — steps 1–5, then correction loop until `splitter_verdict.py` exit 0. Post-LLM: `.claude/skills/splitter/step3-excel/splitter_post.sh`.

## Non-Interactive Shell Commands

**ALWAYS use non-interactive flags** with file operations to avoid hanging on confirmation prompts.

```bash
cp -f source dest    # NOT: cp source dest
mv -f source dest    # NOT: mv source dest
rm -f file           # NOT: rm file
rm -rf directory     # NOT: rm -r directory
```

**Other commands that may prompt:** `scp -o BatchMode=yes`, `ssh -o BatchMode=yes`, `apt-get -y`, `HOMEBREW_NO_AUTO_UPDATE=1 brew …`

## Rules

Do not run tests against paid models during development unless necessary.
