# Changelog

All notable changes to this skill are recorded here. Format loosely follows Keep a Changelog; versions follow semver.

## 2.9.0 — 2026-11-03

### Added

- `corpus/05-walkthrough/meeting-actions-walkthrough.md` — a third walkthrough, and the first one built on a deliberately messy input: a raw meeting note with colloquialisms, gaps and a topic left unresolved. Demonstrates sorting seven paragraphs into decisions, actions, discussion and notices; six actions survive, two open questions get flagged as risks, one date moves to the calendar.

## 2.8.0 — 2026-11-03

### Added

- `corpus/05-walkthrough/competitor-brief-walkthrough.md` — a second walkthrough: a competitor brief done in two steps, built around source grading (first-hand, second-hand, third-hand), three of five raw intel items surviving the cut, and a recommendation to verify before reacting.
- Six screenshot thumbnails under `assets/samples/`, wired into the README as a two-column preview grid so readers see the output before clicking.

### Changed

- The samples section now shows what each page looks like instead of describing it.

## 2.7.0 — 2026-11-03

### Added

- `references/corpus/05-walkthrough/` — a complete walkthrough of all seven steps on one task: task card, brief, action list, flow, stats table, deck outline, review record, plus the state file and a retrospective on the walkthrough itself. Data and company are fictional; the snags are realistic.
- `04-real/README.md` now spells out the difference from the walkthrough folder: evidence versus sample.

## 2.6.0 — 2026-11-03

### Added

- `references/maturity.md` — four maturity levels (assisted, controlled automation, autonomous execution, self-optimising), the three things needed to climb, four governance questions, and the shift from "it worked once" to "success rate over ten runs".
- Four more HTML samples: weekly report, meeting minutes, action list, and an index page. Six in total, all reachable through GitHub Pages.
- `templates/rules.json` — a trigger rule table: what signal, what to do, which template, and whether to notify a person.

### Changed

- Every example now has a live URL under the project's Pages site, so samples open in a browser instead of showing raw source.
- The platform badge names no specific vendor.

## 2.5.0 — 2026-11-03

### Added

- `references/mindset.md` — five ways of thinking that change the output by changing the question: first principles, adversarial review, ablation, Occam's razor, boundary check. Each carries an office-scenario example, plus a section on retiring steps that no longer earn their place.
- `references/automation.md` — from human-driven to signal-driven: three trigger types (schedule, event, threshold), a rule table whose last column decides when to bother a person, one exit, two lists of settled decisions, and periodic subtraction.
- `templates/pipeline-state.yaml` — an optional state file recording per-step status, artifact path, provenance and blockers. Plain text, no parser needed, so it does not break the zero-dependency rule.
- Main file gained a section on when to start, and the reference index lists both new volumes.

### Changed

- Corpus provenance now names methods and fields only, never people or source articles.

## 2.4.0 — 2026-11-03

### Added

- Seven operating principles in the main file, drawn from orchestrator design patterns: classify before acting, route by deliverable, compose rather than enumerate, types must connect, define once, intermediates stay internal, one line of provenance per step.
- A "what this does not cover, and where it goes" table: quick edits, single answers, finished decks, code, negotiation, unprepared data.
- The seven-step table now carries an artifact-type column, so it is visible which outputs can feed which step.

### Changed

- Handoff rules are marked as the single definition; other sections reference rather than repeat them.

## 2.3.0 — 2026-11-03

### Added

- `references/corpus/00-sources.md` — provenance for every piece: which methods belong to the public domain (GRAI, KPT, AAR, structured-writing frameworks, 5W2H), what the corpus does not do (no copied passages, no licensed assets, fictional data), and a five-point checklist for judging any template.
- Source headers on all three corpus files, each stating what is derived and what is self-written.
- `references/corpus/04-real/` — rules for filing real outputs: what qualifies, naming, the five mandatory header fields, redaction limits, and a template.

## 2.2.0 — 2026-11-03

### Added

- `references/corpus/01-formats.md` — six document skeletons (weekly, monthly, minutes, email, proposal, retrospective), each with acceptance tests and common mistakes. Retrospective covers GRAI, KPT and AAR, plus the four taboos.
- `references/corpus/02-phrases.md` — a phrase bank organised by where it sits in a document, with a banned-word list and a weak-to-strong rewrite table, plus rules for numbers and dates.
- `references/corpus/03-samples.md` — six full samples across ops, project management, meetings, cross-team email, a one-page proposal and a GRAI retrospective. Each marks what to copy and what not to.
- Main file gained a section on how to use the corpus: copy the structure, rewrite the phrasing, replace every number.

## 2.1.0 — 2026-11-03

### Added

- `examples/research-brief.html` and `examples/monthly-review.html` — two finished HTML outputs. Single file, no external assets, print-friendly. They double as templates: copy, replace the content, ship.
- README section "What the output looks like", linking both.
- `references/steps-deep.md` gained the definition step and the review step, so all seven are documented at the same depth.

### Fixed

- Every remaining reference to the old five-step framing now reads seven steps, including the reference index, variants, scenarios, examples, and the contributing guide.

## 2.0.0 — 2026-11-02

### Changed

- The skill is now about **designing** a pipeline, not only running one. The main file gained a seven-move design section, a section on fixing an existing pipeline, and a section on documenting a pipeline for other people.
- Steps grew from five to seven: a definition step at the front and a review step at the end. The middle five are unchanged.
- The step count is no longer fixed. The main file states the only test for splitting: whether input, risk and definition-of-done genuinely differ.
- README and both figures rebuilt around seven steps.

### Added

- `references/design.md` — the full design method, with six traps and three fix patterns.
- `references/sharing.md` — the eight-section documentation pattern, three formats, and a pre-publish checklist.
- `templates/00-define.md` — the task-card template for step zero.

## 1.1.0 — 2026-11-02

### Added

- `templates/` — six copy-paste prompts, one per step plus a weekly-report variant. Each carries inputs, the prompt itself, an output contract and an acceptance list.
- `CONTRIBUTING.md` — how to propose a change, what a good template looks like, what gets rejected.
- `references/scenarios.md` — three extensions: client-facing material, cross-team output, adapting the seven steps to an industry workflow.
- `assets/cover.svg` and `assets/pipeline.svg`, generated by `tools/gen_assets.py`.
- Main file gained four sections: why splitting helps (three mechanisms), how to set checkpoints, what to do when stuck, and when not to use the pipeline.

### Changed

- README now opens with the cover, and the ASCII pipeline diagram became a vector figure.
- Reference index in `SKILL.md` lists all five reference files.

### Removed

- Provenance note in `metadata.source` and its two references in the READMEs, at the author's request.

## 1.0.0 — 2026-11-02

### Added

- Initial release: seven-step office pipeline (research, read, map, tabulate, report), four reference files, universal installer covering 18 AI tools, plugin manifests for four ecosystems.
