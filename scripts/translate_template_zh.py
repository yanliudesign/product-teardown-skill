#!/usr/bin/env python3
"""Translate UI chrome in the ZH template to Chinese.
Only UI labels change — every {{PLACEHOLDER}} stays intact so the same fill script
can feed both templates.
"""
from pathlib import Path

ZH = Path("/Users/yanliu/personal/product teardown/templates/product-teardown-template-zh.html")
s = ZH.read_text(encoding="utf-8")

# (old, new) pairs. Order matters: longer strings first to avoid partial matches.
SUBS = [
    # <title>
    ('<title>Product Teardown · {{PRODUCT}} — Principal PM Analysis</title>',
     '<title>产品拆解 · {{PRODUCT}} — Principal PM 深度分析</title>'),

    # ARIA
    ('aria-label="Language"', 'aria-label="语言切换"'),
    ('aria-label="English version"', 'aria-label="英文版本"'),
    ('aria-label="中文版本">中文', 'aria-label="中文版本 · 当前">中文'),

    # Meta strip
    ('<span>Product Teardown Report</span>', '<span>产品拆解报告</span>'),
    ('<span>Principal PM · Systems Analysis</span>', '<span>Principal PM · 系统级分析</span>'),

    # Role row labels
    ('<div class="label">Category</div>', '<div class="label">品类</div>'),
    ('<div class="label">Users</div>',    '<div class="label">用户规模</div>'),
    ('<div class="label">Model</div>',    '<div class="label">商业模式</div>'),
    ('<div class="label">Stage</div>',    '<div class="label">阶段</div>'),

    # TOC
    ('<span class="kicker">Inside</span>', '<span class="kicker">目录</span>'),
    ('<li><a href="#tldr">Verdict · TL;DR</a></li>',                  '<li><a href="#tldr">核心结论 · TL;DR</a></li>'),
    ('<li><a href="#metrics">Key Signals</a></li>',                   '<li><a href="#metrics">关键信号</a></li>'),
    ('<li><a href="#s1">1. Product Snapshot</a></li>',                '<li><a href="#s1">1. 产品快照</a></li>'),
    ('<li><a href="#s2">2. Users & JTBD</a></li>',                    '<li><a href="#s2">2. 目标用户 & JTBD</a></li>'),
    ('<li><a href="#s3">3. Core Product Loop</a></li>',               '<li><a href="#s3">3. 核心产品循环</a></li>'),
    ('<li><a href="#s4">4. Architecture & UX System</a></li>',        '<li><a href="#s4">4. 架构 & 交互体系</a></li>'),
    ('<li><a href="#s5">5. Value Delivery & UX Quality</a></li>',     '<li><a href="#s5">5. 价值交付 & 体验质感</a></li>'),
    ('<li><a href="#s6">6. Business Model</a></li>',                  '<li><a href="#s6">6. 商业模式</a></li>'),
    ('<li><a href="#s7">7. Growth Strategy</a></li>',                 '<li><a href="#s7">7. 增长策略</a></li>'),
    ('<li><a href="#s8">8. AI / Future Readiness</a></li>',           '<li><a href="#s8">8. AI · 未来就绪度</a></li>'),
    ('<li><a href="#s9">9. Friction & Weaknesses</a></li>',           '<li><a href="#s9">9. 摩擦 & 短板</a></li>'),
    ('<li><a href="#s10">10. Opportunities & Redesign</a></li>',      '<li><a href="#s10">10. 机会 & 重设计</a></li>'),
    ('<li><a href="#s11">11. Final PM Verdict</a></li>',              '<li><a href="#s11">11. 终局判断</a></li>'),

    # Notice
    ('<strong>Assumptions:</strong>', '<strong>前提假设：</strong>'),

    # Verdict block
    ('<div class="kicker">Principal PM Verdict</div>', '<div class="kicker">Principal PM 判断</div>'),
    ('<div class="label">{{STAR_RATING_x}} / 5 · Strategic strength</div>',
     '<div class="label">{{STAR_RATING_x}} / 5 · 战略强度</div>'),

    # TLDR kicker
    ('<div class="kicker">If you only read three things —</div>',
     '<div class="kicker">如果你只看三件事 —</div>'),

    # Metric cards
    ('<div class="label">Time to Value</div>',        '<div class="label">价值到达时间</div>'),
    ('<div class="label">Core Loop Frequency</div>',  '<div class="label">核心循环频次</div>'),
    ('<div class="label">Moat Score (PM lens)</div>', '<div class="label">护城河评分（PM 视角）</div>'),

    # §1
    ('<h3>Product Snapshot</h3>',           '<h3>产品快照</h3>'),
    ('<span class="pill">What it really is</span>', '<span class="pill">它到底是什么</span>'),
    ('<p class="section-intro">Beyond the marketing description — what this product actually is as a system.</p>',
     '<p class="section-intro">抛开营销话术 — 把这个产品当成一个「系统」来看，它到底是什么。</p>'),
    ('<h4>Core user promise</h4>',         '<h4>核心用户承诺</h4>'),
    ('<h4>Category & positioning</h4>',    '<h4>品类 & 定位</h4>'),
    ('<h4 style="margin-top:14px;">Assumptions</h4>', '<h4 style="margin-top:14px;">前提假设</h4>'),

    # §2
    ('<h3>Target Users & Jobs-to-be-Done</h3>',      '<h3>目标用户 & Jobs-to-be-Done</h3>'),
    ('<span class="pill">Who + why</span>',          '<span class="pill">谁 + 为什么</span>'),
    ('<h4>Primary user segments</h4>',               '<h4>主要用户分层</h4>'),
    ('<h4>Trigger & context</h4>',                   '<h4>触发 & 场景</h4>'),
    ('<p><strong>Trigger moment:</strong>',          '<p><strong>触发时刻：</strong>'),
    ('<p><strong>Frequency:</strong>',               '<p><strong>使用频次：</strong>'),
    ('<p><strong>Context:</strong>',                 '<p><strong>使用场景：</strong>'),
    ('<h4>Jobs-to-be-Done</h4>',                     '<h4>Jobs-to-be-Done · 用户「雇佣」这个产品去做什么</h4>'),
    ('<div class="who">Functional</div>',            '<div class="who">功能层</div>'),
    ('<div class="who">Emotional</div>',             '<div class="who">情感层</div>'),
    ('<div class="who">Social</div>',                '<div class="who">社交层</div>'),
    ('"When ___, I want to ___, so I can ___."',     '"当 ___ 的时候，我想要 ___，这样我就能 ___。"'),
    ('"I want to feel ___ / avoid feeling ___."',    '"我想要感受到 ___ / 避免感受到 ___。"'),
    ('"I want others to see me as ___."',            '"我想要别人把我看成 ___。"'),

    # §3
    ('<h3>Core Product Loop</h3>',                                   '<h3>核心产品循环</h3>'),
    ('<span class="pill">System dynamics</span>',                    '<span class="pill">系统动力学</span>'),
    ('<p class="section-intro">The engine — how a single user session compounds into retention and, if lucky, growth.</p>',
     '<p class="section-intro">引擎 — 一次使用如何滚成留存，运气好还能滚成增长。</p>'),
    ('<div class="kicker">Trigger</div>', '<div class="kicker">触发 · Trigger</div>'),
    ('<div class="kicker">Action</div>',  '<div class="kicker">行动 · Action</div>'),
    ('<div class="kicker">Reward</div>',  '<div class="kicker">奖赏 · Reward</div>'),
    ('<div class="kicker">Return</div>',  '<div class="kicker">回访 · Return</div>'),
    ('<h4>Acquisition loop</h4>',            '<h4>获取循环</h4>'),
    ('<h4>Activation · Aha moment</h4>',     '<h4>激活 · Aha 时刻</h4>'),
    ('<h4>Retention drivers</h4>',           '<h4>留存驱动</h4>'),
    ('<h4>Virality / network effects</h4>',  '<h4>裂变 / 网络效应</h4>'),

    # §4
    ('<h3>Product Architecture & UX System</h3>',                          '<h3>产品架构 & 交互体系</h3>'),
    ('<span class="pill">Surfaces + entities</span>',                      '<span class="pill">界面 + 实体</span>'),
    ('margin:8px 0 10px;">Key product surfaces</h4>',                      'margin:8px 0 10px;">核心产品界面（Surfaces）</h4>'),
    ('margin:18px 0 10px;">Core entities · what the system is built around</h4>',
     'margin:18px 0 10px;">核心实体 · 整个系统绕着什么转</h4>'),
    ('<h4>IA logic</h4>',                                                  '<h4>信息架构逻辑</h4>'),
    ('<h4>Navigation & interaction model</h4>',                            '<h4>导航 & 交互模型</h4>'),

    # §5
    ('<h3>Value Delivery & UX Quality</h3>',                                                   '<h3>价值交付 & 体验质感</h3>'),
    ('<span class="pill">Feel of the product</span>',                                          '<span class="pill">产品的手感</span>'),
    ('<span class="lbl">Time-to-value</span>',   '<span class="lbl">价值到达速度</span>'),
    ('<span class="lbl">Cognitive load</span>',  '<span class="lbl">认知负荷</span>'),
    ('<span class="lbl">Delight density</span>', '<span class="lbl">惊喜密度</span>'),
    ('<span class="lbl">Trust signals</span>',   '<span class="lbl">信任信号</span>'),
    ('<span class="lbl">Struggle risk</span>',   '<span class="lbl">用户挣扎风险</span>'),
    ('<h4>Key delight moments</h4>',             '<h4>关键惊喜时刻</h4>'),
    ('<h4>Where users likely struggle</h4>',     '<h4>用户可能卡壳的地方</h4>'),

    # §6
    ('<h3>Business Model & Monetization</h3>',   '<h3>商业模式 & 变现</h3>'),
    ('<span class="pill">How it makes money</span>', '<span class="pill">怎么赚钱</span>'),
    ('<span class="tag">Revenue model</span>',              '<span class="tag">收入模型</span>'),
    ('<span class="tag">Free ↔ Paid boundary</span>',       '<span class="tag">免费 ↔ 付费 分水岭</span>'),
    ('<span class="tag">Monetization entry points</span>',  '<span class="tag">变现入口</span>'),
    ('<span class="tag">UX ↔ Monetization alignment</span>', '<span class="tag">体验 ↔ 变现 是否同向</span>'),

    # §7
    ('<h3>Growth Strategy</h3>',                     '<h3>增长策略</h3>'),
    ('<span class="pill">Explicit or inferred</span>', '<span class="pill">明牌或推断</span>'),
    ('<h4>Likely acquisition channels</h4>',         '<h4>主要获取渠道</h4>'),
    ('<h4>Primary growth loops</h4>',                '<h4>主要增长循环</h4>'),
    ('margin:20px 0 10px;">Expansion vectors</h4>',  'margin:20px 0 10px;">扩张向量</h4>'),
    ('<div class="growth-col"><h5>Horizontal</h5>',  '<div class="growth-col"><h5>横向</h5>'),
    ('<div class="growth-col"><h5>Vertical</h5>',    '<div class="growth-col"><h5>纵向</h5>'),
    ('<div class="growth-col"><h5>Platform</h5>',    '<div class="growth-col"><h5>平台</h5>'),

    # §8
    ('<h3>AI / Future Readiness</h3>',                                          '<h3>AI · 未来就绪度</h3>'),
    ('<span class="pill">Human ↔ AI task split</span>',                         '<span class="pill">人 ↔ AI 任务分工</span>'),
    ('<p class="section-intro">Where the product sits today on the AI-integration spectrum, and where the next 12–24 months push it.</p>',
     '<p class="section-intro">今天这个产品在 AI 整合光谱上的位置，以及未来 12–24 个月会被推向哪里。</p>'),
    ('<div class="lvl">Level 1</div><div class="name">Assistive</div>',
     '<div class="lvl">Level 1</div><div class="name">辅助 · Assistive</div>'),
    ('<div class="lvl">Level 2</div><div class="name">Embedded</div>',
     '<div class="lvl">Level 2</div><div class="name">嵌入 · Embedded</div>'),
    ('<div class="lvl">Level 3</div><div class="name">Autonomous / Agentic</div>',
     '<div class="lvl">Level 3</div><div class="name">自主 · Agentic</div>'),
    ('<h4>Current AI usage</h4>',                                    '<h4>当前 AI 使用状况</h4>'),
    ('<h4>What could become agentic in 12–24 months</h4>',           '<h4>12–24 个月内可 Agent 化的环节</h4>'),
    ('<h4>Deeper AI opportunities</h4>',                             '<h4>更深层 AI 机会</h4>'),
    ('<h4>Strategic AI-disruption risk</h4>',                        '<h4>被 AI 颠覆的战略风险</h4>'),

    # §9
    ('<h3>Friction & Weaknesses</h3>',                                                       '<h3>摩擦 & 短板</h3>'),
    ('<span class="pill">Critical PM lens</span>',                                           '<span class="pill">批判性 PM 视角</span>'),
    ('<p class="section-intro">Explicit and opinionated. Where the system leaks, breaks, or over-designs.</p>',
     '<p class="section-intro">直接、有观点。系统在哪里漏、哪里断、哪里过度设计。</p>'),
    ('<span class="sev">高 · High</span>',   '<span class="sev">高</span>'),
    ('<span class="sev">中 · Medium</span>', '<span class="sev">中</span>'),

    # §10
    ('<h3>Opportunities & Redesign Ideas</h3>',              '<h3>机会 & 重设计</h3>'),
    ('<span class="pill">Actionable PM thinking</span>',     '<span class="pill">可落地的 PM 思考</span>'),
    ('<div class="kicker">Improvement · 1</div>',            '<div class="kicker">改进 · 1</div>'),
    ('<div class="kicker">Improvement · 2</div>',            '<div class="kicker">改进 · 2</div>'),
    ('<div class="kicker">Improvement · 3</div>',            '<div class="kicker">改进 · 3</div>'),
    ('<div class="kicker">Strategic shift</div>',            '<div class="kicker">战略转向</div>'),
    ('<div class="kicker">🌙 Moonshot</div>',                '<div class="kicker">🌙 登月构想</div>'),

    # §11
    ('<h3>Final PM Verdict</h3>',                    '<h3>终局判断</h3>'),
    ('<span class="pill">Synthesis</span>',          '<span class="pill">综合判定</span>'),
    ('<h5>Why it wins</h5>',                         '<h5>为什么它赢</h5>'),
    ('<h5>Where it breaks</h5>',                     '<h5>在哪里断裂</h5>'),
    ('<h5>Long-term moat</h5>',                      '<h5>长期护城河</h5>'),

    # Footer
    ('<div class="brand-sub">Created by <strong>Dreameryanyan</strong> · Principal PM Product Teardown OS</div>',
     '<div class="brand-sub">Created by <strong>Dreameryanyan</strong> · Principal PM 产品拆解操作系统</div>'),
    ('<div class="sig">— Product Teardown · Principal PM Analysis</div>',
     '<div class="sig">— 产品拆解 · Principal PM 分析</div>'),
    ('Generated {{TIMESTAMP}} · Product: <strong>{{PRODUCT}}</strong> ·\n  Structured per the 11-section teardown framework (Snapshot → JTBD → Loop → Architecture → UX → Business → Growth → AI → Friction → Opportunities → Verdict).\n  Insight over description; systems over features. Assumptions marked inline — correct any and regenerate.',
     '生成于 {{TIMESTAMP}} · 产品：<strong>{{PRODUCT}}</strong> ·\n  按 11 节拆解框架构造（快照 → JTBD → 循环 → 架构 → 体验 → 商业 → 增长 → AI → 摩擦 → 机会 → 终局）。\n  洞察优先于描述，系统优先于功能。所有前提假设已在文中显式标注 — 有任何一条不对，告诉我重新生成。'),
]

missing = []
for old, new in SUBS:
    if old in s:
        s = s.replace(old, new, 1)
    else:
        missing.append(old[:80])

if missing:
    print("MISSING (skipped):")
    for m in missing:
        print(" ", m)
else:
    print(f"All {len(SUBS)} substitutions applied.")

ZH.write_text(s, encoding="utf-8")
print(f"Wrote: {ZH}")
