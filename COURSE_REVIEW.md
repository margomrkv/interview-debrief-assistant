# Course review — AM Best Offer (Post-Interview Debrief Assistant)

Instructor feedback and rubric scores for the Data Sanity final project (2026).
See also [`review/project-criteria-scoring.docx`](review/project-criteria-scoring.docx) for the official criteria document.

## What worked well

- A deliberate two-stage prompt-chaining pipeline (Splitter → Scoring) with an honest write-up of why it's a workflow, not an agent.
- A genuinely real DSPy / MIPROv2 prompt-optimization training loop on a 169-item human-labeled gold set, with session-level 70/30 train/test split and publisher stratification.
- An interpretable soft-tolerance evaluation metric with median-predictor baselines and 95% bootstrap confidence intervals — and real, reproducible numbers committed to `docs/PROJECT_OVERVIEW.md` and `examples/trains/`.
- The cleanest module separation in the cohort: `splitter` / `assessor` / `kb` / `ui` / `common` each carry a single responsibility, the LLM client lives behind one factory, and the UI hides the backend behind a `Protocol` so emulator and live share the rollup math.
- Production-aware details: `extra_body={"reasoning":{"exclude":True}}` for OpenRouter reasoning models, centralized + idempotent logging setup, model choice justified per role.
- Real streaming UI with SSE, two screens (upload → results), drag-and-drop, "Use demo" alternative, per-question cards with progressive scoring, and a verdict pane.
- Tests across `splitter / assessor / ui / common / kb` covering metric math, eval runner, the live UI backend with both LLMs mocked, report rollup, splitter JSON edge cases, and loggers.

## Scores

### Technical Implementation — 19.5 / 20 (+ 0 bonus)

| Criterion | Score | Max |
|---|-------|---|
| AI Design | 5     | 5 |
| Code Design | 4     | 4 |
| Works-as-expected | 4     | 4 |
| Evaluation | 3.5   | 4 |
| Tests | 2     | 2 |
| Logging | 1     | 1 |
| (bonus) Deployment | 0     | 2 |

**AI Design — 5/5.** The approach is tight and thoughtfully scoped: a deliberate workflow (not an agent), schema-guided JSON extraction with a validator loop in the Splitter, a trained DSPy ChainOfThought signature in the Assessor, and a MIPROv2-optimized evaluator prompt trained against a human-labeled gold set with proper session-level train/test split. Hyper-parameter choices are documented (TOL_BAND=2 rationale, MIN_DEMO_SCORE=0.85, anchored 1–10 scale in the prompt). The only attack surface is file upload, and PII/injection guardrails would reasonably be out of scope for a student project of this shape.

**Code Design — 4/4.** A pleasure to read: clean module split with single responsibilities, no scattered LLM calls, prompts isolated under `prompts/`, the LLM client wrapped behind one factory, strictly one-way dependencies (`ui` → `assessor`/`splitter` → `common`, `kb` → `common`), and a UI `Protocol` with `EmulatorBackend` / `LiveBackend` cleanly separated and lazy-imported. Consistent naming and typing, `from __future__ import annotations` everywhere, explicit dataclasses for the wire format. Even the logging setup is centralized and idempotent.

**Works-as-expected — 4/4.** End-to-end path is fully implemented and flows smoothly: upload / "Use demo" → SSE stream → Splitter LLM call → per-item Scoring LLM call → rollup verdict → frontend renders. The trained prompt artifact is committed, example train artifacts live in `examples/trains/gpt-5.4-nano-final/`, and the live UI was confirmed working during review.

**Evaluation — 3.5/4.** Genuine evaluation infrastructure that stands out in the cohort: 244-item hard-skill corpus, 169 with Opus-labeled reference scores, session-level 70/30 split with publisher stratification, a soft-tolerance metric with median-predictor baseline and 95% bootstrap CIs, and auto-generated train/test reports under `runs/<run_id>/`. Real results are reported and interpreted (gpt-5.4-nano: train 0.514, test 0.506 [0.426, 0.588] vs baseline 0.298; gemma under-performs the test baseline; overfit gap discussed honestly). Baseline + test set + bootstrap CIs is more than most teams ship. The one area to refine is the gold-set labeling — it was produced by Opus without human verification. It's a reasonable bootstrapping approach, though it's hard to be sure the initial labels are calibrated well enough; a spot-check pass by a human would lift confidence in the numbers.

