#!/usr/bin/env python3
"""生成 README 与个人主页共用的封面图，以及五步流程图。

  assets/cover.svg     900x336  五个工位串在一条传送带上
  assets/pipeline.svg  900x260  五步与交接物的横向流程

用法: python tools/gen_assets.py
"""

from __future__ import annotations

import pathlib

W, H = 900, 336
SANS = ("PingFang SC, Microsoft YaHei, Noto Sans SC, system-ui, "
        "sans-serif")
MONO = "JetBrains Mono, SF Mono, Menlo, Consolas, monospace"

# 暖灰纸底 + 墨绿主色 + 陶土强调
BG = "#F7F5F0"
INK = "#1F2328"
MUTED = "#6B675E"
FAINT = "#A39E93"
GREEN = "#2F5D50"
GREEN_L = "#E4EDE9"
CLAY = "#B4592F"
LINE = "#DED9CE"


def t(x, y, body, size, fill, *, weight=400, font=SANS, anchor=None,
      spacing=None, italic=False):
    a = [f'x="{x}"', f'y="{y}"']
    if anchor:
        a.append(f'text-anchor="{anchor}"')
    a.append(f'font-family="{font}"')
    a.append(f'font-size="{size}"')
    if weight != 400:
        a.append(f'font-weight="{weight}"')
    if spacing:
        a.append(f'letter-spacing="{spacing}"')
    if italic:
        a.append('font-style="italic"')
    a.append(f'fill="{fill}"')
    return f'<text {" ".join(a)}>{body}</text>'


def icon(idx: int, cx: float, cy: float) -> str:
    """七个工位的小图标，统一 22x22 以内。"""
    def a(w=1.5, op=None):
        base = f'stroke="{GREEN}" stroke-width="{w}" fill="none" stroke-linecap="round"'
        if op:
            base += f' stroke-opacity="{op}"'
        return base

    if idx == 0:
        return (f'<rect x="{cx - 10}" y="{cy - 10}" width="20" height="20" rx="3" {a()}/>'
                f'<path d="M{cx - 5} {cy} l3.5 3.5 l6.5 -7" {a()}/>')
    if idx == 1:
        return (f'<circle cx="{cx - 2}" cy="{cy - 2}" r="7.5" {a()}/>'
                f'<line x1="{cx + 4}" y1="{cy + 4}" x2="{cx + 10}" y2="{cy + 10}" {a()}/>')
    if idx == 2:
        return (f'<rect x="{cx - 8}" y="{cy - 11}" width="16" height="22" rx="2" {a()}/>'
                f'<line x1="{cx - 4}" y1="{cy - 4}" x2="{cx + 4}" y2="{cy - 4}" {a(1.2, ".55")}/>'
                f'<line x1="{cx - 4}" y1="{cy + 1}" x2="{cx + 4}" y2="{cy + 1}" {a(1.2, ".55")}/>'
                f'<line x1="{cx - 4}" y1="{cy + 6}" x2="{cx + 1}" y2="{cy + 6}" {a(1.2, ".55")}/>')
    if idx == 3:
        return (f'<rect x="{cx - 11}" y="{cy - 10}" width="9" height="7" rx="1.5" {a()}/>'
                f'<rect x="{cx + 2}" y="{cy + 3}" width="9" height="7" rx="1.5" {a()}/>'
                f'<path d="M{cx - 6} {cy - 3} V{cy} H{cx + 6} V{cy + 3}" {a(1.3)}/>')
    if idx == 4:
        return (f'<rect x="{cx - 10}" y="{cy - 9}" width="20" height="18" rx="2" {a()}/>'
                f'<line x1="{cx - 10}" y1="{cy - 3}" x2="{cx + 10}" y2="{cy - 3}" {a(1.2)}/>'
                f'<line x1="{cx - 3}" y1="{cy - 9}" x2="{cx - 3}" y2="{cy + 9}" {a(1.2)}/>')
    if idx == 5:
        return (f'<rect x="{cx - 10}" y="{cy - 9}" width="20" height="18" rx="2" {a()}/>'
                f'<path d="M{cx - 6} {cy + 4} l5 -6 l4 4 l5 -7" {a(1.5)}/>')
    return (f'<path d="M{cx - 9} {cy} l4.5 5 l8 -10" {a(1.8)}/>'
            f'<line x1="{cx - 10}" y1="{cy + 8}" x2="{cx + 10}" y2="{cy + 8}" {a(1.2, ".5")}/>')


