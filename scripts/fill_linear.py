#!/usr/bin/env python3
"""Fill both EN and ZH templates for the Linear teardown, cross-link the language buttons,
and open both files on the Desktop."""
import re
import subprocess
from pathlib import Path

SLUG = "linear"
YM = "202607"
DATE = "2026-07-01"

REPO = Path("/Users/yanliu/personal/product teardown")
TMPL_EN = REPO / "templates" / "product-teardown-template-en.html"
TMPL_ZH = REPO / "templates" / "product-teardown-template-zh.html"
OUT_DIR = Path.home() / "Desktop" / "Claude skills"

OUT_EN = OUT_DIR / f"product-teardown-{SLUG}-en-{YM}.html"
OUT_ZH = OUT_DIR / f"product-teardown-{SLUG}-zh-{YM}.html"

# Language switcher — buttons on both files point at the same pair of names
LANG = {"LANG_EN_HREF": OUT_EN.name, "LANG_ZH_HREF": OUT_ZH.name}

# Shared product screenshots (og:image assets from linear.app — canonical marketing shots)
SHOTS = {
    "SHOT_1_URL": "https://linear.app/static/og/homepage.jpg",
    "SHOT_2_URL": "https://linear.app/static/og/intake.jpg",
    "SHOT_3_URL": "https://linear.app/static/og/plan.jpg",
    "SHOT_4_URL": "https://linear.app/static/og/build.jpg",
    "SHOT_5_URL": "https://linear.app/static/og/diffs.png",
    "SHOT_6_URL": "https://linear.app/static/og/monitor.jpg",
}

