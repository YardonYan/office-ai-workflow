<div align="center">

[中文](./README.md) · **English**

# office-ai-workflow

#### Design an office pipeline, then run it

[![Version](https://img.shields.io/badge/version-2.0.0-green.svg)](SKILL.md)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-Standard-8B5CF6.svg)](https://agentskills.io)
[![Dependencies](https://img.shields.io/badge/dependencies-0-brightgreen.svg)](#compatibility)
[![Steps](https://img.shields.io/badge/steps-7-D97706.svg)](#the-seven-steps)

</div>

<p align="center">
  <img src="./assets/cover.svg" width="100%" alt="office-ai-workflow: a seven-step office pipeline">
</p>

---

> Stop treating the assistant as a chat window. Chain the scattered office work into one line: brief each step properly, let each output feed the next, and have a person check only the numbers and the conclusion.

This skill does two things: **design a pipeline for a recurring kind of work**, and **run one task through an existing pipeline**.

## Two ways in

| Your situation | Start here |
|---|---|
| One concrete task to finish efficiently | Go straight to the seven steps |
| A recurring kind of work you keep rethinking from scratch | Read "Designing your own pipeline" first |
| A pipeline that keeps stalling at one step | Read "Fixing an existing pipeline" |
| A pipeline you want others to use | Read "Writing it down for other people" |

Most people are stuck on the second one: they know AI should help here, but do not know how to start. That section is the point of this repo.

## The seven steps

Two steps at the ends, five in the middle. The end steps are the ones people skip, and the ones that decide whether the rest works.

<p align="center">
  <img src="./assets/pipeline.svg" width="100%" alt="Seven steps and their handoffs: task card, brief, action list, flow, stats table, draft deck, review record">
</p>

| # | Step | Hands over | In one line |
|---|---|---|---|
| 0 | Define | Task card | Goal, scope, output contract, written before you start |
| 1 | Research | Brief | Bound the range, compress into three columns you can act on |
| 2 | Read | Action list | Extract five fields, never paraphrase the whole document |
| 3 | Map | Flow | Mark parallel work, review gates and handoffs |
| 4 | Tabulate | Stats table | Lock the definition first, write the formula down |
| 5 | Report | Draft deck | One conclusion per slide, numbers quoted from the table |
| 6 | Review | Review record | Numbers, definitions and conclusions all reconcile |

The step count is not fixed. Three steps is fine if that is what your task has; nine is fine too. The only test: **is this step's input, risk and definition of done genuinely different from the next one.**

## Designing your own pipeline

Seven moves, for people who do not know where to start.

| Move | The judgement that matters |
|---|---|
| 1. Find the repetition | Start with the one you dread most each week |
| 2. Decide if it deserves a pipeline | Still doing it next month, over half an hour, inconsistent results — two of three |
| 3. Split on decisions, not on files | Split where input, risk or done-criteria differ |
| 4. Write the contract per step | The done-criterion must be answerable yes or no |
| 5. Chain it, check the handoffs | If you cannot name the artifact between two steps, merge them |
| 6. Run one real task through it | Watch where it stalls and which output the next step cannot use |
| 7. Fix and freeze | Prompts become templates, outputs become samples, boundaries get written |

Full version with six common traps and three fix patterns: [`references/design.md`](./references/design.md).

## Writing it down for other people

A pipeline only you can run is not a pipeline. Eight sections when you share it:

purpose (including **what it does not do**) · when to use · inputs (including **what counts as bad input**) · output contract · guardrails · examples · how to run · changelog.

The two most-skipped sections are the output contract and the bad-input note. They are also the two that decide whether anyone else can use it. Details: [`references/sharing.md`](./references/sharing.md).

## Templates

Seven copy-paste prompts under `templates/`. Each carries inputs, the prompt, an output contract, an acceptance list and failure handling.

| Template | Use it when |
|---|---|
| [`00-define.md`](./templates/00-define.md) | Defining the boundary before starting |
| [`01-brief.md`](./templates/01-brief.md) | Scattered information into a one-page brief |
| [`02-extract.md`](./templates/02-extract.md) | Long documents into an action list |
| [`03-map.md`](./templates/03-map.md) | A multi-step process into a diagram |
| [`04-stats.md`](./templates/04-stats.md) | A ledger into a stats table |
| [`05-report.md`](./templates/05-report.md) | Materials ready, need a deck outline |
| [`06-weekly.md`](./templates/06-weekly.md) | The weekly report, three-step variant |

## Quick start

Send this to your assistant:

```
Use office-ai-workflow to turn these files into a monthly review.
Focus on customer feedback and blockers. Output a brief, an action list,
a stats table and a deck outline. Keep the original source for every number.
```

It works the steps one at a time and stops at each checklist before moving on.

## Install

```bash
git clone https://github.com/YardonYan/office-ai-workflow.git
cd office-ai-workflow
node tools/install.mjs --list      # which apps are on this machine
node tools/install.mjs --ai all    # install to all of them
```

Zero dependencies, Node standard library only. Also supports `--dry-run`, `--force`, `--uninstall`, `--project` and `--dir`.

Supported apps include WorkBuddy, CodeBuddy, TRAE (CN and international), Qoder (CN and international), QoderWork, Qwen Code, Lingma, Kimi Code CLI, iFlow CLI, CodeArts Doer, OpenClaw, Claude Code, Codex CLI, Cursor and the shared `~/.agents/skills` convention. Run `--list` for the exact paths.

## What's inside

| File | Content |
|---|---|
| `SKILL.md` | Main file: two ways in, seven steps, design moves, fixing, writing down, checkpoints, failure handling |
| `references/design.md` | Designing from scratch: three starting points, observing a real run, six traps, a minimum viable pipeline |
| `references/sharing.md` | Documenting it: eight sections, three formats, the first screen, upkeep |
| `references/why-and-how.md` | How others build pipelines: four schools and what they share |
| `references/steps-deep.md` | Per-step inputs, actions, output definition, checklist, common mistakes |
| `references/variants.md` | Six variants: three-step, weekly, retrospective, meeting, competitor, chat-only |
| `references/scenarios.md` | Client-facing material, cross-team output, adapting to an industry |
| `references/examples.md` | Three worked cases |
| `templates/` | Seven copy-paste prompt templates |

## Non-negotiables

1. The assistant drafts and organizes. Numbers, sources and conclusions get human review before they leave the room.
2. Keep the original evidence. Never invent figures, owners or dates. Mark missing fields instead of guessing.
3. Each step's checklist must pass before the next one starts.
4. Redact sensitive material before it enters the pipeline.

## Compatibility

Built on the [Agent Skills](https://agentskills.io) open standard: one directory, one `SKILL.md`, frontmatter limited to the fields the spec allows. Any tool that reads the standard loads it without conversion.

The skill needs no scripts, network or packages. Files under `tools/` only install the skill and generate assets and plugin manifests.

## Contributing

Templates and scenario variants are welcome. See [`CONTRIBUTING.md`](./CONTRIBUTING.md).

## License

[Apache-2.0](./LICENSE), `Copyright 2026 YardonYan`.
