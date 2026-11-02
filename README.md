<div align="center">

**中文** · [English](./README.en.md)

# office-ai-workflow

#### 把五个高频办公任务串成一条流水线

[![Version](https://img.shields.io/badge/version-1.1.0-green.svg)](SKILL.md)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-Standard-8B5CF6.svg)](https://agentskills.io)
[![Dependencies](https://img.shields.io/badge/dependencies-0-brightgreen.svg)](#兼容性)
[![Platform](https://img.shields.io/badge/platform-WorkBuddy%20%C2%B7%20CodeBuddy%20%C2%B7%20TRAE%20%C2%B7%20Qoder%20%C2%B7%20Claude%20Code-orange.svg)](#安装)

</div>

<p align="center">
  <img src="./assets/cover.svg" width="100%" alt="office-ai-workflow：五个工位串成一条流水线">
</p>

---

> 查资料、读文件、理流程、做表格、写汇报，五件事单看都不难，串起来才省时间。
> 上一步的产出是下一步的原料，人只核对关键数字和最终结论。

一个 Skill，一条五步流水线。不依赖脚本、不联网、不装任何包，把文件夹丢进 AI 的技能目录就能用。

## 解决什么问题

单点用 AI 做办公任务，常见三个毛病：

| 毛病 | 后果 |
|---|---|
| 问完就关窗口 | 下次重新交代背景，调好的格式和说法全丢 |
| 每次重新描述需求 | 任务模糊、资料零散，结果时好时坏 |
| 中间产物不留存 | 拼汇报时材料还是散的，数字口径对不上 |

流水线把顺序和交接固定下来：查到的资料接着用来读文件，读出的要点进清单，清单和数字最后落进汇报。方法固定，每次只换输入。

## 五步

<p align="center">
  <img src="./assets/pipeline.svg" width="100%" alt="五步与交接物：查资料→信息简报、读文件→行动清单、理流程→流程图、做表格→统计表、写汇报→初稿，最后人工复核">
</p>

| 步 | 做什么 | 交出什么 |
|---|---|---|
| 一 | 查资料：限定主题与时间范围，整理成一页简报 | 信息简报（信息点 / 来源 / 与工作关系） |
| 二 | 读文件：长文档按五要素提取，不复述全文 | 行动清单（事项 / 负责人 / 时间 / 依据） |
| 三 | 理流程：把复杂事情画成流程图或职责图 | 流程图（含人工审核节点） |
| 四 | 做表格：统一口径再汇总，写明计算方式 | 统计表（带计算过程，可复核） |
| 五 | 写汇报：五页骨架，每页一个结论 | PPT 初稿（交人工复核） |

五步不必每次全走。缺哪步跳哪步，但已走步骤的顺序不乱、交接物不省。

## 30 秒上手

把这句话发给 AI：

```
用 office-ai-workflow，帮我把这几个文件整理成本月复盘。
重点是客户反馈和进度卡点，输出简报 + 行动清单 + 统计表 + PPT 大纲，
数字必须保留原始依据，不要臆造。
```

它会把五步拆开做，每步停下来给你过检查清单，再进下一步。

## 安装

### 一条命令

```bash
git clone https://github.com/YardonYan/office-ai-workflow.git
cd office-ai-workflow
node tools/install.mjs --list          # 看本机能装到哪些应用
node tools/install.mjs --ai all        # 一次装到全部
```

零依赖，只用 Node 标准库。支持 `--dry-run` 预览、`--force` 覆盖、`--uninstall` 卸载、`--project` 装进当前项目、`--dir` 装到自定义目录。

### 手动放

把整个仓库目录拷到对应位置，保证 `<技能目录>/office-ai-workflow/SKILL.md` 这个层级存在。

| 应用 | 全局目录 | 项目目录 |
|---|---|---|
| WorkBuddy | `~/.workbuddy/skills/` | `.workbuddy/skills/` |
| CodeBuddy | `~/.codebuddy/skills/` | `.codebuddy/skills/` |
| TRAE 国内版 | `~/.trae-cn/skills/` | `.trae-cn/skills/` |
| TRAE 国际版 | `~/.trae/skills/` | `.trae/skills/` |
| Qoder 国内版 | `~/.qoder-cn/skills/` | `.qoder/skills/` |
| Qoder 国际版 | `~/.qoder/skills/` | `.qoder/skills/` |
| Qwen Code | `~/.qwen/skills/` | `.qwen/skills/` |
| 通义灵码 | `~/.lingma/skills/` | `.lingma/skills/` |
| Kimi Code CLI | `~/.kimi/skills/` | `.kimi/skills/` |
| iFlow CLI | `~/.iflow/skills/` | `.iflow/skills/` |
| OpenClaw | `~/.openclaw/skills/` | `.openclaw/skills/` |
| 华为 CodeArts Doer | `~/.codeartsdoer/skills/` | — |
| Claude Code | `~/.claude/skills/` | `.claude/skills/` |
| Codex CLI | `~/.codex/skills/` | `.codex/skills/` |
| Cursor | `~/.cursor/skills/` | `.cursor/skills/` |
| 通用约定 | `~/.agents/skills/` | `.agents/skills/` |

国内工具排前面。装完重启应用，或在应用里执行一次刷新。

## 使用途径

| 途径 | 怎么做 | 适合 |
|---|---|---|
| 安装器 | `node tools/install.mjs --ai <id>` | 本机长期使用，一条命令覆盖多个应用 |
| 手动拷贝 | 拷目录到上表位置 | 只用一两个应用，不想跑命令 |
| 项目内 | 放进项目的 `.codebuddy/skills/` 等目录，随仓库提交 | 团队共用，换机器自动带上 |
| 插件市场 | 见 `.claude-plugin/` 与 `.codebuddy-plugin/` 的清单 | 支持插件市场的应用，一次装好 |

不适用：网页版 IDE（CodeSandbox、StackBlitz）和云 Shell。技能是给 AI 读的指令文件，这些环境没有加载入口。

## 内含

主册给顺序和原则，细节在四个分册里，按需读，不占平时上下文。

| 文件 | 内容 |
|---|---|
| `SKILL.md` | 主册：三条机制、全景图、开工四件事、五步要点、检查点、失败处理 |
| `references/why-and-how.md` | 别人怎么搭流水线：提示词链、数字员工、任务编排、模板加变量四种流派，以及拆分过头与一步到位的判断 |
| `references/steps-deep.md` | 五步各自的输入、动作、产物定义、检查项、常见错误、失败处理 |
| `references/variants.md` | 六种变体：三步精简、周报专线、月度复盘、会议专线、竞品简报、纯对话版 |
| `references/scenarios.md` | 三类延伸：面向客户的材料、跨部门协作出品、把五步换成本行业流程 |
| `references/examples.md` | 三个完整案例，带真实的输入输出与卡点处理 |
| `templates/` | 六份可直接复制的提示词模板 |
| `CONTRIBUTING.md` | 想贡献模板时先看这个 |

## 模板

`templates/` 下六份，复制就能用。每份含输入说明、提示词原文、输出契约、验收清单、失败处理。

| 模板 | 用在什么时候 |
|---|---|
| [`01-brief.md`](./templates/01-brief.md) | 要把零散信息收成一页简报 |
| [`02-extract.md`](./templates/02-extract.md) | 要从长文档里拿出行动清单 |
| [`03-map.md`](./templates/03-map.md) | 要把一件多环节的事画成图 |
| [`04-stats.md`](./templates/04-stats.md) | 要把台账变成能进汇报的统计 |
| [`05-report.md`](./templates/05-report.md) | 材料齐了，要出汇报大纲 |
| [`06-weekly.md`](./templates/06-weekly.md) | 每周固定交周报，走三步精简版 |

## 输出契约

每一步的产物长什么样，事先写死。写完对着核，比事后返工便宜。

| 步 | 产物 | 硬性要求 |
|---|---|---|
| 一 | 信息简报 | 三列，最多四行，每行可溯源 |
| 二 | 行动清单 | 事项是动词开头，负责人不臆造 |
| 三 | 流程图 | 并行不画成串行，审核节点不省 |
| 四 | 统计表 | 分类合计等于总数，公式写在表下 |
| 五 | 汇报大纲 | 每页一个结论，标题是结论句 |

## 什么时候用 / 不用

| 用 | 不用 |
|---|---|
| 每月固定要交的复盘 | 一次性的临时问答 |
| 跨部门联合出品的材料 | 只有自己看的工作笔记 |
| 需要留档、需要复用的产出 | 结论已定、只差一句话的事 |
| 材料散在多个文件里 | 材料本身还没准备好 |

判断标准一条：这件事下个月还会再做一遍吗。会，值得建流程；不会，做完算数。

## 为什么值得做成流水线

这套东西值得复用的不是某一次生成，是固定的输入、处理和检查套路。下次只换四样：

1. 新的源文件
2. 新的时间范围
3. 新的统计口径
4. 新的汇报主题

不能省的四样：来源与依据、人工检查、数据复核、敏感信息处理。

## 硬性底线

1. AI 负责整理和起草；关键数字、原始依据和最终结论必须人工核对后才能对外使用。
2. 保留原始依据，不臆造数据、不补造负责人和日期；字段缺失明确标注，不猜。
3. 每步的检查清单过完才进下一步；不过关就修，不跳闸。
4. 涉及敏感信息先脱敏再进流水线。

## 兼容性

按 [Agent Skills](https://agentskills.io) 开放标准组织：一个目录、一个 `SKILL.md`、YAML frontmatter 只含规范允许的字段。凡是支持该标准的工具都能直接加载，不需要转换。

技能本身不依赖任何脚本、网络和第三方包。`tools/` 下两个脚本只用于安装和生成插件清单，删掉不影响技能工作。

## 相关

- 配套技能：[slides-workflow](https://github.com/YardonYan/for-my-self-skills)（把大纲做成成稿 PPT）
- 技能合集：[for-my-self-skills](https://github.com/YardonYan/for-my-self-skills)

## 许可

[Apache-2.0](./LICENSE)，版权行 `Copyright 2026 YardonYan`。