# ---------- English content ----------
V_EN = {
    "PRODUCT": "Linear",
    "ONE_LINER_2_LINE_SUBTITLE": "An opinionated, keyboard-first issue tracker built as a taste-driven product OS for high-velocity software teams — Jira's spiritual replacement, engineered as craft, not configuration.",
    "DATE_YYYY_MM_DD": DATE,
    "TIMESTAMP": f"{DATE} · Principal PM Teardown",
    "CATEGORY": "Product-engineering OS / Issue tracker",
    "USER_SCALE": "[inferred] 10K+ paying teams; hundreds of thousands of seats",
    "BUSINESS_MODEL_SHORT": "Per-seat SaaS · Free / $14 / Enterprise",
    "STAGE_MATURITY": "Growth · Series C+ · Profitable [inferred]",
    "ASSUMPTIONS_ONE_PARAGRAPH_LIST_WHAT_IS_INFERRED_VS_KNOWN":
        "Product surface + pricing + Linear Method narrative are directly observable. Revenue / retention / seat count are [inferred] from public signals (funding rounds, founder interviews, developer surveys). AI feature depth reflects publicly shipped functionality as of mid-2026. Correct any assumption and I'll regenerate.",
    "VERDICT_ONE_LINER": "The best-designed tracker of its generation — but its next act is not more taste, it's becoming the substrate for AI agents.",
    "VERDICT_BODY_2_3_LINES":
        "Linear won by making craft the go-to-market: sub-second sync, keyboard-first flow, opinionated Linear Method. That moat is real but perishable — an AI-native tracker could turn issue tracking into 'just talk to the agent' and Linear's opinionated schema becomes a liability. The pivot to 'system of record for AI agents' is the whole game.",
    "STAR_ROW_e_g_★★★★☆": "★★★★☆",
    "STAR_RATING_x": "4.3",
    "TLDR_1_HEADLINE": "Craft is the growth engine",
    "TLDR_1_BODY": "Linear's PLG loop is not viral coefficient — it's founder/IC evangelism amplified by the Linear Method narrative. That's cheaper than paid acquisition and harder to copy than a feature.",
    "TLDR_2_HEADLINE": "Opinionation is moat and cage",
    "TLDR_2_BODY": "The refusal to be configurable is why engineers love it — and why non-eng teams and large orgs keep hitting a ceiling. Every horizontal expansion (Docs, marketing, ops) has been slower than Jira/Notion equivalents.",
    "TLDR_3_HEADLINE": "AI is a layer, not a rethink",
    "TLDR_3_BODY": "Current AI features (auto-title, similar-issue, Ask Linear) are additive polish. An AI-first competitor rebuilding issue tracking as an agent interface — no UI, just intent — is Linear's real strategic risk in 24 months.",
    "TTV_VALUE": "<1", "TTV_UNIT": "min",
    "TTV_NOTE_WHAT_HAPPENS_AT_AHA": "First ⌘K → issue filed → real-time sync visible to teammates. Fastest TTV in the category by a clear margin.",
    "LOOP_FREQ": "Many × day",
    "LOOP_FREQ_NOTE_TRIGGER_CONTEXT": "Triggered by Slack notifications, PRs, standups. Engineers loop 5–20× per workday; cycle rhythm re-locks weekly.",
    "MOAT_SCORE": "6.5",
    "MOAT_REASONING_ONE_LINE": "Brand + sync engine + workflow lock-in are strong today; none survive AI-native workflow disruption alone.",
    "SNAPSHOT_ONE_TO_TWO_SENTENCE_DEFINITION":
        "Linear is not an issue tracker — it's a curated operating system for product engineering that happens to use issues as its atomic unit.",
    "USER_PROMISE": "Your tool disappears. Every action is a keystroke, every state syncs instantly, every screen respects your time. You stay in flow; the org stays aligned.",
    "CATEGORY_POSITIONING_PARAGRAPH":
        "Sits between issue tracker (Jira, GitHub Issues) and project management (Asana, Basecamp), narrowly positioned as *the* tool for product engineering — deliberately not IT ops, not marketing, not 'any team.' The narrowness is the strategy: taste requires exclusion.",
    "ASSUMPTION_1": "Sweet-spot team size 5–500 engineers; larger orgs adopt team-by-team.",
    "ASSUMPTION_2": "PLG dominant motion; enterprise/sales overlay only above ~$50K ARR.",
    "SEGMENT_1_NAME": "Seed → Series C software startups",
    "SEGMENT_1_DETAIL": "Founders who refuse to install Jira. Dominant install base and largest advocacy source.",
    "SEGMENT_2_NAME": "Product-eng pods inside larger tech cos",
    "SEGMENT_2_DETAIL": "Vercel, OpenAI-stack cos, modern SaaS. Adopted team-by-team, often circumventing IT's Jira mandate.",
    "SEGMENT_3_NAME": "Senior ICs who dragged the team in",
    "SEGMENT_3_DETAIL": "The bottom-up entry vector — one engineer chooses Linear, then convinces the EM, then convinces the org.",
    "TRIGGER_MOMENT": "New team + tool decision; existing team's Jira frustration hits a breaking point; a returning engineer refuses to work in anything else.",
    "FREQUENCY": "Multiple × per workday for engineers; daily standup rhythm; weekly cycle/roadmap review.",
    "USAGE_CONTEXT": "Alt-tabbed against IDE, GitHub, Slack, Figma — Linear is a peer, not a destination. Command-K opens over any context in <100ms.",
    "JTBD_FUNCTIONAL": "\"When I'm interrupted mid-flow to file / find / update work, I want a tool that costs me <5 seconds — so I stay in the code.\"",
    "JTBD_EMOTIONAL": "\"I want to feel like a competent operator, not a Jira bureaucrat. I want the tool to reflect that our team is fast and thoughtful.\"",
    "JTBD_SOCIAL": "\"I want peers, founders, and hires to see that we care about craft — 'we use Linear' is shorthand for that.\"",
    "LOOP_TRIGGER_TITLE": "Notification arrives",
    "LOOP_TRIGGER_DETAIL": "Slack ping, GitHub PR, standup thread, teammate @mention — a piece of work needs your attention.",
    "LOOP_ACTION_TITLE": "⌘K → do the thing",
    "LOOP_ACTION_DETAIL": "Create, assign, label, status-shift, link. All keyboard, all sub-second, no context switch.",
    "LOOP_REWARD_TITLE": "Instant real-time sync",
    "LOOP_REWARD_DETAIL": "Board updates for the whole team; visible momentum; teammates react; cycle progress compounds.",
    "LOOP_RETURN_TITLE": "Cycle cadence re-locks",
    "LOOP_RETURN_DETAIL": "1–2 week cycles + project milestones + inbox force scheduled re-entry. You don't need discipline — the tool has rhythm.",
    "LOOP_ONE_LINE_INSIGHT_WHAT_THE_LOOP_ACTUALLY_TEACHES_THE_USER":
        "The loop teaches you that documenting work is not overhead — it's the same speed as doing the work.",
    "ACQUISITION_LOOP_DETAIL":
        "Founder/IC evangelism → free team trial → paid upgrade → new company forms → same evangelist reinstalls Linear (alumni loop). Amplified by Linear Method content + X/Twitter design tribe.",
    "AHA_MOMENT_DETAIL":
        "The first time you file an issue in <3 seconds with ⌘K and watch it sync live on a teammate's screen. Emotional beat: 'oh — this is what it should have been.'",
    "RETENTION_1": "Cycle rhythm — the tool has a heartbeat you can't get from Jira/Asana.",
    "RETENTION_2": "Integrations — GitHub, Slack, Figma make Linear the pointer to work everywhere else.",
    "RETENTION_3": "Roadmap lock-in — once the org's plan lives here, switching cost explodes.",
    "VIRALITY_DETAIL_OR_NONE":
        "Weak inside the product (no social layer). Strong outside — Linear Method, founder Twitter, 'Linear-quality' as a design meme. Cross-workspace links now seeding early cross-company network effects.",
    "SURFACE_1_NAME": "⌘K palette", "SURFACE_1_ROLE": "The verb layer. Any action, any object, any nav — no menus.",
    "SURFACE_2_NAME": "Inbox",       "SURFACE_2_ROLE": "Personal triage; the first surface most users hit each morning.",
    "SURFACE_3_NAME": "Cycles",      "SURFACE_3_ROLE": "1–2 week sprint container; the heartbeat of the tool.",
    "SURFACE_4_NAME": "Projects",    "SURFACE_4_ROLE": "Goal + milestones + issues; the container above cycles.",
    "SURFACE_5_NAME": "Roadmap / Initiatives", "SURFACE_5_ROLE": "Portfolio rollup for leadership; where projects ladder to strategy.",
    "SURFACE_6_NAME": "Views",       "SURFACE_6_ROLE": "Saved filters as first-class objects — any list can be a view.",
    "ENTITY_1": "Issue", "ENTITY_2": "Cycle", "ENTITY_3": "Project", "ENTITY_4": "Team", "ENTITY_5": "Roadmap / Initiative",
    "IA_LOGIC_PARAGRAPH":
        "Nouns are stable and live in the left nav (Team → Cycle → Project → Roadmap → Initiative). Verbs live in ⌘K. Filters are first-class; every list is a saved view. IA depth is deliberately shallow — Linear resists the 'settings sprawl' that killed Jira's UX.",
    "NAV_INTERACTION_PARAGRAPH":
        "Keyboard-first throughout: `C` create, `L` label, `S` status, ⌘K anything. Optimistic UI over a bespoke sync engine (a technical moat few competitors match). Modals are rare; slide-in drawers preserve list context.",
    "TTV_BAR": "92", "TTV_LABEL": "Very fast",
    "COG_BAR": "35", "COG_LABEL": "Low",
    "DELIGHT_BAR": "82", "DELIGHT_LABEL": "High",
    "TRUST_BAR": "88", "TRUST_LABEL": "High",
    "STRUGGLE_BAR": "40", "STRUGGLE_LABEL": "Low-Medium",
    "DELIGHT_1": "⌘K palette responsiveness — real-time sub-100ms feel.",
    "DELIGHT_2": "Keyboard-only issue creation and status transitions.",
    "DELIGHT_3": "The issue-detail typography and micro-motion — it feels *considered*.",
    "STRUGGLE_1": "Cross-team dependency modeling — still awkward for 5+ teams shipping one launch.",
    "STRUGGLE_2": "Non-engineering onboarding — marketing/ops feel the tool wasn't built for them.",
    "STRUGGLE_3": "Portfolio hierarchy (Roadmap/Initiative) feels bolted-on for orgs with 50+ projects.",
    "REVENUE_MODEL_NAME": "Per-seat SaaS · 4 tiers",
    "REVENUE_MODEL_DETAIL": "Free (small teams, capped) → Standard → Business (~$14/user/mo) → Enterprise (custom). Bulk of revenue [inferred] concentrated in Business and Enterprise.",
    "FREE_PAID_BOUNDARY_NAME": "Team maturity, not usage",
    "FREE_PAID_DETAIL": "Free supports small teams (≤2 teams, limited issues). Paid unlocks cycles, projects, roadmaps — the *rhythm* features that only matter once you're scaling.",
    "MON_ENTRY_HEADLINE": "The 'we've grown up' upgrade",
    "MON_ENTRY_DETAIL": "First paid trigger: 'we want real cycles and a roadmap.' Second: SSO/audit at Enterprise. Rarely a mid-flow paywall.",
    "UX_MON_HEADLINE": "Clean alignment",
    "UX_MON_DETAIL_ARE_THEY_ALIGNED_OR_IN_TENSION":
        "Paywalls hit at growth milestones (not mid-task) — the upgrade feels earned, not punitive. Rare in category. Only weak spot: 'AI features' as an upsell risks feeling gated at a time when users expect AI as default.",
    "CHANNEL_1": "Founder / senior-IC evangelism (dominant)",
    "CHANNEL_2": "Linear Method blog + weekly changelog + X/Twitter design tribe",
    "CHANNEL_3": "Integrations marketplace + GitHub/Slack surfaces (indirect billboard effect)",
    "GROWTH_LOOP_1_NAME": "PLG · IC → team upgrade",
    "GROWTH_LOOP_1_DETAIL": "One engineer trials → invites team → team hits paid feature → upgrade → new team standardizes.",
    "GROWTH_LOOP_2_NAME": "Alumni loop",
    "GROWTH_LOOP_2_DETAIL": "Engineers who used Linear at one company install it at the next — cheapest, hardest-to-copy acquisition channel in category.",
    "HORIZONTAL_1": "Docs (Notion-lite) inside Linear",
    "HORIZONTAL_2": "Customer Requests + Insights",
    "VERTICAL_1": "Eng leadership analytics (cycle health, throughput)",
    "VERTICAL_2": "PM workflows: spec → project → cycle → issue",
    "PLATFORM_1": "Public API + webhooks + integrations",
    "PLATFORM_2": "Sync engine as a substrate for third-party tools",
    "ACTIVE_IF_ASSISTIVE": "", "ACTIVE_IF_EMBEDDED": "active", "ACTIVE_IF_AUTONOMOUS": "",
    "CURRENT_AI_USAGE_PARAGRAPH":
        "Level ~1.5 — assistive tipping into embedded. Auto-title / description drafts, similar-issue detection, weekly project summaries, 'Ask Linear' natural-language query. All human-in-the-loop; nothing yet takes an autonomous action on your behalf.",
    "AGENTIC_CANDIDATE_1": "Inbox triage — assign owner, label, cycle, detect duplicates automatically.",
    "AGENTIC_CANDIDATE_2": "Cycle re-planning — agent shuffles issues based on PR velocity and blockers.",
    "AGENTIC_CANDIDATE_3": "Status roll-ups — agent watches GitHub + Slack and keeps issue state current with no human input.",
    "AI_OPPORTUNITY_1": "Spec-drafting agent — turns a Slack thread into a project + issues.",
    "AI_OPPORTUNITY_2": "Executive weekly narrative — auto-generated review doc grounded in real issue/PR data.",
    "AI_DISRUPTION_RISK":
        "High. A greenfield AI-native tracker could reframe issue tracking as 'talk to the agent, no UI needed.' Linear's opinionated schema becomes a liability if the primary interface stops being a UI. Existential unless Linear becomes the system of record *for AI agents*.",
    "FRICTION_1_TITLE": "Non-engineering teams are second-class citizens",
    "FRICTION_1_BODY_WHY_IT_MATTERS":
        "Marketing, ops, and design have workflows Linear doesn't model well. In practice, these teams end up on Notion or Asana, splitting the company's operating surface. Linear is losing the 'single company OS' battle it needs to win to justify a Notion-scale valuation.",
    "FRICTION_2_TITLE": "AI is a feature layer, not a product rethink",
    "FRICTION_2_BODY":
        "Current AI = auto-title, similar-issue, Ask Linear. Additive polish. An AI-first competitor rebuilding issue tracking as an agent interface (no UI, just intent) leapfrogs the entire product surface. Linear needs a category-redefining AI story, not features.",
    "FRICTION_3_TITLE": "Cross-team dependency modeling is weak",
    "FRICTION_3_BODY":
        "Initiatives helped, but the 'ten teams shipping toward one launch' case still requires spreadsheets and Slack. This is the #1 pain of scaled eng orgs — and the exact wedge a competitor could exploit.",
    "FRICTION_4_TITLE": "Enterprise governance lags Jira",
    "FRICTION_4_BODY":
        "Granular permissions, audit, custom-field-at-scale, sandboxes — all lighter than Jira. Puts a ceiling on penetration in banks / gov / healthcare and forces awkward workarounds in Fortune 500 rollouts.",
    "OPP_1_HEADLINE": "Agentic Triage Inbox",
    "OPP_1_DETAIL_WHAT_HOW_WHY":
        "Every new issue meets a Linear agent that proposes owner, cycle, labels, duplicates, and a first-draft spec. Human clicks ✓. Cuts PM overhead ~40% and turns triage from a chore into a review. Ships in 2 quarters; deepens moat by turning Linear into the *judgment layer*, not the input layer.",
    "OPP_2_HEADLINE": "Program primitive — model dependencies as a DAG",
    "OPP_2_DETAIL":
        "Introduce a real object between Project and Initiative that represents cross-team programs with typed dependencies. Auto-surface the critical path in the roadmap. Kills spreadsheets, unlocks the 200-eng-org buyer.",
    "OPP_3_HEADLINE": "Executive Cockpit view",
    "OPP_3_DETAIL":
        "Auto-generated weekly narrative (progress, risk, blockers) grounded in issue/PR data, delivered as a doc CEOs/CPOs actually read. Wins the org's operating surface from Notion by giving leadership a Linear-native reason to check in daily.",
    "STRATEGIC_HEADLINE": "Become the system of record for AI agents building software",
    "STRATEGIC_DETAIL_HIGH_IMPACT_BET":
        "Reposition Linear as an API-first substrate where AI coding agents file issues, close them, open PRs, and update roadmaps — not a UI for humans first. Every AI code tool becomes a Linear client. Moat shifts from UX taste (perishable) to network of agents (durable). This is the pivot that outruns AI disruption instead of being killed by it.",
    "MOONSHOT_HEADLINE": "Continuous Product Kernel",
    "MOONSHOT_DETAIL_WHY_IT_COULD_RESHAPE_THE_CATEGORY":
        "Linear absorbs Slack + docs + GitHub signals and continuously re-plans the roadmap in real time. Cycles become fluid, not fixed. The tool stops being a *tracker*; it becomes the *operating loop* — the equivalent of what Bloomberg is to a trader. Category-redefining if it works.",
    "FINAL_WINS":
        "Uncompromising taste + speed + narrative discipline. Craft *is* the go-to-market. A generation of founders installs Linear reflexively, and the alumni loop keeps compounding cheaper than any paid channel.",
    "FINAL_BREAKS":
        "Opinionation ceiling caps large-org and non-engineering expansion. AI features are additive, not a rethink. Cross-team dependencies still leak. Docs / horizontal plays feel fragile against Notion.",
    "FINAL_MOAT_OR_LACK_THEREOF":
        "Real but perishable — brand + sync engine + workflow lock-in. None of these survive AI-native workflow disruption alone. If Linear becomes the substrate for AI agents, moat is durable for a decade. If not, they are the next Jira in five years.",
    "SHOT_1_CAPTION": "Homepage hero — 'product development system for teams and agents.'",
    "SHOT_2_CAPTION": "Intake — conversations → routed, labeled, prioritized issues.",
    "SHOT_3_CAPTION": "Plan — initiatives, roadmap timeline, cross-team milestones.",
    "SHOT_4_CAPTION": "Build — native surface for Codex, Cursor, Copilot agents.",
    "SHOT_5_CAPTION": "Diffs — structural PR review inside Linear.",
    "SHOT_6_CAPTION": "Monitor — Pulse, insights, cycle-time by agent.",
}