**Tests — 2/2.** Strong test coverage across the surfaces that matter: the metric math, the eval runner, the live UI backend with both LLM calls mocked (real integration of UI + emulator catalogue + mocked splitter/assessor), the report rollup, splitter JSON parsing edge cases, and the score/prompt loggers. Meaningful unit + integration coverage.

**Logging — 1/1.** Both LLM stages log input/output thoroughly. Splitter writes `LLM_INPUT_STEP_2` / `LLM_INPUT_STEP_5` into `*.pipeline-log.md` plus stderr; training writes per-iteration cost JSONL, a `PromptTracer` trace JSONL, a per-iteration scores CSV, and an aggregate pipeline log. Optional Phoenix tracing is wired.

**Deployment — 0/2 (bonus).** This is the easy bonus to pick up next time: there's currently no Dockerfile, docker-compose, or hosted URL, and the README only documents local `make ui-emulator` / `make ui-live`. Since the emulator backend needs no API keys, a free-tier deploy would be essentially free credit and worth grabbing.

### Interface — 8 / 10

| Criterion | Score | Max |
|---|---|---|
| UI | 3 | 4 |
| Reliable UI | 2 | 3 |
| Intuitive UI | 3 | 3 |

**UI — 3/4.** A real web UI with SSE streaming, two screens, drag-and-drop, "Use demo" button, per-Q&A cards with live scoring updates, and a final verdict pane. Wired to both emulator and live backends with an identical streaming contract — the architecture here is genuinely nice. The opportunity to lift this further is one interaction in emulator mode: when a user uploads a transcript that doesn't match a demo file, the UI prints "This is a demo emulator — it can only process the demo file", since fresh ingest only works in live mode. Making that path either gracefully fall back to live or surface clearer guidance would round out the experience.

**Reliable UI — 2/3.** Solid defensive foundations are in place: the SSE handler wraps the whole pipeline in `try/except` for `BrokenPipeError`/`ConnectionResetError`, both LLM stages swallow exceptions to safe defaults, and the frontend renders a "No interviewer signal — not scored" badge per item that fails. The main thing to look at next is making errors more legible to the user — currently failures degrade to silence rather than distinct messages. Worth exploring: separate paths for "API down" vs "transcript empty" vs "rate-limited", input validation on the upload, and a user-facing error when the splitter LLM call itself fails (today the stream just emits zero items with no diagnostic in the UI).

**Intuitive UI — 3/3.** Genuinely easy to use: two clear screens (upload vs results), drag-and-drop with a prominent "Use demo" alternative, per-question cards with progressive disclosure as scoring completes, and a verdict pane with HIRE/NO_HIRE chip and p(hire). UI strings are consistent and the visual hierarchy reads at a glance.

## Presentation Feedback

| Aspect | Score | Max |
|---|---|---|
| Problem Statement | 4 | 4 |
| Architecture Briefing | 4 | 4 |
| App Demo | 2 | 4 |
| Metrics Briefing | 3 | 4 |
| Presentation Overall | 4 | 4 |

Good presentation and clear speech — the area that can be tightened is the app demo. You showed the interface briefly without explaining what was actually inside it, which leaves the audience wondering. Two possible rearrangements that would land better: either *open* with the interface, walk through what's in scope, and then move into how it's built; or *close* with a proper demo (which often works better, since the task itself is understandable enough that the audience won't need the UI to follow you). Whichever framing you pick, give the demo a real beat — show the metrics being calculated for each transcript, name what they mean, and tie that back to the value to the candidate. The work is solid; this is just about giving the demo the airtime it deserves.