def cover() -> str:
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
         f'viewBox="0 0 {W} {H}" role="img" aria-label="office-ai-workflow">',
         f'<rect width="{W}" height="{H}" fill="{BG}"/>']

    # 标题区
    s.append(t(60, 62, "office-ai-workflow", 25, INK, weight=600))
    s.append(t(60, 90, "五步办公流水线：从零散资料到一页汇报", 14, MUTED))
    s.append(t(60, 110, "Five office tasks, chained into one pipeline",
               10.5, FAINT))

    # 右上角：一条细线 + 标签
    s.append(f'<line x1="620" y1="46" x2="840" y2="46" stroke="{LINE}" '
             f'stroke-width="1"/>')
    s.append(t(840, 40, "AGENT SKILL · APACHE-2.0", 9, FAINT, font=MONO,
               anchor="end", spacing=1))

    steps = [
        ("01", "查资料", "简报", "search"),
        ("02", "读文件", "清单", "doc"),
        ("03", "理流程", "流程图", "flow"),
        ("04", "做表格", "统计表", "table"),
        ("05", "写汇报", "初稿", "deck"),
    ]

    bw, bh, gap = 130, 116, 22
    total = len(steps) * bw + (len(steps) - 1) * gap
    x0 = (W - total) / 2
    top = 152

    # 传送带
    s.append(f'<rect x="{x0 - 26}" y="{top + bh - 6}" width="{total + 52}" '
             f'height="3" rx="1.5" fill="{LINE}"/>')

    for i, (num, name, out, icon) in enumerate(steps):
        x = x0 + i * (bw + gap)
        # 工位
        s.append(f'<rect x="{x}" y="{top}" width="{bw}" height="{bh}" rx="7" '
                 f'fill="#FFFFFF" stroke="{LINE}" stroke-width="1.2"/>')
        # 顶部色条
        s.append(f'<rect x="{x}" y="{top}" width="{bw}" height="4" rx="2" '
                 f'fill="{GREEN}" fill-opacity="{0.35 + i * 0.12:.2f}"/>')
        s.append(t(x + 14, top + 26, num, 9.5, FAINT, font=MONO,
                   spacing=1.2))
        s.append(t(x + 14, top + 46, name, 14, INK, weight=600))

        cx, cy = x + bw / 2, top + 74
        if icon == "search":
            s.append(f'<circle cx="{cx - 3}" cy="{cy - 2}" r="9" fill="none" '
                     f'stroke="{GREEN}" stroke-width="1.8"/>')
            s.append(f'<line x1="{cx + 4}" y1="{cy + 5}" x2="{cx + 11}" '
                     f'y2="{cy + 12}" stroke="{GREEN}" stroke-width="1.8" '
                     f'stroke-linecap="round"/>')
        elif icon == "doc":
            s.append(f'<rect x="{cx - 10}" y="{cy - 13}" width="20" '
                     f'height="26" rx="2" fill="none" stroke="{GREEN}" '
                     f'stroke-width="1.6"/>')
            for k in range(3):
                s.append(f'<line x1="{cx - 5}" y1="{cy - 6 + k * 7}" '
                         f'x2="{cx + 5}" y2="{cy - 6 + k * 7}" '
                         f'stroke="{GREEN}" stroke-width="1.3" '
                         f'stroke-opacity=".55"/>')
        elif icon == "flow":
            s.append(f'<rect x="{cx - 13}" y="{cy - 14}" width="12" '
                     f'height="9" rx="1.5" fill="none" stroke="{GREEN}" '
                     f'stroke-width="1.5"/>')
            s.append(f'<rect x="{cx + 1}" y="{cy + 5}" width="12" height="9" '
                     f'rx="1.5" fill="none" stroke="{GREEN}" '
                     f'stroke-width="1.5"/>')
            s.append(f'<path d="M{cx - 7} {cy - 5} V{cy} H{cx + 7} V{cy + 5}" '
                     f'fill="none" stroke="{GREEN}" stroke-width="1.4"/>')
        elif icon == "table":
            s.append(f'<rect x="{cx - 12}" y="{cy - 11}" width="24" '
                     f'height="22" rx="2" fill="none" stroke="{GREEN}" '
                     f'stroke-width="1.5"/>')
            s.append(f'<line x1="{cx - 12}" y1="{cy - 4}" x2="{cx + 12}" '
                     f'y2="{cy - 4}" stroke="{GREEN}" stroke-width="1.3" '
                     f'stroke-opacity=".6"/>')
            s.append(f'<line x1="{cx - 4}" y1="{cy - 11}" x2="{cx - 4}" '
                     f'y2="{cy + 11}" stroke="{GREEN}" stroke-width="1.3" '
                     f'stroke-opacity=".6"/>')
        else:
            s.append(f'<rect x="{cx - 13}" y="{cy - 11}" width="26" '
                     f'height="20" rx="2" fill="none" stroke="{GREEN}" '
                     f'stroke-width="1.5"/>')
            s.append(f'<path d="M{cx - 8} {cy + 4} l6 -8 l5 5 l6 -9" '
                     f'fill="none" stroke="{GREEN}" stroke-width="1.6" '
                     f'stroke-linecap="round" stroke-linejoin="round"/>')

        # 产物标签
        s.append(t(x + bw / 2, top + bh + 26, out, 10.5, CLAY,
                   anchor="middle"))

        # 箭头
        if i < len(steps) - 1:
            ax = x + bw + gap / 2
            s.append(f'<path d="M{ax - 5} {top + 55} h8 m-3 -3 l3 3 l-3 3" '
                     f'fill="none" stroke="{FAINT}" stroke-width="1.3" '
                     f'stroke-linecap="round" stroke-linejoin="round"/>')

    # 底部说明
    s.append(t(60, 318, "上一步的产出是下一步的原料。人只在两端：开头交代四件事，结尾核对数字与结论。",
               10.5, FAINT))
    s.append("</svg>")
    return "\n".join(s)