# ---------- Chinese content ----------
V_ZH = {
    "PRODUCT": "Linear",
    "ONE_LINER_2_LINE_SUBTITLE": "一款有强烈观点、键盘优先的 issue tracker — 把「产品工程」当成主战场，用「品位」而不是「配置」去打赢 Jira 的下一代替代品。",
    "DATE_YYYY_MM_DD": DATE,
    "TIMESTAMP": f"{DATE} · Principal PM 深度拆解",
    "CATEGORY": "产品工程操作系统 / Issue tracker",
    "USER_SCALE": "[推断] 1 万+ 付费团队，数十万席位",
    "BUSINESS_MODEL_SHORT": "按席位订阅 · 免费 / $14 / Enterprise",
    "STAGE_MATURITY": "成长期 · Series C+ · 已盈利 [推断]",
    "ASSUMPTIONS_ONE_PARAGRAPH_LIST_WHAT_IS_INFERRED_VS_KNOWN":
        "产品界面、定价、Linear Method 叙事均可直接观察。营收 / 留存 / 席位数为 [推断]，依据是融资轮次、创始人访谈、开发者调研。AI 能力深度基于 2026 年中期已公开发布的功能。任一前提不对，告诉我重新生成。",
    "VERDICT_ONE_LINER": "这一代设计得最好的 tracker — 但下一幕的赢法不再是「更有品味」，而是变成 AI Agent 的底层记录系统。",
    "VERDICT_BODY_2_3_LINES":
        "Linear 靠「把品位做成 GTM」赢到今天：亚秒级同步、键盘优先、Linear Method 有观点。这道护城河真实但会过期 — 一个 AI 原生的 tracker 可以把「记 issue」重构成「跟 Agent 讲一句话」，Linear 高度确定的 schema 反而变成拖累。能不能转型成「AI Agent 的系统 of record」，是 Linear 未来五年唯一的题。",
    "STAR_ROW_e_g_★★★★☆": "★★★★☆",
    "STAR_RATING_x": "4.3",
    "TLDR_1_HEADLINE": "「品位」就是增长引擎",
    "TLDR_1_BODY": "Linear 的 PLG 循环不靠病毒系数 — 靠创始人 / 高级 IC 的自发传教，被 Linear Method 内容放大。这比付费投放便宜、比任何功能更难被抄。",
    "TLDR_2_HEADLINE": "「有观点」既是护城河也是天花板",
    "TLDR_2_BODY": "拒绝可配置化是工程师爱它的原因 — 也是它在非工程团队和大企业里反复撞墙的原因。所有横向扩张（Docs / 市场 / 运营）都比 Jira / Notion 走得慢。",
    "TLDR_3_HEADLINE": "AI 目前是「贴层」不是「重构」",
    "TLDR_3_BODY": "现在的 AI（自动标题、相似 issue、Ask Linear）是加法式抛光。一个 AI-first 的竞品把 tracker 重做成「跟 Agent 说话，没有 UI」— 这才是 Linear 未来 24 个月真正的战略风险。",
    "TTV_VALUE": "<1", "TTV_UNIT": "分钟",
    "TTV_NOTE_WHAT_HAPPENS_AT_AHA": "第一次 ⌘K → 提 issue → 实时同步给队友。品类里最快的 TTV，遥遥领先。",
    "LOOP_FREQ": "每天多次",
    "LOOP_FREQ_NOTE_TRIGGER_CONTEXT": "由 Slack 通知、PR、standup 触发。工程师每个工作日循环 5–20 次；周维度 cycle 节奏再次锁回。",
    "MOAT_SCORE": "6.5",
    "MOAT_REASONING_ONE_LINE": "品牌 + 同步引擎 + 工作流锁定今天很强；但没有一样能单独扛住 AI 原生工作流的颠覆。",
    "SNAPSHOT_ONE_TO_TWO_SENTENCE_DEFINITION":
        "Linear 不是 issue tracker — 它是一套精心策划的「产品工程操作系统」，只不过恰好用 issue 作为最小原子单位。",
    "USER_PROMISE": "工具消失。所有操作都是一个快捷键，所有状态实时同步，所有屏幕都尊重你的时间。你留在心流里，组织留在对齐里。",
    "CATEGORY_POSITIONING_PARAGRAPH":
        "介于 issue tracker（Jira、GitHub Issues）和项目管理（Asana、Basecamp）之间，被极窄地定位为「*产品工程团队*的工具」— 刻意不做 IT ops、不做 marketing、不做「任何团队都能用」。窄，就是策略：品位需要排他。",
    "ASSUMPTION_1": "甜蜜点团队规模 5–500 名工程师；更大的组织按团队逐步渗透。",
    "ASSUMPTION_2": "PLG 是主战术；只有 ARR 大约 5 万美金以上才叠销售。",
    "SEGMENT_1_NAME": "Seed → Series C 软件创业公司",
    "SEGMENT_1_DETAIL": "拒绝装 Jira 的创始人们。安装量最大、口碑输出最猛的一群。",
    "SEGMENT_2_NAME": "大厂里的产品工程小队",
    "SEGMENT_2_DETAIL": "Vercel、OpenAI 生态公司、现代 SaaS。按小队渗透，经常绕开 IT 部门要求用 Jira 的行政指令。",
    "SEGMENT_3_NAME": "拽着团队一起用的高级 IC",
    "SEGMENT_3_DETAIL": "自底向上的入口 — 一个工程师先自己用，说服 EM，最后说服整个组织。",
    "TRIGGER_MOMENT": "新团队做选型决策；老团队被 Jira 折磨到临界点；回流的工程师拒绝在任何别的东西上写 issue。",
    "FREQUENCY": "工程师每个工作日多次；每天 standup 节奏；每周 cycle / roadmap 复盘。",
    "USAGE_CONTEXT": "在 IDE、GitHub、Slack、Figma 之间 Alt-Tab — Linear 是「同侪」，不是「终点」。⌘K 在任何上下文上 100ms 内弹出。",
    "JTBD_FUNCTIONAL": "\"当我被打断去『记 / 找 / 改』一件工作的时候，我要一个只花我 <5 秒的工具 — 这样我可以马上回到代码里。\"",
    "JTBD_EMOTIONAL": "\"我想感觉自己是个有能力的操盘手，不是 Jira 里的官僚。我要工具反映出『我们团队又快又用心』。\"",
    "JTBD_SOCIAL": "\"我想让同侪、创始人和候选人一眼看出我们在乎 craft — 『我们用 Linear』就是这句话的简写。\"",
    "LOOP_TRIGGER_TITLE": "通知来了",
    "LOOP_TRIGGER_DETAIL": "Slack 提到、GitHub PR、standup 里的 @、队友抛过来的问题 — 有一件事需要你处理。",
    "LOOP_ACTION_TITLE": "⌘K → 一键搞定",
    "LOOP_ACTION_DETAIL": "新建、指派、打标签、切状态、加链接。全键盘、亚秒级、不切上下文。",
    "LOOP_REWARD_TITLE": "实时同步的即时反馈",
    "LOOP_REWARD_DETAIL": "全组 board 立刻更新；能看见推进感；队友有反应；cycle 进度肉眼可见地积累。",
    "LOOP_RETURN_TITLE": "Cycle 节奏把你拽回来",
    "LOOP_RETURN_DETAIL": "1–2 周 cycle + 项目里程碑 + Inbox 会强制你按节奏回来。你不需要自律 — 工具本身有心跳。",
    "LOOP_ONE_LINE_INSIGHT_WHAT_THE_LOOP_ACTUALLY_TEACHES_THE_USER":
        "这个循环真正在教你的是：「记录工作」不是额外成本 — 它和「做工作」一样快。",
    "ACQUISITION_LOOP_DETAIL":
        "创始人 / IC 传教 → 团队免费试用 → 付费升级 → 新公司组建 → 同一批传教士再次带来 Linear（校友循环）。Linear Method 内容 + X / Twitter 上的设计圈在放大这个循环。",
    "AHA_MOMENT_DETAIL":
        "你第一次用 ⌘K 在 3 秒内提完一个 issue，然后看到它在队友屏幕上实时出现。情绪节点：「哦 — 这才是它本来应该有的样子。」",
    "RETENTION_1": "Cycle 节奏 — 工具自带心跳，Jira/Asana 给不了。",
    "RETENTION_2": "集成 — GitHub、Slack、Figma 让 Linear 成为「所有工作的指针」。",
    "RETENTION_3": "Roadmap 锁定 — 一旦组织的路线图长在这里，切换成本瞬间爆炸。",
    "VIRALITY_DETAIL_OR_NONE":
        "产品内很弱（没有社交层）。产品外很强 — Linear Method、创始人 Twitter、「Linear-quality」已经是设计圈的迷因。跨 workspace 链接正在孕育早期的跨公司网络效应。",
    "SURFACE_1_NAME": "⌘K 命令面板", "SURFACE_1_ROLE": "动词层。任何操作、任何对象、任何跳转 — 无需菜单。",
    "SURFACE_2_NAME": "Inbox",       "SURFACE_2_ROLE": "个人分诊台；大多数用户每天早晨第一个打开的界面。",
    "SURFACE_3_NAME": "Cycles",      "SURFACE_3_ROLE": "1–2 周的 sprint 容器；工具的心跳。",
    "SURFACE_4_NAME": "Projects",    "SURFACE_4_ROLE": "目标 + 里程碑 + issue；cycle 之上的容器。",
    "SURFACE_5_NAME": "Roadmap / Initiatives", "SURFACE_5_ROLE": "面向管理层的组合视图；项目上升为战略的地方。",
    "SURFACE_6_NAME": "Views",       "SURFACE_6_ROLE": "把「保存的过滤器」变成一等公民 — 任何列表都能变成一个 View。",
    "ENTITY_1": "Issue", "ENTITY_2": "Cycle", "ENTITY_3": "Project", "ENTITY_4": "Team", "ENTITY_5": "Roadmap / Initiative",
    "IA_LOGIC_PARAGRAPH":
        "名词稳定，住在左侧导航（Team → Cycle → Project → Roadmap → Initiative）。动词住在 ⌘K 里。Filter 是一等公民；任何列表都可以保存成 View。信息架构故意做得浅 — Linear 抵抗那种「设置无限膨胀」的形态（正是那种形态杀死了 Jira 的体验）。",
    "NAV_INTERACTION_PARAGRAPH":
        "全流程键盘优先：`C` 新建、`L` 打标签、`S` 切状态、⌘K 干任何事。乐观 UI 建在自研同步引擎之上（少数竞品能做到的技术护城河）。极少弹模态；侧滑抽屉保留列表上下文。",
    "TTV_BAR": "92", "TTV_LABEL": "极快",
    "COG_BAR": "35", "COG_LABEL": "低",
    "DELIGHT_BAR": "82", "DELIGHT_LABEL": "高",
    "TRUST_BAR": "88", "TRUST_LABEL": "高",
    "STRUGGLE_BAR": "40", "STRUGGLE_LABEL": "中低",
    "DELIGHT_1": "⌘K 面板的响应速度 — 100ms 以内的实时手感。",
    "DELIGHT_2": "纯键盘完成 issue 新建和状态切换。",
    "DELIGHT_3": "Issue 详情页的字体和微动效 — 能感觉出「有人认真想过」。",
    "STRUGGLE_1": "跨团队依赖建模 — 5 个以上团队一起发一版的场景仍然别扭。",
    "STRUGGLE_2": "非工程团队的上手 — 市场 / 运营会明显感觉到「这工具不是为我做的」。",
    "STRUGGLE_3": "组合层级（Roadmap / Initiative）对于 50+ 项目的组织有点「贴上去」的感觉。",
    "REVENUE_MODEL_NAME": "按席位订阅 · 4 档",
    "REVENUE_MODEL_DETAIL": "免费（小团队、有配额）→ Standard → Business（~$14/user/月）→ Enterprise（自定义）。[推断] 收入主要集中在 Business 和 Enterprise。",
    "FREE_PAID_BOUNDARY_NAME": "按「团队成熟度」而不是按使用量",
    "FREE_PAID_DETAIL": "免费版支持小团队（≤2 teams，issue 数上限）。付费才解锁 cycles、projects、roadmaps — 这些「节奏层」的功能只有你规模化以后才用得上。",
    "MON_ENTRY_HEADLINE": "「我们长大了」升级点",
    "MON_ENTRY_DETAIL": "第一次付费触发：「我们要真正的 cycle 和 roadmap」。第二次：SSO / 审计 进 Enterprise。极少中途撞收费墙。",
    "UX_MON_HEADLINE": "干净对齐",
    "UX_MON_DETAIL_ARE_THEY_ALIGNED_OR_IN_TENSION":
        "付费墙落在增长里程碑上（不是任务中途）— 升级感觉是「挣来的」，不是被罚。品类里少见的干净对齐。唯一隐忧：把 AI 能力做成 upsell，在用户已经默认「AI 是标配」的时代，容易让人不爽。",
    "CHANNEL_1": "创始人 / 高级 IC 的自发传教（主渠道）",
    "CHANNEL_2": "Linear Method 博客 + 每周 changelog + X / Twitter 设计圈",
    "CHANNEL_3": "集成市场 + GitHub / Slack 界面的间接品牌曝光",
    "GROWTH_LOOP_1_NAME": "PLG · IC → 团队升级",
    "GROWTH_LOOP_1_DETAIL": "一个工程师试用 → 拉队友 → 团队撞到付费功能 → 升级 → 新团队标准化。",
    "GROWTH_LOOP_2_NAME": "校友循环",
    "GROWTH_LOOP_2_DETAIL": "在一家公司用过 Linear 的工程师，去下一家继续装 — 品类里最便宜、最难被复制的获客渠道。",
    "HORIZONTAL_1": "Linear 内嵌的 Docs（类 Notion）",
    "HORIZONTAL_2": "Customer Requests + Insights",
    "VERTICAL_1": "工程管理层分析（cycle 健康度、吞吐量）",
    "VERTICAL_2": "PM 工作流：spec → project → cycle → issue",
    "PLATFORM_1": "公开 API + Webhook + 集成生态",
    "PLATFORM_2": "同步引擎作为第三方工具的底层",
    "ACTIVE_IF_ASSISTIVE": "", "ACTIVE_IF_EMBEDDED": "active", "ACTIVE_IF_AUTONOMOUS": "",
    "CURRENT_AI_USAGE_PARAGRAPH":
        "水平大约在 1.5 — 从「辅助」向「嵌入」过渡。自动标题 / 描述、相似 issue 检测、每周项目总结、Ask Linear 自然语言查询。全部人在环内；还没有任何环节由 AI 自主替你行动。",
    "AGENTIC_CANDIDATE_1": "Inbox 分诊 — 自动指派 owner、打标签、放 cycle、检测重复。",
    "AGENTIC_CANDIDATE_2": "Cycle 重新规划 — Agent 根据 PR 速度和阻塞情况自动挪 issue。",
    "AGENTIC_CANDIDATE_3": "状态汇总 — Agent 监听 GitHub + Slack，全程无人干预地把 issue 状态保持最新。",
    "AI_OPPORTUNITY_1": "起稿 Agent — 把一条 Slack 讨论直接变成 project + issue 集合。",
    "AI_OPPORTUNITY_2": "高层周报叙事 — 基于真实 issue / PR 数据自动生成、CEO / CPO 真正会读的文档。",
    "AI_DISRUPTION_RISK":
        "高。一个全新的 AI 原生 tracker 可以把 issue 管理重构成「跟 Agent 说一句话，不需要 UI」。Linear 强观点的 schema 一旦不再是主要交互界面，反而成为拖累。除非 Linear 变成「*AI Agent* 的系统 of record」，否则是生死题。",
    "FRICTION_1_TITLE": "非工程团队被当二等公民",
    "FRICTION_1_BODY_WHY_IT_MATTERS":
        "市场、运营、设计的工作流 Linear 建模得不好。实际结果是这些团队跑去 Notion / Asana，把公司「一套操作系统」的战场拆成两半。Linear 正在输掉「公司统一 OS」这一战 — 而这一战不赢，就撑不起 Notion 那个级别的估值。",
    "FRICTION_2_TITLE": "AI 是功能贴层，不是产品重构",
    "FRICTION_2_BODY":
        "现在的 AI = 自动标题、相似 issue、Ask Linear。加法式抛光。一个 AI-first 竞品把 issue 管理重构成「Agent 界面」（没有 UI，只有意图）就直接绕开整个产品面。Linear 需要一个「重新定义品类」的 AI 故事，不是几个功能。",
    "FRICTION_3_TITLE": "跨团队依赖建模仍然弱",
    "FRICTION_3_BODY":
        "Initiatives 有所改善，但「10 个团队一起发一版」的场景仍需要 spreadsheet + Slack 兜底。这是规模化工程组织的第 1 号痛点 — 也正是竞品最能切入的一刀。",
    "FRICTION_4_TITLE": "企业级治理落后于 Jira",
    "FRICTION_4_BODY":
        "细粒度权限、审计、大规模自定义字段、sandbox — 都比 Jira 轻。这在银行 / 政府 / 医疗行业形成天花板，也在 Fortune 500 部署里逼出各种别扭的绕路方案。",
    "OPP_1_HEADLINE": "Agent 化的分诊 Inbox",
    "OPP_1_DETAIL_WHAT_HOW_WHY":
        "每一个新 issue 先经过一个 Linear Agent，它自动建议 owner、cycle、标签、重复项、以及一段草稿 spec。人只需要点 ✓。PM 分诊工作量减 40%，triage 从「杂活」变成「审核」。2 个季度内可出；深化护城河的方式是把 Linear 从「输入层」升级为「判断层」。",
    "OPP_2_HEADLINE": "Program 新原语 — 把依赖建模成 DAG",
    "OPP_2_DETAIL":
        "在 Project 和 Initiative 之间引入一个真正的对象，用带类型的依赖关系表示跨团队 program，在 roadmap 上自动高亮关键路径。杀死 spreadsheet 用法，打开 200 人工程组织这个买家。",
    "OPP_3_HEADLINE": "Executive Cockpit 视图",
    "OPP_3_DETAIL":
        "基于 issue / PR 数据自动生成的每周叙事（进展 / 风险 / 阻塞），以「CEO / CPO 真的愿意读」的文档形态呈现。给管理层一个 Linear 原生的每天必看理由，把「组织日常操作面」从 Notion 手里抢回来。",
    "STRATEGIC_HEADLINE": "把 Linear 重新定位成「AI Agent 造软件」的系统 of record",
    "STRATEGIC_DETAIL_HIGH_IMPACT_BET":
        "Linear 不再是人类用的 UI 优先工具，而是一个 API-first 的底层 — AI 编码 Agent 在这里开 issue、关 issue、开 PR、更新 roadmap。每一个 AI 编程工具都成为 Linear 的客户端。护城河从「UX 品位（会过期）」升级为「Agent 网络（能持久）」。这是唯一能跑赢 AI 颠覆而不是被 AI 颠覆的转向。",
    "MOONSHOT_HEADLINE": "持续产品内核（Continuous Product Kernel）",
    "MOONSHOT_DETAIL_WHY_IT_COULD_RESHAPE_THE_CATEGORY":
        "Linear 吸收 Slack + docs + GitHub 的所有信号，实时地重规划 roadmap。Cycle 变成流动的，不再是固定的。工具不再是「记录器」；它变成一台「操作循环机」— 对应产品经理，就像彭博终端对应交易员。如果做成，就是重新定义品类。",
    "FINAL_WINS":
        "不妥协的品位 + 速度 + 叙事纪律。「Craft 本身就是 GTM」— 一整代创始人把 Linear 当成默认选择。校友循环持续复利，比任何付费渠道都便宜。",
    "FINAL_BREAKS":
        "「有观点」这道天花板压住了大企业和非工程团队的扩张。AI 目前是加法不是重构。跨团队依赖建模仍然漏。Docs / 横向扩张在 Notion 面前显得脆弱。",
    "FINAL_MOAT_OR_LACK_THEREOF":
        "真实但会过期 — 品牌 + 同步引擎 + 工作流锁定，没有任何一样能单独扛住 AI 原生工作流的颠覆。如果 Linear 拿下「AI Agent 底层」这一转向，护城河可持续十年；如果没有，它五年后就是下一个 Jira。",    "SHOT_1_CAPTION": "官网 Hero — 「面向团队 + Agent 的产品开发系统」。",
    "SHOT_2_CAPTION": "Intake — 对话与反馈 → 自动派发、打标、定优先级。",
    "SHOT_3_CAPTION": "Plan — initiatives、roadmap 时间轴、跨团队里程碑。",
    "SHOT_4_CAPTION": "Build — 为 Codex / Cursor / Copilot Agent 原生搭建的工作面。",
    "SHOT_5_CAPTION": "Diffs — 在 Linear 内部直接看结构化 PR 代码变更。",
    "SHOT_6_CAPTION": "Monitor — Pulse 周报、Insights、按 Agent 拆分的 cycle time。",}


