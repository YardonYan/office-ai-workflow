

<div align="center">

[Two ways in](#two-ways-in) · [Seven steps](#the-seven-steps) · [Quick start](#quick-start) · [Samples](#what-the-output-looks-like) · [Principles](#seven-operating-principles) · [Thinking](#five-ways-of-thinking) · [Maturity](#maturity-and-governance) · [Design](#designing-your-own-pipeline) · [Write it down](#writing-it-down-for-other-people) · [Templates](#templates) · [Contracts](#output-contracts) · [Corpus](#corpus) · [Install](#install) · [Contents](#what's-inside)

</div>

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

## Quick start

Send this to your assistant:

```
Use office-ai-workflow to turn these files into a monthly review.
Focus on customer feedback and blockers. Output a brief, an action list,
a stats table and a deck outline. Keep the original source for every number.
```

It works the steps one at a time and stops at each checklist before moving on.

## What the output looks like

Six single-file HTML pages. Open one and you are looking at a finished deliverable — copy it, replace the content, ship it.

<p align="center"><sub>Live preview · <a href="https://yardonyan.github.io/office-ai-workflow/examples/">yardonyan.github.io/office-ai-workflow/examples</a></sub></p>

| | |
|---|---|
| <a href="https://yardonyan.github.io/office-ai-workflow/examples/research-brief.html"><img src="./assets/samples/research-brief.png" width="330" alt="信息简报"></a><br><sub><b>信息简报</b> · 三列结构，结尾一个建议动作</sub> | <a href="https://yardonyan.github.io/office-ai-workflow/examples/action-list.html"><img src="./assets/samples/action-list.png" width="330" alt="行动清单"></a><br><sub><b>行动清单</b> · 五要素提取，负责人缺失怎么标</sub> |
| <a href="https://yardonyan.github.io/office-ai-workflow/examples/weekly.html"><img src="./assets/samples/weekly.png" width="330" alt="周报"></a><br><sub><b>周报</b> · 三段式，四百字以内</sub> | <a href="https://yardonyan.github.io/office-ai-workflow/examples/minutes.html"><img src="./assets/samples/minutes.png" width="330" alt="会议纪要"></a><br><sub><b>会议纪要</b> · 五段结构，待办四列</sub> |
| <a href="https://yardonyan.github.io/office-ai-workflow/examples/monthly-review.html"><img src="./assets/samples/monthly-review.png" width="330" alt="月度复盘"></a><br><sub><b>月度复盘</b> · 五页骨架，数据与口径</sub> | <a href="https://yardonyan.github.io/office-ai-workflow/examples/index.html"><img src="./assets/samples/index.png" width="330" alt="示例目录"></a><br><sub><b>示例目录</b> · 全部示例的入口页</sub> |

All single-file, dependency-free, print-friendly.

## Seven operating principles

More important than memorising the seven steps. Scenarios vary; the principles do not.

| # | Principle | In one line |
|---|---|---|
| 1 | Classify before acting | One-off or a pipeline, what form is the deliverable, what material exists — answer all three first |
| 2 | Route by deliverable, not by name | The same request name can hide two paths; look at what ships, not what it is called |
| 3 | Compose, do not enumerate | The seven steps are a standard composition, not the only one |
| 4 | Types must connect | Each step's output has a type; the next step can only consume a matching one. A gap means a missing step |
| 5 | Define once | Handoff rules are defined in one place and referenced elsewhere; duplicated definitions drift |
| 6 | Intermediates stay internal | Briefs, lists, tables and diagrams are intermediate: give a path and a one-line summary, not a polished deliverable |
| 7 | One line of provenance per step | Not a tick box: what was checked and what was concluded |

Some work looks like office work but should not go through a pipeline. The test: if it needs one decision or one action, skip the pipeline. Pipelines exist for multiple handoffs, multiple people, and a record.

## Five ways of thinking

The seven steps set the order; this section sets how to think. Five prompts, each a mature method — say one and the mode switches.

| Method | In one line | Use it when |
|---|---|---|
| First principles | Stop optimising the current plan; re-ask what this is for | You suspect the task itself is framed wrong |
| Adversarial review | Do not justify it; find counterexamples that break the core assumption | Before a proposal is final, before a deck ships |
| Ablation | Remove one change at a time and see where the gain really came from | You made several changes at once |
| Occam's razor | Remove every step that is not necessary | The pipeline keeps growing |
| Boundary check | Is the responsibility split clean, should this be two documents | Structure is muddled, too many people involved |

Chained, they map to five cognitive moves: reframe the problem, attack the assumption, verify the contribution, delete complexity, tidy the boundaries.

Details and office-scenario examples: [`references/mindset.md`](./references/mindset.md).

## Maturity and governance

Building the pipeline is the start. You also need to know what level it sits at and whether it can fail safely.

| Level | Name | Test |
|---|---|---|
| L1 | Assisted generation | A person drives, the assistant drafts |
| L2 | Controlled automation | Fixed steps, fixed artifacts, a person only checks (the seven steps live here) |
| L3 | Autonomous execution | Triggered by signals, only escalates on exceptions |
| L4 | Self-optimising | Spots its own redundancy and proposes removal |

Most office work stops at L2. Going up needs three things, none of them tools: a trigger, a pass/fail criterion, and an exception exit.

Governance is four questions: who enables it, who is isolated from whom, who hears about overreach, and who signs off. The last one is the most skipped — **an assistant saying it is done does not make it done.**

Details: [`references/maturity.md`](./references/maturity.md).

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

## Output contracts

Fix what each step produces before you start. Checking against it afterwards is cheaper than rework.

| Step | Artifact | Hard requirement |
|---|---|---|
| 0 | Task card | All four questions answered, including what you will not do |
| 1 | Brief | Three columns, four rows max, every row traceable |
| 2 | Action list | Items start with a verb, owners never invented |
| 3 | Flow | Parallel work not drawn as sequential, review gates kept |
| 4 | Stats table | Categories sum to the total, formula written below |
| 5 | Deck outline | One conclusion per slide, titles are conclusions |
| 6 | Review record | Three sampled numbers, one definition, one conclusion, written down |

## Corpus

No blank page when you write a weekly, a monthly, minutes, an email, a proposal or a retrospective.

| File | Content |
|---|---|
| [`corpus/00-sources.md`](./references/corpus/00-sources.md) | Where every piece comes from, plus a checklist for judging any template |
| [`corpus/01-formats.md`](./references/corpus/01-formats.md) | Six document skeletons, each with acceptance tests and common mistakes |
| [`corpus/02-phrases.md`](./references/corpus/02-phrases.md) | Phrase bank by position: opening, progress, results, problems, plans, closing — plus banned words and weak-to-strong rewrites |
| [`corpus/03-samples.md`](./references/corpus/03-samples.md) | Six full samples: ops weekly, project monthly, meeting minutes, cross-team email, one-page proposal, GRAI retrospective |
| [`corpus/04-real/`](./references/corpus/04-real/) | Real outputs: filing rules, template, redaction limits |
| [`corpus/05-walkthrough/`](./references/corpus/05-walkthrough/) | Three walkthroughs: monthly review, competitor brief, meeting minutes to actions (messy input), fictional data |

Use them by parts, not whole: copy the structure, rewrite the phrasing, replace every number.

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
| `references/mindset.md` | Five ways of thinking: first principles, adversarial review, ablation, Occam's razor, boundary check |
| `references/automation.md` | From human-driven to signal-driven: three trigger types, a rule table, one exit, settled decisions, periodic subtraction |
| `references/sharing.md` | Documenting it: eight sections, three formats, the first screen, upkeep |
| `references/why-and-how.md` | How others build pipelines: four schools and what they share |
| `references/steps-deep.md` | Per-step inputs, actions, output definition, checklist, common mistakes |
| `references/variants.md` | Six variants: three-step, weekly, retrospective, meeting, competitor, chat-only |
| `references/scenarios.md` | Client-facing material, cross-team output, adapting to an industry |
| `references/examples.md` | Three worked cases |
| `references/corpus/` | Corpus: sources, skeletons, phrases, samples, real-output rules, a walkthrough |
| `templates/` | Seven copy-paste prompt templates, plus an optional `pipeline-state.yaml` |
| `examples/` | Six HTML samples, usable as templates |

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