def pipeline() -> str:
    w, h = 900, 236
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
         f'viewBox="0 0 {w} {h}" role="img" aria-label="五步流水线与交接物">',
         f'<rect width="{w}" height="{h}" fill="#FFFFFF"/>']

    s.append(t(40, 38, "五步与交接物", 15, INK, weight=600))
    s.append(t(40, 58, "每一步都留下实体产物，下一步拿它当原料", 10.5, MUTED))

    steps = [("查资料", "信息简报"), ("读文件", "行动清单"),
             ("理流程", "流程图"), ("做表格", "统计表"), ("写汇报", "初稿")]
    bw, gap, y = 118, 30, 96
    review_w = 96
    total = len(steps) * bw + review_w + gap * len(steps)
    x0 = (w - total) / 2

    for i, (name, out) in enumerate(steps):
        x = x0 + i * (bw + gap)
        s.append(f'<rect x="{x}" y="{y}" width="{bw}" height="44" rx="6" '
                 f'fill="{GREEN_L}" stroke="{GREEN}" stroke-width="1"/>')
        s.append(t(x + bw / 2, y + 27, name, 12, GREEN, weight=600,
                   anchor="middle"))
        s.append(f'<line x1="{x + bw / 2}" y1="{y + 44}" x2="{x + bw / 2}" '
                 f'y2="{y + 62}" stroke="{CLAY}" stroke-width="1.2" '
                 f'stroke-dasharray="3 3"/>')
        s.append(f'<rect x="{x + 12}" y="{y + 62}" width="{bw - 24}" '
                 f'height="24" rx="4" fill="#FFFFFF" stroke="{CLAY}" '
                 f'stroke-width="1" stroke-opacity=".5"/>')
        s.append(t(x + bw / 2, y + 78, out, 9.5, CLAY, anchor="middle"))

        ax = x + bw + gap / 2
        s.append(f'<path d="M{ax - 7} {y + 22} h14 m-4 -4 l4 4 l-4 4" '
                 f'fill="none" stroke="{FAINT}" stroke-width="1.4" '
                 f'stroke-linecap="round" stroke-linejoin="round"/>')

    # 人工复核
    rx = x0 + len(steps) * (bw + gap)
    s.append(f'<rect x="{rx}" y="{y}" width="{review_w}" height="44" rx="6" '
             f'fill="#FFFFFF" stroke="{FAINT}" stroke-width="1" '
             f'stroke-dasharray="4 3"/>')
    s.append(t(rx + review_w / 2, y + 27, "人工复核", 11.5, MUTED,
               anchor="middle"))

    s.append(t(40, 208, "缺哪步跳哪步，但已走步骤的顺序不乱、交接物不省。",
               10.5, FAINT))
    s.append("</svg>")
    return "\n".join(s)


