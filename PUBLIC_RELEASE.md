# Public release notes

**Last updated:** 2026-06-04  
**Remote:** [`margomrkv/interview-debrief-assistant`](https://github.com/margomrkv/interview-debrief-assistant) (private; flip to public after team review)

This directory (`ds-final-project-public/`) is a **sanitized mirror** of the private course repo. The original repo at `../ds-final-project/` is unchanged.

## Removed from entire git history

- `data/candidatecontext/` — private interview transcripts, CVs, feedback
- `candidatecontext/`, `marketflow/`, `transcripts/anton*`, `examples/candidatecontext/`
- `docs/meetings/` — internal team / mentor call transcripts
- `course/` — lecture slides, workshops, assignments
- `data/emulator-data/anton/` — UI demo derived from a private interview

## Reorganized for reviewers

| Was | Now |
|-----|-----|
| `course/final_project/AM_Best_Offer_feedback.md` | [`REVIEW_REPORT.md`](REVIEW_REPORT.md) |
| `docs/PROJECT_OVERVIEW.md` | [`docs/PROJECT_REPORT.md`](docs/PROJECT_REPORT.md) |
| `course/final_project/Project Criteria & Scoring.docx` | [`submission/project-criteria-scoring.docx`](submission/project-criteria-scoring.docx) |
| `course/final_project/Post-Interview … en_v1.docx` | [`submission/project-report-en_v1.docx`](submission/project-report-en_v1.docx) |

## History rewrite (three passes)

1. **Path purge** — removed sensitive directories from all commits (`git filter-repo --invert-paths`).
2. **Leftover paths** — `examples/candidatecontext/`, `transcripts/anton-*`.
3. **String redaction** — replaced path literals in docs/skills across history (e.g. `candidatecontext/anton/` → `[private]/`).

## Verify locally

```bash
git rev-list --all --objects | grep -E 'candidatecontext|transcripts/anton|marketflow|docs/meetings|course/|emulator-data/anton' || echo OK
git grep -l 'candidatecontext/anton' $(git rev-list --all) || echo OK
```

## Publish to GitHub

Repository created as **private** first; make public only after Anton / team sign-off.

```bash
cd /Users/mm/projects/ds-final-project-public
git remote add origin https://github.com/margomrkv/interview-debrief-assistant.git
# or: git@github.com:margomrkv/interview-debrief-assistant.git

git checkout master && git merge ui2
git push -u origin master
git push origin ui2          # optional: keep feature branch on remote
git push origin --tags       # if any
```

Clone for reviewers:

```bash
git clone https://github.com/margomrkv/interview-debrief-assistant.git
cd interview-debrief-assistant
python3 src/ui/app.py 18000   # http://127.0.0.1:18000 → Transcript Lens → Use demo
pytest tests/
```

Do **not** force-push over the private course repo (`am-best-offer`) without team agreement.
