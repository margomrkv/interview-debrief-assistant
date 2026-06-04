# Public release notes

**Last updated:** 2026-06-04

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
| `course/final_project/AM_Best_Offer_feedback.md` | [`COURSE_REVIEW.md`](COURSE_REVIEW.md) |
| `course/final_project/Project Criteria & Scoring.docx` | [`review/project-criteria-scoring.docx`](review/project-criteria-scoring.docx) |
| `course/final_project/Post-Interview … en_v1.docx` | [`review/project-report-en_v1.docx`](review/project-report-en_v1.docx) |

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

```bash
cd /Users/mm/projects/ds-final-project-public
git remote add origin git@github.com:<org>/<new-public-repo>.git
git push -u origin --all
git push origin --tags   # if any
```

Use a **new** empty public repository; do not force-push over the private `am-best-offer` remote without team agreement.