def render(template_path: Path, values: dict, active_lang: str) -> str:
    html = template_path.read_text(encoding="utf-8")
    v = dict(values)
    v.update(SHOTS)
    v["LANG_EN_HREF"] = LANG["LANG_EN_HREF"]
    v["LANG_ZH_HREF"] = LANG["LANG_ZH_HREF"]
    v["ACTIVE_IF_EN"] = "active" if active_lang == "en" else ""
    v["ACTIVE_IF_ZH"] = "active" if active_lang == "zh" else ""

    for key in sorted(v, key=len, reverse=True):
        html = html.replace("{{" + key + "}}", v[key])

    remaining = [m for m in re.findall(r"\{\{[A-Z0-9_★☆_e_g_x]+\}\}", html) if m != "{{PLACEHOLDER}}"]
    if remaining:
        print(f"  UNRESOLVED in {template_path.name}:")
        for r in sorted(set(remaining)):
            print("   ", r)
    return html


OUT_DIR.mkdir(parents=True, exist_ok=True)

for target, tmpl, values, lang in [
    (OUT_EN, TMPL_EN, V_EN, "en"),
    (OUT_ZH, TMPL_ZH, V_ZH, "zh"),
]:
    html = render(tmpl, values, lang)
    for kw in ("Dreameryanyan", "brand-mark", "yanliudreamer", "xiaohongshu"):
        assert kw in html, f"BRAND KEYWORD MISSING in {target.name}: {kw}"
    target.write_text(html, encoding="utf-8")
    print(f"Wrote: {target}")

# Delete the stale single-language file if it exists
old = OUT_DIR / f"product-teardown-{SLUG}-{YM}.html"
if old.exists():
    old.unlink()
    print(f"Removed stale: {old}")

subprocess.run(["open", str(OUT_EN)])
print("Opened EN. Click 中文 in the bottom-right to switch.")