def cover() -> str:
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
         f'viewBox="0 0 {W} {H}" role="img" aria-label="office-ai-workflow">',
         f'<rect width="{W}" height="{H}" fill="{BG}"/>']

    s.append(t(60, 58, "office-ai-workflow", 24, INK, weight=600))
    s.append(t(60, 84, "办公工作流的设计与实现", 13.5, MUTED))
    s.append(t(60, 103, "Design a pipeline, then run it", 10, FAINT))
    s.append(f'<line x1="620" y1="46" x2="840" y2="46" stroke="{LINE}" '
             f'stroke-width="1"/>')
    s.append(t(840, 40, "AGENT SKILL · APACHE-2.0", 9, FAINT, font=MONO,
               anchor="end", spacing=1))

    steps = [
        ("0", "定义", "任务卡"),
        ("1", "查资料", "简报"),
        ("2", "读文件", "清单"),
        ("3", "理流程", "流程图"),
        ("4", "做表格", "统计表"),
        ("5", "写汇报", "初稿"),
        ("6", "复核", "核对记录"),
    ]

    bw, bh, gap = 104, 108, 16
    total = len(steps) * bw + (len(steps) - 1) * gap
    x0 = (W - total) / 2
    top = 158

    s.append(f'<rect x="{x0 - 22}" y="{top + bh - 5}" width="{total + 44}" '
             f'height="3" rx="1.5" fill="{LINE}"/>')

    for i, (num, name, out) in enumerate(steps):
        x = x0 + i * (bw + gap)
        s.append(f'<rect x="{x}" y="{top}" width="{bw}" height="{bh}" rx="6" '
                 f'fill="#FFFFFF" stroke="{LINE}" stroke-width="1.2"/>')
        s.append(f'<rect x="{x}" y="{top}" width="{bw}" height="3.5" rx="1.75" '
                 f'fill="{GREEN}" fill-opacity="{0.3 + i * 0.1:.2f}"/>')
        s.append(t(x + 12, top + 24, num, 9, FAINT, font=MONO, spacing=1.2))
        s.append(t(x + 12, top + 43, name, 13, INK, weight=600))
        s.append(icon(i, x + bw / 2, top + 76))

        s.append(t(x + bw / 2, top + bh + 24, out, 10, CLAY, anchor="middle"))

        if i < len(steps) - 1:
            ax = x + bw + gap / 2
            s.append(f'<path d="M{ax - 4} {top + 52} h7 m-3 -2.6 l3 2.6 l-3 2.6" '
                     f'fill="none" stroke="{FAINT}" stroke-width="1.2" '
                     f'stroke-linecap="round" stroke-linejoin="round"/>')

    s.append(t(60, 316, "两端是定义与复核，中间五步是主体。上一步的产出是下一步的原料。",
               10.5, FAINT))
    s.append("</svg>")
    return "\n".join(s)


def pipeline() -> str:
    w, h = 900, 212
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
         f'viewBox="0 0 {w} {h}" role="img" aria-label="七步与交接物">',
         f'<rect width="{w}" height="{h}" fill="#FFFFFF"/>']
    s.append(t(40, 36, "七步与交接物", 15, INK, weight=600))
    s.append(t(40, 56, "每一步都留下实体产物，下一步拿它当原料", 10.5, MUTED))

    steps = [("定义", "任务卡"), ("查资料", "信息简报"), ("读文件", "行动清单"),
             ("理流程", "流程图"), ("做表格", "统计表"), ("写汇报", "初稿"),
             ("复核", "核对记录")]
    bw, gap, y = 100, 20, 94
    total = len(steps) * bw + (len(steps) - 1) * gap
    x0 = (w - total) / 2

    for i, (name, out) in enumerate(steps):
        x = x0 + i * (bw + gap)
        s.append(f'<rect x="{x}" y="{y}" width="{bw}" height="42" rx="6" '
                 f'fill="{GREEN_L}" stroke="{GREEN}" stroke-width="1"/>')
        s.append(t(x + bw / 2, y + 26, name, 11.5, GREEN, weight=600,
                   anchor="middle"))
        s.append(f'<line x1="{x + bw / 2}" y1="{y + 42}" x2="{x + bw / 2}" '
                 f'y2="{y + 60}" stroke="{CLAY}" stroke-width="1.2" '
                 f'stroke-dasharray="3 3"/>')
        s.append(f'<rect x="{x + 8}" y="{y + 60}" width="{bw - 16}" '
                 f'height="22" rx="4" fill="#FFFFFF" stroke="{CLAY}" '
                 f'stroke-width="1" stroke-opacity=".5"/>')
        s.append(t(x + bw / 2, y + 75, out, 9, CLAY, anchor="middle"))

        if i < len(steps) - 1:
            ax = x + bw + gap / 2
            s.append(f'<path d="M{ax - 6} {y + 21} h12 m-4 -3.4 l4 3.4 l-4 3.4" '
                     f'fill="none" stroke="{FAINT}" stroke-width="1.3" '
                     f'stroke-linecap="round" stroke-linejoin="round"/>')

    s.append(t(40, 206, "缺哪步跳哪步，但已走步骤的顺序不乱、交接物不省。",
               10.5, FAINT))
    s.append("</svg>")
    return "\n".join(s)


def main() -> int:
    out = pathlib.Path(__file__).resolve().parent.parent / "assets"
    out.mkdir(parents=True, exist_ok=True)
    for name, fn in (("cover.svg", cover), ("pipeline.svg", pipeline)):
        p = out / name
        p.write_text(fn(), encoding="utf-8", newline="\n")
        print(f"{p}  {p.stat().st_size} 字节")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
