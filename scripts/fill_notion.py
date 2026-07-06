#!/usr/bin/env python3
"""Fill both EN and ZH templates for the Notion teardown, cross-link the language buttons,
and open both files on the Desktop."""
import re
import subprocess
from pathlib import Path

SLUG = "notion"
YM = "202607"
DATE = "2026-07-05"

REPO = Path("/Users/yanliu/personal/product teardown")
TMPL_EN = REPO / "templates" / "product-teardown-template-en.html"
TMPL_ZH = REPO / "templates" / "product-teardown-template-zh.html"
OUT_DIR = Path.home() / "Desktop" / "Claude skills"

OUT_EN = OUT_DIR / f"product-teardown-{SLUG}-en-{YM}.html"
OUT_ZH = OUT_DIR / f"product-teardown-{SLUG}-zh-{YM}.html"

LANG = {"LANG_EN_HREF": OUT_EN.name, "LANG_ZH_HREF": OUT_ZH.name}

# Real hot-linkable product marketing screenshots (ctfassets.net — Notion's CDN).
SHOTS = {
    "SHOT_1_URL": "https://images.ctfassets.net/spoqsaf9291f/2kZsh7GLDkeSbS09zeNDpt/72e31019ad1ade3524748408b22cdeb0/ai-hero-image.png",
    "SHOT_2_URL": "https://images.ctfassets.net/spoqsaf9291f/1lM3knSXmvknnVQTvixGdt/6e41434ff3036aff202504ed0280d3c5/Agents.png",
    "SHOT_3_URL": "https://images.ctfassets.net/spoqsaf9291f/2O5v6DjzJSm6lVutlHr0pp/bd820f57ef274bc30b1bc7bf5e7bb326/docs-hero-2.png",
    "SHOT_4_URL": "https://images.ctfassets.net/spoqsaf9291f/4Z1732pchOu8VGaYGjQLqA/9d6c07b1e0dcdf3036422a49ab902f8b/project-hero.png",
    "SHOT_5_URL": "https://images.ctfassets.net/spoqsaf9291f/1HzgXZ0VGXdYgIE8zaIdAc/6a603e79668e8057526a15303430a6c5/meeting-notes-hero.png",
    "SHOT_6_URL": "https://images.ctfassets.net/spoqsaf9291f/5i2CEYkqUC1OmgrjaqUpIy/036820c5e6b8fcf8fdc0b253b5b0db00/mail_macOS.png",
}

# ---------- English content ----------
V_EN = {
    "PRODUCT": "Notion",
    "ONE_LINER_2_LINE_SUBTITLE": "A block-based workspace pretending to be a doc — really a soft database + programmable canvas that absorbs wiki, docs, tasks, and now AI agents into a single company operating system.",
    "DATE_YYYY_MM_DD": DATE,
    "TIMESTAMP": f"{DATE} · Principal PM Teardown",
    "CATEGORY": "Company OS · docs + DB + AI workspace",
    "USER_SCALE": "[inferred] 100M+ registered users, ~10M paid seats across 100K+ paying orgs",
    "BUSINESS_MODEL_SHORT": "Per-seat SaaS · Free / $10 / $18 / Enterprise · AI add-on",
    "STAGE_MATURITY": "Late-growth · post Series C · pre-IPO · [inferred] cash-flow positive",
    "ASSUMPTIONS_ONE_PARAGRAPH_LIST_WHAT_IS_INFERRED_VS_KNOWN":
        "Product surface, pricing, and public product launches (AI, Calendar, Mail, Agents, Enterprise Search) are directly observable. Seat counts, ARR mix, retention, and AI attach rate are [inferred] from funding, press, and public dev-tool surveys. AI depth reflects features shipped through mid-2026 (Notion 3 / agents). Correct any assumption and I'll regenerate.",
    "VERDICT_ONE_LINER": "The best-designed workspace of its generation — and the only one credibly repositioning from 'a place your team writes' to 'the substrate your team's agents run on.'",
    "VERDICT_BODY_2_3_LINES":
        "Notion won by turning docs into a soft database — the block model let one primitive absorb wiki, tasks, tables, and now AI outputs. That flexibility is the moat and the ceiling: teams love it, but structure discipline is on them. The 2026 pivot to Notion Agents plus Enterprise Search is the real bet: become the org's memory + labor layer before Google/Microsoft/Atlassian close the window.",
    "STAR_ROW_e_g_★★★★☆": "★★★★☆",
    "STAR_RATING_x": "4.4",
    "TLDR_1_HEADLINE": "The block model is the moat",
    "TLDR_1_BODY": "One primitive — the block — lets Notion be a doc, a wiki, a DB, a kanban, and now an agent surface. Competitors have to pick a shape; Notion refuses to. That's what makes horizontal expansion (Calendar, Mail, Sites, AI) feel native instead of bolted-on.",
    "TLDR_2_HEADLINE": "Flexibility is also the ceiling",
    "TLDR_2_BODY": "A blank page is freedom for power users and paralysis for everyone else. 'My Notion is a mess' is a real, structural churn driver — and the exact wedge Coda, ClickUp, and now Notion's own AI templates keep attacking.",
    "TLDR_3_HEADLINE": "Notion 3 / Agents is the whole game",
    "TLDR_3_BODY": "AI-native competitors could reframe workspaces as 'talk to the agent, no pages needed.' Notion's response — agents that write, query, and act *inside* the workspace with the org's real context — is either their durable second act or an OpenAI-shaped extinction event within 24 months.",
    "TTV_VALUE": "~2", "TTV_UNIT": "min",
    "TTV_NOTE_WHAT_HAPPENS_AT_AHA": "First slash command → block appears → drop a database → realize you just built an app. Aha is 'this is a tool, not a doc.'",
    "LOOP_FREQ": "Multiple × day",
    "LOOP_FREQ_NOTE_TRIGGER_CONTEXT": "Meeting notes, project pages, personal task list, Slack link-outs. Individuals loop 5–15×/day; teams re-lock weekly on planning + review docs.",
    "MOAT_SCORE": "7.0",
    "MOAT_REASONING_ONE_LINE": "Block model + workspace lock-in + brand + emerging AI context graph = strong today; only the last one survives an AI-native workflow shift.",
    "SNAPSHOT_ONE_TO_TWO_SENTENCE_DEFINITION":
        "Notion is not a doc editor — it's a programmable block canvas layered over a soft relational database, sold as 'the workspace' because that's the shape most teams need first.",
    "USER_PROMISE": "Everything your team writes, tracks, or looks up lives in one place — flexible enough to shape to any workflow, structured enough that AI can reason across all of it.",
    "CATEGORY_POSITIONING_PARAGRAPH":
        "Sits at the intersection of docs (Google Docs, Confluence), wiki (Confluence, Slab), lightweight PM (Asana, Trello), and lightweight DB (Airtable, Coda). Deliberately positioned as *the* company OS — not a tool, an org's operating surface. The category is 'workspace,' and Notion has done the most to define what that word now means.",
    "ASSUMPTION_1": "PLG-first; enterprise motion is real but downstream of team-level adoption.",
    "ASSUMPTION_2": "AI attach rate is the leading indicator leadership actually tracks internally.",
    "SEGMENT_1_NAME": "Startups & modern SaaS teams",
    "SEGMENT_1_DETAIL": "10–500 people, YC-adjacent, refuse Confluence. Dominant install base and strongest advocacy source.",
    "SEGMENT_2_NAME": "Cross-functional pods inside larger cos",
    "SEGMENT_2_DETAIL": "Marketing, ops, PM teams inside F500s who need a shared surface faster than IT can approve one. Adopted team-by-team.",
    "SEGMENT_3_NAME": "Individuals & creators (Notion-as-life-OS)",
    "SEGMENT_3_DETAIL": "The template economy — personal wikis, second brains, freelancer stacks. Small revenue, massive top-of-funnel and brand moat.",
    "TRIGGER_MOMENT": "New team spinning up; 'our Google Drive is chaos'; a returning PM/EM refuses to work in Confluence; someone in the org sees a beautiful Notion template on Twitter/X.",
    "FREQUENCY": "Multiple × per workday for ICs; daily for PMs/EMs writing meeting notes and project briefs; weekly for exec review + roadmap rituals.",
    "USAGE_CONTEXT": "Alt-tabbed against Slack, Figma, Linear, Google Meet. Notion is the reference layer — the place everyone links to when they need 'the source of truth.'",
    "JTBD_FUNCTIONAL": "\"When I need to capture, structure, or find something my team needs, I want one place that shapes to the task instead of forcing me into someone else's template.\"",
    "JTBD_EMOTIONAL": "\"I want to feel organized and in control — like my team runs on a real system, not a pile of Slack threads and Google Docs.\"",
    "JTBD_SOCIAL": "\"I want my team, candidates, and investors to see we're a modern, thoughtful org — a well-shaped Notion is shorthand for that.\"",
    "LOOP_TRIGGER_TITLE": "A moment of information friction",
    "LOOP_TRIGGER_DETAIL": "Meeting starts, project kicks off, teammate asks 'where's the doc?', an idea needs a home right now.",
    "LOOP_ACTION_TITLE": "/ → block → structure",
    "LOOP_ACTION_DETAIL": "Slash command spawns the right block (page, DB, callout, toggle). Structure emerges under the writer's hands with no config screen.",
    "LOOP_REWARD_TITLE": "Instant shareable artifact",
    "LOOP_REWARD_DETAIL": "One URL replaces a Slack thread + Google Doc + Airtable table. Feels like you *built* something in the time it takes to write.",
    "LOOP_RETURN_TITLE": "The page becomes the ritual",
    "LOOP_RETURN_DETAIL": "Weekly 1:1s, project trackers, on-call rotations — pages become the org's rhythm. You return not because Notion asks, but because the meeting starts.",
    "LOOP_ONE_LINE_INSIGHT_WHAT_THE_LOOP_ACTUALLY_TEACHES_THE_USER":
        "The loop teaches you that 'writing it down' and 'building the tool' are the same act — you don't graduate from docs to software; docs are software.",
    "ACQUISITION_LOOP_DETAIL":
        "Individual → team invite (bottom-up) + creator/template economy → SEO on 'notion template for X' + Twitter/X design tribe → Enterprise upgrade once org standardizes. Alumni loop: leavers install Notion at the next company.",
    "AHA_MOMENT_DETAIL":
        "First time you turn a page into a database view, then a kanban of the same data, then embed it inside another page — the block model clicks and you realize you have a low-code tool, not a text editor.",
    "RETENTION_1": "Workspace lock-in — everything you've built is here; export is legal but painful.",
    "RETENTION_2": "Team ritual gravity — weekly reviews, 1:1s, project pages become the calendar's shape.",
    "RETENTION_3": "AI grounded in your workspace — the more you use Notion, the more useful Notion AI becomes; classic data compounding loop.",
    "VIRALITY_DETAIL_OR_NONE":
        "In-product: guest links + public share pages seed cross-org discovery. Out-of-product: creator/template economy on YouTube, TikTok, X — arguably the strongest content-driven virality in productivity SaaS since Dropbox.",
    "SURFACE_1_NAME": "Page / block canvas", "SURFACE_1_ROLE": "The atomic unit — every doc, DB, view, embed lives here.",
    "SURFACE_2_NAME": "Sidebar (Teamspaces)", "SURFACE_2_ROLE": "The nav + IA layer; where org shape becomes visible.",
    "SURFACE_3_NAME": "Databases + Views",   "SURFACE_3_ROLE": "The soft-DB layer that turns pages into apps (table, board, calendar, timeline).",
    "SURFACE_4_NAME": "Notion AI panel",     "SURFACE_4_ROLE": "Write, summarize, ask across the workspace — in-context, not a chat app on the side.",
    "SURFACE_5_NAME": "Agents / Notion 3",   "SURFACE_5_ROLE": "Autonomous workers that ingest signal (Slack, Gmail, Linear), write pages, update DBs, and take multi-step actions.",
    "SURFACE_6_NAME": "Calendar + Mail",     "SURFACE_6_ROLE": "Adjacent surfaces feeding the same graph; time + inbox now inside the workspace.",
    "ENTITY_1": "Block", "ENTITY_2": "Page", "ENTITY_3": "Database + View", "ENTITY_4": "Teamspace", "ENTITY_5": "Agent",
    "IA_LOGIC_PARAGRAPH":
        "IA is deliberately soft: pages nest recursively, teamspaces group them, databases relate them. There is no global schema — structure emerges per team. This is the reason Notion scales across use cases (marketing wiki, eng roadmap, HR handbook) and the reason it decays without an owner (nested-page rot). The 2025+ push on Teamspaces + Home is an admission that pure emergence isn't enough at 500+ seats.",
    "NAV_INTERACTION_PARAGRAPH":
        "Mouse-first interaction with keyboard power-user layer (slash commands, quick find). Drag-to-restructure is the signature gesture — any block can move anywhere. Optimistic UI over a graph-shaped backend; sync improved dramatically 2024–2026 but still trails Linear/Figma on the perceived-latency axis in large workspaces.",
    "TTV_BAR": "70", "TTV_LABEL": "Fast",
    "COG_BAR": "60", "COG_LABEL": "Medium-High",
    "DELIGHT_BAR": "80", "DELIGHT_LABEL": "High",
    "TRUST_BAR": "78", "TRUST_LABEL": "High",
    "STRUGGLE_BAR": "58", "STRUGGLE_LABEL": "Medium",
    "DELIGHT_1": "Slash command → any block appears exactly where the cursor is.",
    "DELIGHT_2": "Toggling a table into a board/calendar/timeline in one click — the shape of the data changes, the data doesn't.",
    "DELIGHT_3": "Notion AI writing a first draft that already knows the workspace's tone and links to real internal sources.",
    "STRUGGLE_1": "Nested-page rot — after 6 months, teams can't find anything. Search never fully solved this.",
    "STRUGGLE_2": "Database learning curve — relations, rollups, formulas are Excel-hard for non-technical users.",
    "STRUGGLE_3": "Perceived latency at scale — large workspaces still show visible loads that Linear/Figma don't.",
    "REVENUE_MODEL_NAME": "Per-seat SaaS · 4 tiers · AI add-on",
    "REVENUE_MODEL_DETAIL": "Free (individuals + small teams) → Plus (~$10/user/mo) → Business (~$18) → Enterprise (custom). Notion AI is a per-seat add-on that is increasingly bundled at the top tiers. [inferred] Business + Enterprise + AI drive the majority of revenue.",
    "FREE_PAID_BOUNDARY_NAME": "Team scale, admin needs, and AI",
    "FREE_PAID_DETAIL": "Free is generous for individuals and tiny teams; paid tiers unlock unlimited file uploads, version history, admin/SSO, and (crucially) higher AI limits. AI is the paywall that most consistently moves free → paid in 2026.",
    "MON_ENTRY_HEADLINE": "'We've outgrown Free' + 'we need AI'",
    "MON_ENTRY_DETAIL": "First upgrade trigger: guest limits + admin control. Second: SSO / audit at Enterprise. Third (newest and biggest): AI limits — teams that use it once want it everywhere.",
    "UX_MON_HEADLINE": "Mostly aligned, one growing tension",
    "UX_MON_DETAIL_ARE_THEY_ALIGNED_OR_IN_TENSION":
        "Historically clean — paywalls hit at scale milestones, not mid-flow. The tension in 2026 is AI: metering AI at a moment users expect it as default creates friction. Notion's answer (bundle AI into Business/Enterprise, keep meter light on paid tiers) is smart, but the free-tier AI experience is now noticeably capped.",
    "CHANNEL_1": "Bottom-up PLG + creator/template economy (dominant)",
    "CHANNEL_2": "SEO on 'notion template for X' + 'notion vs Y' + Twitter/X design tribe",
    "CHANNEL_3": "Enterprise sales overlay on top of team-level adoption",
    "GROWTH_LOOP_1_NAME": "PLG · individual → team → org",
    "GROWTH_LOOP_1_DETAIL": "One person adopts → shares a page → team standardizes → admin buys seats → org negotiates Enterprise. Each hop is a natural upgrade trigger.",
    "GROWTH_LOOP_2_NAME": "Creator / template economy",
    "GROWTH_LOOP_2_DETAIL": "Creators publish templates, drive SEO + social, users copy templates and become active workspaces. Cheapest and most defensible acquisition loop in the category — a decade of accumulated content moat.",
    "HORIZONTAL_1": "Calendar + Mail (own the productivity suite, not just the wiki)",
    "HORIZONTAL_2": "Sites + Forms (turn Notion pages into public web surfaces)",
    "VERTICAL_1": "PM/eng workflow: PRD → project DB → linked meeting notes → AI status roll-up",
    "VERTICAL_2": "Sales & CS workflow: account pages + CRM-lite + AI enterprise search",
    "PLATFORM_1": "Notion API + integrations (Slack, GitHub, Linear, Figma) + Connectors that let AI read outside sources",
    "PLATFORM_2": "Agents as a platform — third parties (and eventually customers) shipping agents into the workspace",
    "ACTIVE_IF_ASSISTIVE": "", "ACTIVE_IF_EMBEDDED": "", "ACTIVE_IF_AUTONOMOUS": "active",
    "CURRENT_AI_USAGE_PARAGRAPH":
        "Level ~2.5 — well past assistive, credibly moving into autonomous. Notion AI writes, summarizes, translates, and answers questions grounded in workspace context (embedded). Notion 3 / Agents can watch signals (Slack, Gmail, Linear), draft pages, update databases, and take multi-step actions in the background (early autonomous). One of very few productivity products where AI already changes what a workspace *is*, not just how you type into it.",
    "AGENTIC_CANDIDATE_1": "Meeting → notes → follow-ups: agent joins the call, writes structured notes, opens tasks in the right DB, pings owners.",
    "AGENTIC_CANDIDATE_2": "PM status roll-up: agent reads project DBs, Linear, and PRs, drafts a weekly narrative for leadership.",
    "AGENTIC_CANDIDATE_3": "Customer-facing agent: reads the wiki + CRM, answers Slack #help-ops or a public help site, escalates when unsure.",
    "AI_OPPORTUNITY_1": "Auto-structuring rot — agent watches teamspaces, proposes merges/archives, and heals the IA in the background.",
    "AI_OPPORTUNITY_2": "Cross-workspace intelligence — agents that talk to *other* companies' Notion (with permission), enabling org-to-org workflows (vendor pages, partner OKRs).",
    "AI_DISRUPTION_RISK":
        "Medium-high. An AI-native workspace could reframe the primary interface as chat + agents, making the block canvas an implementation detail. Notion's answer (agents + Enterprise Search grounded in the workspace) is the right one, but OpenAI shipping a first-party 'work OS' is the existential scenario. The next 24 months decide whether Notion becomes the org's memory layer or its Wikipedia.",
    "FRICTION_1_TITLE": "Nested-page rot at scale",
    "FRICTION_1_BODY_WHY_IT_MATTERS":
        "In a 500-person org, Notion becomes a haystack. Search improved, Teamspaces helped, but the emergent-structure model still lacks a maintenance loop. This is the #1 reason large orgs argue for Confluence — 'at least we know where things are.' If AI can't heal it in 24 months, Notion loses the enterprise memory battle.",
    "FRICTION_2_TITLE": "Database power ≠ database usability",
    "FRICTION_2_BODY":
        "Relations, rollups, formulas are Excel-hard. Non-technical teammates hit a wall. Coda and Airtable are still real threats for the 'we need real DB logic' segment because their onboarding is more forgiving. Notion needs an AI-native DB builder that reads 'I want a bug tracker with SLAs' and just makes it.",
    "FRICTION_3_TITLE": "Perceived latency in large workspaces",
    "FRICTION_3_BODY":
        "Notion is dramatically faster than 2022, but at 5K+ page workspaces the loading state is still visible. Every second of load is a moment users compare Notion to Linear or Figma — and lose. Sync-engine investment must continue at the same intensity as AI investment.",
    "FRICTION_4_TITLE": "AI experience is uneven across surfaces",
    "FRICTION_4_BODY":
        "Notion AI in a doc is delightful. Notion AI over a large DB, an enterprise-search-scale corpus, or a multi-workspace query is inconsistent — sometimes brilliant, sometimes hallucinated. In a market where OpenAI ships weekly, 'inconsistent' reads as 'behind.' Ground truth + trust must be the top AI polish priority.",
    "OPP_1_HEADLINE": "IA Healer agent",
    "OPP_1_DETAIL_WHAT_HOW_WHY":
        "A background agent that watches teamspaces, flags duplicate pages, proposes merges, retires stale content, and reorganizes nested-page rot with a human approval step. Solves the #1 enterprise objection and turns Notion's biggest structural weakness into an AI-native strength. Ships in 2 quarters; unlocks the F500 memory-layer buyer.",
    "OPP_2_HEADLINE": "DB-from-intent builder",
    "OPP_2_DETAIL":
        "AI-native database builder that takes plain-English intent ('bug tracker with SLA, weekly digest, on-call rotation') and generates the schema, views, and automations. Kills the Airtable/Coda case for non-technical teams and expands the addressable population beyond power users.",
    "OPP_3_HEADLINE": "Agent Marketplace",
    "OPP_3_DETAIL":
        "Third-party (and customer-built) agents that run inside a workspace with scoped permissions and audit trails. Turns Notion from a product into a platform, mirrors what App Store did for iOS, and creates a moat AI-native competitors can't match without an install base.",
    "STRATEGIC_HEADLINE": "Reposition as the org's memory + labor layer",
    "STRATEGIC_DETAIL_HIGH_IMPACT_BET":
        "Stop selling 'a workspace.' Sell 'the substrate your agents run on.' Every doc, DB, and page becomes grounded context for a fleet of agents that write, query, and act on the org's behalf. Pricing shifts from per-seat to per-agent + per-seat. Moat compounds because the more the org uses Notion, the more useful the agents get — a data flywheel with real defensibility against OpenAI/Google, both of whom lack workspace context.",
    "MOONSHOT_HEADLINE": "Cross-org agent network",
    "MOONSHOT_DETAIL_WHY_IT_COULD_RESHAPE_THE_CATEGORY":
        "Notion becomes the protocol layer between companies. Your agent talks to your vendor's agent through shared Notion permissions — RFPs, invoices, project handoffs, partnership OKRs all flow agent-to-agent inside a scoped workspace neither side hosts. Notion moves from 'company OS' to 'inter-company OS' — the same category shift Slack tried with Connect and never landed. Winner-take-most if it works.",
    "FINAL_WINS":
        "Block model + creator economy + brand + workspace lock-in + real AI grounding. The horizontal-suite bets (Calendar, Mail, Sites, Agents) shipped and mostly land. Very few productivity companies have this many arrows in the air with this level of coherence.",
    "FINAL_BREAKS":
        "Nested-page rot at enterprise scale. DB learning curve caps the non-technical wedge. AI experience is brilliant in docs and uneven at scale. Perceived latency vs Linear/Figma. Free-tier AI meter is starting to feel stingy.",
    "FINAL_MOAT_OR_LACK_THEREOF":
        "Real and compounding — block model + workspace data graph + creator economy. But moat depth depends on the agent bet landing: if Notion becomes the org's grounded memory + labor layer, moat is durable for a decade. If a first-party 'work OS' from OpenAI/Google/Microsoft ships with equivalent grounding, Notion becomes 'the beautiful editor' — respected, growing, but no longer the category winner.",
    "SHOT_1_CAPTION": "Notion AI hero — write, ask, and act grounded in the workspace.",
    "SHOT_2_CAPTION": "Agents — autonomous workers that draft pages, update DBs, and take multi-step actions.",
    "SHOT_3_CAPTION": "Docs — the block canvas that started it all; still the atomic unit.",
    "SHOT_4_CAPTION": "Projects — DB + views = kanban, timeline, table without switching tools.",
    "SHOT_5_CAPTION": "AI Meeting Notes — meeting → structured notes → linked follow-ups.",
    "SHOT_6_CAPTION": "Notion Mail — inbox pulled inside the workspace graph.",

    # ----- §5 Craft signals -----
    "CRAFT_PRINCIPLE":
        "'Notion-quality' is a real, copyable pattern language — not a vibe. Five decisions define it, and each one is a place competitors either flinch or ship a diluted version.",
    "CRAFT_1_NAME": "One primitive: the block",
    "CRAFT_1_DETAIL": "Every atom of the product is a block that can nest, transform, and reflow. Text, tables, boards, embeds, AI outputs all share one contract. Google Docs, Confluence, and Coda have this partially; Notion committed all the way, which is why the surface expands cheaply.",
    "CRAFT_2_NAME": "Slash-command as the verb layer",
    "CRAFT_2_DETAIL": "`/` opens the full block vocabulary at the cursor. No modal, no config, no menu tax. It's the productivity-tool equivalent of a command palette — Notion normalized it for non-technical users years before it became table stakes.",
    "CRAFT_3_NAME": "Emergent structure over imposed structure",
    "CRAFT_3_DETAIL": "No global schema, no forced hierarchy. Teams build the IA they need, mistakes and all. This is why adoption is fast and rot is real — and why 'AI heals the IA' is the natural next move.",
    "CRAFT_4_NAME": "Illustrated brand as UI",
    "CRAFT_4_DETAIL": "Custom illustration system, warm marketing site, doodle-y empty states. The brand *is* part of the product — it lowers the emotional temperature of 'yet another SaaS tool' and buys tolerance for the DB learning curve.",
    "CRAFT_5_NAME": "AI as a first-class block, not a sidebar",
    "CRAFT_5_DETAIL": "Notion AI outputs live inline, editable, and versioned like any other block. It's not a chat pinned to the side — it's woven into the canvas. Most rivals still bolt AI on; Notion made it part of the primitive.",

    # ----- §8 Competitor landscape -----
    "COMP_INTRO":
        "Four rivals worth naming. Only one — OpenAI/ChatGPT with workspace ambitions — represents an existential threat. The others compete at the boundary (docs, wiki, DB) and are being outrun on breadth, not beaten on depth.",
    "COMP_1_NAME": "Google Workspace",
    "COMP_2_NAME": "Confluence (Atlassian)",
    "COMP_3_NAME": "Coda / Airtable",
    "COMP_4_NAME": "ChatGPT / OpenAI (work surface)",
    "COMP_DIM_1": "Philosophy",
    "COMP_DIM_2": "Speed & craft",
    "COMP_DIM_3": "AI depth & grounding (2026)",
    "COMP_DIM_4": "Company-OS ambition",
    "COMP_OWN_D1": "One block primitive, emergent structure, canvas as workspace",
    "COMP_1_D1":   "Separate apps (Docs, Sheets, Drive) stitched by Drive + Gemini",
    "COMP_2_D1":   "Structured wiki with enterprise governance; Jira-flavored discipline",
    "COMP_3_D1":   "DB-first workspace (Coda), relational tables (Airtable); both power-user leaning",
    "COMP_4_D1":   "Chat-first workspace, agents as primary interface, no canvas yet",
    "COMP_OWN_D2": "Strong; sync improved dramatically 2024–26 but not sub-100ms at scale",
    "COMP_1_D2":   "Fast on Docs/Sheets, sluggish and dated on Drive/Sites/Chat",
    "COMP_2_D2":   "Slow, legacy UI, actively hated by users; visible page loads",
    "COMP_3_D2":   "Coda fast-and-heavy; Airtable snappy in-table but heavier on nav",
    "COMP_4_D2":   "Very fast chat; no rich canvas yet, so speed comparison is unfair",
    "COMP_OWN_D3": "Deep and grounded: workspace context, agents, Enterprise Search",
    "COMP_1_D3":   "Gemini is capable but weakly grounded across siloed apps",
    "COMP_2_D3":   "Atlassian Intelligence: additive; grounding is inconsistent",
    "COMP_3_D3":   "Coda AI is table-grounded and strong; Airtable AI is early",
    "COMP_4_D3":   "Best raw model + agents; grounding requires connectors; no native workspace",
    "COMP_OWN_D4": "High: pitching itself as *the* company OS with intent",
    "COMP_1_D4":   "Owns email + calendar + storage; disjointed as an OS",
    "COMP_2_D4":   "Confined to eng+ops; brand can't cross the aisle",
    "COMP_3_D4":   "Coda tried and hit ceiling; Airtable narrower",
    "COMP_4_D4":   "The scariest vector — if OpenAI ships a first-party work OS, Notion's #1 direct rival",
    "COMP_WHERE_OWN_WINS":
        "Grounded AI + block canvas + workspace context + brand + creator economy. Nobody else has all five. Google and Atlassian have distribution but not coherence; Coda/Airtable have depth in DB but not breadth; ChatGPT has model but not canvas.",
    "COMP_WHERE_RIVALS_CATCH":
        "OpenAI's 'work' ambitions are the existential vector — 24-month watch. Google is quietly rebundling Gemini + Drive + Chat into a workspace-like posture. Confluence is losing but Atlassian's enterprise install base means it's not dying fast enough.",

    # ----- §11 Metrics they optimize for -----
    "METRICS_INTRO":
        "Notion doesn't publish OKRs, but you can read the metric stack off the product surface: what they invest in, what they defend, and — most tellingly — what they refuse to look at.",
    "NORTH_STAR_METRIC": "Weekly Active Workspaces × depth (≥3 members × ≥5 collaborative edits/wk)",
    "NORTH_STAR_WHY":
        "Not seat count and not MAU. A workspace with real, multi-person, sustained editing is the atomic unit of value — and the strongest leading indicator of paid conversion, AI attach, and retention.",
    "INPUT_METRIC_1_NAME": "AI attach rate (paid seats with active weekly AI use)",
    "INPUT_METRIC_1_WHY":
        "In 2026 this is the most important number in the building. AI usage drives upgrade + retention + the case for the agent pivot. If it stalls, the whole strategic narrative wobbles.",
    "INPUT_METRIC_2_NAME": "Databases created per workspace",
    "INPUT_METRIC_2_WHY":
        "Blocks are the atomic unit; databases are the moment users cross from 'doc' to 'app.' A workspace with real DBs has 3–5× the retention of a docs-only one. Notion protects this by making DB creation cheaper every quarter.",
    "INPUT_METRIC_3_NAME": "Time-to-second-workspace (alumni loop)",
    "INPUT_METRIC_3_WHY":
        "When someone leaves a company and starts a new one, Notion needs to be the reflex. The gap between company #1 and company #2 tells you whether the brand loop is intact — arguably the cheapest acquisition channel in the category.",
    "GUARDRAIL_METRIC": "Perceived latency on core interactions (page open, slash, DB view switch)",
    "GUARDRAIL_WHY":
        "Every ms of visible load is a comparison against Linear/Figma that Notion loses. Speed is the guardrail every new feature — especially AI — is measured against. If it degrades, adoption reverses at scale.",
    "METRIC_BLINDSPOT": "Nested-page rot (findability decay in workspaces older than 12 months)",
    "METRIC_BLINDSPOT_WHY":
        "Almost certainly not on the top-line dashboard. Which is exactly why enterprises still argue for Confluence. What you don't measure, you don't win — and this is the exact wedge OpenAI or Google could exploit to reframe workspaces around 'ask, don't hunt.'",

    # ----- §13 Risk matrix -----
    "RISK_INTRO":
        "Four risks worth calling out, ordered by severity. Each includes the leading indicator to watch and the mitigation Notion should ship.",
    "RISK_1_NAME": "OpenAI (or Google/Microsoft) ships a first-party 'work OS'",
    "RISK_1_CAT": "Competitive",
    "RISK_1_SEV": "High", "RISK_1_SEV_CLASS": "high",
    "RISK_1_LIK": "Medium-High · 12–24 mo",
    "RISK_1_MIT": "Double down on grounded agents + workspace context as the defensible layer; ship agent marketplace before hyperscalers reach parity; make Notion the substrate their models want to run on.",
    "RISK_2_NAME": "Enterprise memory battle lost to Confluence/Google on rot",
    "RISK_2_CAT": "Market",
    "RISK_2_SEV": "High", "RISK_2_SEV_CLASS": "high",
    "RISK_2_LIK": "Ongoing · already visible in F500 RFPs",
    "RISK_2_MIT": "Ship an IA Healer agent; instrument findability as a first-class metric; publish enterprise-scale case studies where the org grew past 5K seats without rot.",
    "RISK_3_NAME": "AI meter erodes free-tier goodwill and slows top-of-funnel",
    "RISK_3_CAT": "Growth",
    "RISK_3_SEV": "Medium", "RISK_3_SEV_CLASS": "med",
    "RISK_3_LIK": "Medium · 12 mo",
    "RISK_3_MIT": "Keep a genuinely useful free AI baseline; monetize via depth (agents, enterprise search, connectors) rather than metering the on-ramp; watch signup → first-AI-use conversion weekly.",
    "RISK_4_NAME": "Perceived-latency debt in large workspaces",
    "RISK_4_CAT": "Technical",
    "RISK_4_SEV": "Medium", "RISK_4_SEV_CLASS": "med",
    "RISK_4_LIK": "Medium · 18 mo",
    "RISK_4_MIT": "Continue sync-engine investment at the same intensity as AI investment; hold a hard SLO on page-open time even as blocks + AI outputs + agents multiply the graph.",
}

# ---------- Chinese content ----------
V_ZH = {
    "PRODUCT": "Notion",
    "ONE_LINER_2_LINE_SUBTITLE": "一款伪装成「文档」的积木式工作空间 —— 本质是「软数据库 + 可编程画布」，把 wiki、文档、任务、以及最近的 AI 助手一起吞进「公司操作系统」这一层。",
    "DATE_YYYY_MM_DD": DATE,
    "TIMESTAMP": f"{DATE} · 资深产品经理深度拆解",
    "CATEGORY": "公司操作系统 · 文档 + 数据库 + AI 工作空间",
    "USER_SCALE": "[推断] 1 亿+ 注册用户，~1000 万付费席位，10 万+ 付费组织",
    "BUSINESS_MODEL_SHORT": "按席位订阅 · 免费 / $10 / $18 / 企业版 · AI 附加订阅",
    "STAGE_MATURITY": "成熟成长期 · C 轮之后 · IPO 之前 · [推断] 现金流已转正",
    "ASSUMPTIONS_ONE_PARAGRAPH_LIST_WHAT_IS_INFERRED_VS_KNOWN":
        "产品界面、定价、以及公开发布过的产品（AI、Calendar、Mail、Agents、Enterprise Search）可直接观察。席位数、营收结构、留存、AI 附加率为 [推断]，依据是融资信息、媒体报道和公开的开发者调研。AI 深度基于 2026 年中期已发布的功能（Notion 3 / agents）。任一前提不对，告诉我重新生成。",
    "VERDICT_ONE_LINER": "这一代设计得最好的工作空间 —— 也是唯一在认真把自己从「团队写东西的地方」重定位成「团队 AI 助手运行的底层」的那一个。",
    "VERDICT_BODY_2_3_LINES":
        "Notion 靠「把文档做成软数据库」赢到今天：一个积木（block）原语就吞下了 wiki、任务、表格，现在还吞下了 AI 输出。这份灵活性是护城河也是天花板 —— 团队喜欢用，但结构靠他们自己维护。2026 年押注 Notion Agents 加 Enterprise Search，才是真正的赌注：赶在 Google / Microsoft / Atlassian 关窗之前，成为组织的「记忆 + 劳动」这一层。",
    "STAR_ROW_e_g_★★★★☆": "★★★★☆",
    "STAR_RATING_x": "4.4",
    "TLDR_1_HEADLINE": "「积木模型」就是护城河",
    "TLDR_1_BODY": "只有一个原语 —— block —— 就能让 Notion 是文档、是 wiki、是数据库、是看板、也是 AI 助手的界面。对手必须挑一种形状，Notion 拒绝挑。所以它横向扩张（Calendar、Mail、Sites、AI）看起来是原生的，不是硬贴上去的。",
    "TLDR_2_HEADLINE": "灵活也是天花板",
    "TLDR_2_BODY": "一张白纸对高手是自由，对普通人是瘫痪。「我的 Notion 一团糟」是真实的结构性流失原因 —— 也是 Coda、ClickUp、以及现在 Notion 自己的 AI 模板一直在切入的那把刀。",
    "TLDR_3_HEADLINE": "Notion 3 / Agents 决定生死",
    "TLDR_3_BODY": "AI 原生的对手可以把工作空间重构成「跟 AI 说话，不需要页面」。Notion 的回答 —— 在工作空间里、基于组织真实上下文写作、查询、行动的 agent —— 要么是它可持续的第二幕，要么就是 24 个月内被 OpenAI 灭掉的开局。",
    "TTV_VALUE": "~2", "TTV_UNIT": "分钟",
    "TTV_NOTE_WHAT_HAPPENS_AT_AHA": "第一次输入斜杠 → block 出现 → 拖一个数据库 → 意识到「我刚才是在做工具，不是在写文档」。这就是 Aha。",
    "LOOP_FREQ": "每天多次",
    "LOOP_FREQ_NOTE_TRIGGER_CONTEXT": "会议记录、项目页、个人任务清单、Slack 链接。个人每天 5–15 次；团队每周在规划 / 复盘文档上再锁一次节奏。",
    "MOAT_SCORE": "7.0",
    "MOAT_REASONING_ONE_LINE": "积木模型 + 工作空间锁定 + 品牌 + 正在成型的「AI 上下文图谱」= 今天很强；只有最后一条能扛住 AI 原生工作流的颠覆。",
    "SNAPSHOT_ONE_TO_TWO_SENTENCE_DEFINITION":
        "Notion 不是一个文档编辑器 —— 它是一块可编程的积木画布，底下铺着一层「软关系型数据库」，之所以对外叫「工作空间」，是因为绝大多数团队最先需要的就是那个形状。",
    "USER_PROMISE": "你团队写下的、追踪的、查找的每一件事，都住在同一个地方 —— 灵活到可以塑成任何工作流，结构化到 AI 可以跨全部内容进行推理。",
    "CATEGORY_POSITIONING_PARAGRAPH":
        "位置在文档（Google Docs、Confluence）、wiki（Confluence、Slab）、轻量项目管理（Asana、Trello）和轻量数据库（Airtable、Coda）的交点。刻意把自己定位成「*那个*公司操作系统」—— 不是一个工具，而是组织的运行界面。这个品类叫「工作空间」，而这个词今天是什么意思，Notion 出的力最多。",
    "ASSUMPTION_1": "自增长（PLG）优先；企业销售真实存在，但下游于团队级的采纳。",
    "ASSUMPTION_2": "AI 附加率是管理层内部真正在盯的领先指标。",
    "SEGMENT_1_NAME": "创业公司和现代 SaaS 团队",
    "SEGMENT_1_DETAIL": "10–500 人、YC 生态圈、拒绝 Confluence。Notion 安装量最大、口碑输出最猛的群体。",
    "SEGMENT_2_NAME": "大厂里的跨职能小队",
    "SEGMENT_2_DETAIL": "五百强内部的市场 / 运营 / 产品团队，需要一个共享界面，但等不了 IT 部门批准。按小队渗透。",
    "SEGMENT_3_NAME": "个人和创作者（Notion 当人生 OS）",
    "SEGMENT_3_DETAIL": "模板经济 —— 个人 wiki、第二大脑、自由职业者工作台。营收占比小，但流量入口和品牌护城河巨大。",
    "TRIGGER_MOMENT": "新团队起步；「我们 Google Drive 一团糟」；跳槽来的 PM / EM 拒绝在 Confluence 里写字；组织里有人在 X 上看到一份漂亮的 Notion 模板。",
    "FREQUENCY": "工程师 / 一线员工每个工作日多次；PM / EM 每天写会议记录、项目简报；高管每周做复盘和路线图。",
    "USAGE_CONTEXT": "在 Slack、Figma、Linear、Google Meet 之间来回切。Notion 是「引用层」—— 大家需要说「真相在哪」的时候，链接指向的地方。",
    "JTBD_FUNCTIONAL": "\"当我要抓、要结构化、要找一件团队需要的东西的时候，我要一个能塑成我这个任务的地方，而不是被塞进别人的模板。\"",
    "JTBD_EMOTIONAL": "\"我要感觉自己是有组织的、在掌控的 —— 我的团队跑在一个真正的系统上，不是一堆 Slack 讨论加 Google 文档。\"",
    "JTBD_SOCIAL": "\"我想让团队、候选人、投资人一眼看出我们是一家现代的、认真的公司 —— 一份漂亮的 Notion 就是这句话的简写。\"",
    "LOOP_TRIGGER_TITLE": "一次「信息摩擦」出现",
    "LOOP_TRIGGER_DETAIL": "会议开始；项目启动；队友问「文档在哪」；一个想法必须立刻有个家。",
    "LOOP_ACTION_TITLE": "/ → block → 结构",
    "LOOP_ACTION_DETAIL": "斜杠命令唤出合适的 block（页面、数据库、Callout、折叠）。结构在写作的手底下自然长出来，不需要任何配置界面。",
    "LOOP_REWARD_TITLE": "立刻可以分享的产物",
    "LOOP_REWARD_DETAIL": "一条 URL 替代了「一段 Slack 讨论 + 一份 Google 文档 + 一张 Airtable 表格」。感觉像是在写字的时间里*搭*出了一个东西。",
    "LOOP_RETURN_TITLE": "页面本身变成了仪式",
    "LOOP_RETURN_DETAIL": "每周 1:1、项目跟踪表、值班表 —— 页面变成了组织的节奏。你回来，不是因为 Notion 提醒你，是因为会议要开了。",
    "LOOP_ONE_LINE_INSIGHT_WHAT_THE_LOOP_ACTUALLY_TEACHES_THE_USER":
        "这个循环真正教你的是：「写下来」和「搭出一个工具」是同一个动作 —— 文档不是软件的前身，文档就是软件。",
    "ACQUISITION_LOOP_DETAIL":
        "个人 → 团队邀请（自下而上）+ 创作者 / 模板经济 → 「notion template for X」的 SEO + 推特设计圈 → 组织标准化后升级企业版。校友循环：离职员工去下一家继续装 Notion。",
    "AHA_MOMENT_DETAIL":
        "你第一次把一个页面变成数据库视图，再把它切成同一批数据的看板，再嵌到另一个页面里 —— 积木模型「叮」的一声打通了，你意识到你手里的不是一个文本编辑器，是一个低代码工具。",
    "RETENTION_1": "工作空间锁定 —— 你搭的所有东西都在这里，导出合法但很痛。",
    "RETENTION_2": "团队仪式重力 —— 周报、1:1、项目页变成日历的形状。",
    "RETENTION_3": "AI 扎根于你的工作空间 —— 用得越多，Notion AI 越有用；经典的「数据复利」循环。",
    "VIRALITY_DETAIL_OR_NONE":
        "产品内：来宾链接 + 公开分享页孕育跨组织的自然发现。产品外：YouTube / TikTok / X 上的创作者与模板经济 —— 大概是 Dropbox 以来生产力 SaaS 里内容驱动最强的病毒传播。",
    "SURFACE_1_NAME": "页面 / 积木画布", "SURFACE_1_ROLE": "原子单位 —— 所有文档、数据库、视图、嵌入都住在这里。",
    "SURFACE_2_NAME": "侧栏（Teamspaces）", "SURFACE_2_ROLE": "导航 + 信息架构层；组织形状在这里变得可见。",
    "SURFACE_3_NAME": "数据库 + 视图", "SURFACE_3_ROLE": "把页面变成 app 的「软数据库」层（表格、看板、日历、时间线）。",
    "SURFACE_4_NAME": "Notion AI 面板", "SURFACE_4_ROLE": "在工作空间里写、总结、问答 —— 内嵌在上下文里，而不是旁边一个聊天窗口。",
    "SURFACE_5_NAME": "Agents / Notion 3", "SURFACE_5_ROLE": "自主工作者，能吃 Slack / Gmail / Linear 的信号，写页面、更新数据库、做多步操作。",
    "SURFACE_6_NAME": "Calendar + Mail", "SURFACE_6_ROLE": "喂给同一张图谱的相邻界面；时间和收件箱现在也进入工作空间。",
    "ENTITY_1": "积木（Block）", "ENTITY_2": "页面（Page）", "ENTITY_3": "数据库 + 视图", "ENTITY_4": "团队空间（Teamspace）", "ENTITY_5": "AI 助手（Agent）",
    "IA_LOGIC_PARAGRAPH":
        "信息架构故意做得「软」：页面可以无限嵌套，Teamspaces 把它们分组，数据库把它们关联起来。没有全局 schema —— 结构按团队自己长出来。这就是 Notion 能横跨市场 wiki、工程路线图、HR 手册的原因，也是它没有维护者就腐烂（嵌套页面 rot）的原因。2025 年之后不断加码 Teamspaces + Home，就是承认「纯涌现」在 500 席以上不够用。",
    "NAV_INTERACTION_PARAGRAPH":
        "鼠标优先，键盘为高手层加了斜杠命令和快速跳转。「拖动重组」是标志性手势 —— 任何 block 都能拖到任何位置。乐观界面 + 图状后端；2024–2026 同步显著改善，但在大工作空间里的感知延迟仍然落后于 Linear / Figma。",
    "TTV_BAR": "70", "TTV_LABEL": "较快",
    "COG_BAR": "60", "COG_LABEL": "中高",
    "DELIGHT_BAR": "80", "DELIGHT_LABEL": "高",
    "TRUST_BAR": "78", "TRUST_LABEL": "高",
    "STRUGGLE_BAR": "58", "STRUGGLE_LABEL": "中",
    "DELIGHT_1": "斜杠命令 → 你需要的 block 精确出现在光标位置。",
    "DELIGHT_2": "一键把一张表格切成看板 / 日历 / 时间线 —— 数据形状变了，数据本身没变。",
    "DELIGHT_3": "Notion AI 一次性起草的第一稿，已经知道你团队的语气，还带着真实内部资料的链接。",
    "STRUGGLE_1": "嵌套页面腐烂 —— 用了半年，团队再也找不到东西。搜索始终没有真正解决这个。",
    "STRUGGLE_2": "数据库学习曲线 —— 关系、汇总、公式对非技术用户是 Excel 级难度。",
    "STRUGGLE_3": "大工作空间下的感知延迟 —— 仍然能看见加载态，Linear / Figma 没有。",
    "REVENUE_MODEL_NAME": "按席位订阅 · 4 档 · AI 附加",
    "REVENUE_MODEL_DETAIL": "免费（个人 + 小团队）→ Plus（~$10/人/月）→ Business（~$18）→ Enterprise（自定义）。Notion AI 是按席位加的一档，正逐步打包进高档套餐。[推断] Business + Enterprise + AI 是主要营收来源。",
    "FREE_PAID_BOUNDARY_NAME": "按「团队规模、管理员需求、AI」三条线",
    "FREE_PAID_DETAIL": "免费版对个人和小团队很慷慨；付费解锁无限上传、版本历史、管理员 / SSO，以及（关键）更高的 AI 配额。2026 年最能把免费用户推向付费的那道门，就是 AI。",
    "MON_ENTRY_HEADLINE": "「我们撑爆免费版了」+「我们需要 AI」",
    "MON_ENTRY_DETAIL": "第一次升级触发：来宾数量上限 + 管理员控制。第二次：企业版的 SSO / 审计。第三次（最新也最猛）：AI 配额 —— 用过一次的团队会想到处都用。",
    "UX_MON_HEADLINE": "整体对齐，一个正在积累的张力",
    "UX_MON_DETAIL_ARE_THEY_ALIGNED_OR_IN_TENSION":
        "历史上很干净 —— 付费墙落在规模里程碑上，不是任务中途。2026 年的张力是 AI：在用户默认「AI 是标配」的时代，给 AI 计量会带来摩擦。Notion 的应对（把 AI 打包进 Business / Enterprise，付费档的计量做轻）是聪明的，但免费档的 AI 体验现在明显被压制了。",
    "CHANNEL_1": "自下而上的 PLG + 创作者 / 模板经济（主渠道）",
    "CHANNEL_2": "「notion template for X」和「notion vs Y」的 SEO + 推特设计圈",
    "CHANNEL_3": "企业销售叠在团队级采纳之上",
    "GROWTH_LOOP_1_NAME": "PLG · 个人 → 团队 → 组织",
    "GROWTH_LOOP_1_DETAIL": "一个人先用 → 分享一个页面 → 团队标准化 → 管理员买席位 → 组织谈企业版。每一跳都是天然的升级触发点。",
    "GROWTH_LOOP_2_NAME": "创作者 / 模板经济",
    "GROWTH_LOOP_2_DETAIL": "创作者发布模板，带来 SEO 和社交流量，用户复制模板，从而变成活跃的工作空间。本品类里最便宜、最难被复制的获客循环 —— 十年积累的内容护城河。",
    "HORIZONTAL_1": "Calendar + Mail（拿下整个生产力套件，不只 wiki）",
    "HORIZONTAL_2": "Sites + Forms（把 Notion 页面变成对外的公开界面）",
    "VERTICAL_1": "产品 / 工程工作流：PRD → 项目数据库 → 关联的会议记录 → AI 状态汇总",
    "VERTICAL_2": "销售与客户成功工作流：客户页面 + 轻量 CRM + AI 企业搜索",
    "PLATFORM_1": "Notion API + 集成（Slack、GitHub、Linear、Figma）+ Connectors 让 AI 读外部数据",
    "PLATFORM_2": "Agents 作为平台 —— 第三方（最终也包括客户）把自己的 agent 部署进工作空间",
    "ACTIVE_IF_ASSISTIVE": "", "ACTIVE_IF_EMBEDDED": "", "ACTIVE_IF_AUTONOMOUS": "active",
    "CURRENT_AI_USAGE_PARAGRAPH":
        "水平大约在 2.5 —— 远超「辅助工具」，可信地在向「自主」推进。Notion AI 写作、总结、翻译、基于工作空间上下文回答问题（深度嵌入）。Notion 3 / Agents 能监听信号（Slack、Gmail、Linear）、起草页面、更新数据库、后台执行多步操作（早期自主）。极少数生产力产品里，AI 已经改变了「工作空间是什么」，不仅是「怎么打字」。",
    "AGENTIC_CANDIDATE_1": "会议 → 记录 → 后续：agent 参会、写结构化笔记、在合适的数据库里开任务、@ 责任人。",
    "AGENTIC_CANDIDATE_2": "PM 状态汇总：agent 读项目数据库、Linear 和 PR，起草一份高管周报叙事。",
    "AGENTIC_CANDIDATE_3": "面向客户的 agent：读 wiki + CRM，接管 Slack #help-ops 或对外的帮助站点，不确定就升级。",
    "AI_OPPORTUNITY_1": "自动修复腐烂 —— agent 监听 teamspace，建议合并 / 归档，后台自愈信息架构。",
    "AI_OPPORTUNITY_2": "跨工作空间的智能 —— agent 之间（在授权下）可以和*别的公司*的 Notion 对话，打通组织与组织之间的工作流（供应商页面、合作伙伴 OKR）。",
    "AI_DISRUPTION_RISK":
        "中偏高。一个 AI 原生的工作空间可以把主界面重构成「聊天 + agent」，让积木画布沦为实现细节。Notion 的应对（扎根于工作空间的 agent + Enterprise Search）是对的方向，但 OpenAI 亲自下场做一个「Work OS」是生死场景。未来 24 个月决定 Notion 是变成组织的「记忆层」，还是变成组织的「维基百科」。",
    "FRICTION_1_TITLE": "规模化后的嵌套页面腐烂",
    "FRICTION_1_BODY_WHY_IT_MATTERS":
        "在 500 人组织里，Notion 变成大草垛。搜索改善了，Teamspaces 有帮助，但「涌现式结构」这套模型仍然缺一个「维护循环」。这是大企业还在替 Confluence 说话的第一号理由 ——「至少我们知道东西在哪」。如果 AI 在 24 个月内治不好这个，Notion 就输掉了企业级的「记忆之战」。",
    "FRICTION_2_TITLE": "数据库的能力 ≠ 数据库的可用性",
    "FRICTION_2_BODY":
        "关系、汇总、公式对非技术用户是 Excel 级别的难。Coda 和 Airtable 在「我们需要真正的数据库逻辑」这个细分市场上仍然是真实威胁，因为它们上手更宽容。Notion 需要一个 AI 原生的数据库构建器 —— 你说「我要一个带 SLA 的 bug 跟踪表」，它就给你搭好。",
    "FRICTION_3_TITLE": "大工作空间的感知延迟",
    "FRICTION_3_BODY":
        "比 2022 年快了很多，但 5000+ 页面的工作空间里，加载态仍然可见。每一秒加载都是用户在把 Notion 和 Linear / Figma 做对比，然后 Notion 输一次。同步引擎的投入必须和 AI 投入同强度地持续。",
    "FRICTION_4_TITLE": "AI 体验在不同界面上不均匀",
    "FRICTION_4_BODY":
        "文档里的 Notion AI 很让人愉悦。跨大数据库、跨企业搜索规模的语料、跨多工作空间的查询，就变得时而惊艳、时而胡编。在 OpenAI 每周发新东西的市场里，「不稳定」就等于「落后」。「有真实依据 + 可信度」必须是 AI 打磨的第一优先级。",
    "OPP_1_HEADLINE": "「信息架构治愈」agent",
    "OPP_1_DETAIL_WHAT_HOW_WHY":
        "一个后台 agent，监听 teamspace，标出重复页面、建议合并、归档过期内容、把嵌套页面的腐烂重排一遍，全部需要人点确认。解决大企业最大的反对意见，把 Notion 最大的结构性弱点变成 AI 原生的强项。2 个季度内可出；打开五百强「记忆层」这个买家。",
    "OPP_2_HEADLINE": "「意图直建」数据库",
    "OPP_2_DETAIL":
        "AI 原生的数据库构建器，接受一段大白话（「一个带 SLA 的 bug 跟踪表，每周日报，值班轮换」），直接生成 schema、视图、自动化。让 Airtable / Coda 在非技术团队上的机会消失，把可服务的人群从「高手」扩到「所有人」。",
    "OPP_3_HEADLINE": "Agent 应用市场",
    "OPP_3_DETAIL":
        "第三方（以及客户自建）的 agent 在有作用域的权限和审计下运行在工作空间里。让 Notion 从「产品」变成「平台」，等同于 App Store 之于 iOS，形成 AI 原生对手没有装机量就打不出来的护城河。",
    "STRATEGIC_HEADLINE": "重定位为「组织的记忆 + 劳动」这一层",
    "STRATEGIC_DETAIL_HIGH_IMPACT_BET":
        "不再卖「一个工作空间」。卖「你 agent 运行的底层」。每一份文档、每一个数据库、每一个页面都变成一支 agent 舰队的真实上下文，让它们代表组织写、查、行动。定价从「按席位」向「按 agent + 按席位」演化。护城河会复利 —— 组织越用 Notion，agent 越有用 —— 这是对 OpenAI / Google 最可防守的一层，因为他们没有工作空间上下文。",
    "MOONSHOT_HEADLINE": "跨组织的 agent 网络",
    "MOONSHOT_DETAIL_WHY_IT_COULD_RESHAPE_THE_CATEGORY":
        "Notion 变成公司与公司之间的协议层。你的 agent 通过共享的 Notion 权限，跟你供应商的 agent 对话 —— RFP、发票、项目交接、合作 OKR 全部 agent 对 agent 地在一个双方都不托管的作用域空间里跑。Notion 从「公司 OS」升级为「公司间 OS」—— Slack Connect 想过、没做成的那次品类转变。做成即赢家通吃。",
    "FINAL_WINS":
        "积木模型 + 创作者经济 + 品牌 + 工作空间锁定 + 真实的 AI 依据。横向套件的赌注（Calendar、Mail、Sites、Agents）都发布了、大多数落地了。生产力品类里，同时在空中的箭这么多、还这么协调的公司极少。",
    "FINAL_BREAKS":
        "企业规模下的嵌套页面腐烂。数据库学习曲线压住了非技术人群的扩张。AI 体验在文档里惊艳，在规模上不均匀。相对 Linear / Figma 的感知延迟。免费版 AI 配额开始显得抠。",
    "FINAL_MOAT_OR_LACK_THEREOF":
        "真实并且在复利 —— 积木模型 + 工作空间数据图谱 + 创作者经济。但护城河的深度，取决于 agent 这一赌注能不能落地：如果 Notion 成为组织有依据的「记忆 + 劳动」层，可持续十年；如果 OpenAI / Google / Microsoft 有一天出了带同等依据的第一方「Work OS」，Notion 就会变成「那个漂亮的编辑器」—— 被尊重、也在增长，但不再是品类赢家。",
    "SHOT_1_CAPTION": "Notion AI Hero —— 基于工作空间的写、问、行动。",
    "SHOT_2_CAPTION": "Agents —— 自主工作者，起草页面、更新数据库、执行多步操作。",
    "SHOT_3_CAPTION": "文档 —— 一切开始的积木画布；至今仍是原子单位。",
    "SHOT_4_CAPTION": "项目 —— 数据库 + 视图 = 看板 / 时间线 / 表格，不用切换工具。",
    "SHOT_5_CAPTION": "AI 会议记录 —— 会议 → 结构化笔记 → 关联的后续任务。",
    "SHOT_6_CAPTION": "Notion Mail —— 收件箱被拉进工作空间的图谱里。",

    # ----- §5 Craft signals -----
    "CRAFT_PRINCIPLE":
        "「Notion 级别的品质」是一套可以数出来、也可以被抄的具体决策 —— 不是一种氛围。定义它的有五条，每一条都是竞品要么犹豫、要么出了个稀释版的地方。",
    "CRAFT_1_NAME": "只有一个原语：block（积木）",
    "CRAFT_1_DETAIL": "产品里每一个最小单位都是 block —— 可以嵌套、变形、回流。文字、表格、看板、嵌入、AI 输出，全部共用一个契约。Google Docs、Confluence、Coda 只做了一半；Notion 一路押到底，所以产品面能以低成本扩张。",
    "CRAFT_2_NAME": "斜杠命令作为动词层",
    "CRAFT_2_DETAIL": "`/` 在光标处唤出全部 block 词汇。没有弹窗、没有配置、没有菜单税。它是生产力工具里的「命令面板」—— Notion 早在这套东西成为标配之前，就把它带给了非技术用户。",
    "CRAFT_3_NAME": "涌现式结构，而不是强加的结构",
    "CRAFT_3_DETAIL": "没有全局 schema，没有强制层级。团队搭自己需要的信息架构，包括其中的错误。这就是采纳快的原因，也是腐烂真实的原因 —— 也是「用 AI 治愈信息架构」为什么会是下一步。",
    "CRAFT_4_NAME": "插画式品牌本身就是 UI",
    "CRAFT_4_DETAIL": "自定义插画体系、温暖的营销站、涂鸦感的空态。品牌本身就是产品的一部分 —— 它把「又一个 SaaS」的情绪温度调低了，也换来了用户对数据库学习曲线的耐心。",
    "CRAFT_5_NAME": "AI 是一等公民 block，不是侧栏",
    "CRAFT_5_DETAIL": "Notion AI 的输出是行内的、可编辑的、和别的 block 一样有版本记录。不是一个钉在侧边的聊天窗口 —— 它织进了画布本身。大多数对手还在把 AI 硬贴上去；Notion 把它做成原语的一部分。",

    # ----- §8 Competitor landscape -----
    "COMP_INTRO":
        "四个值得单独点名的对手。只有一个 —— 带有工作空间野心的 OpenAI / ChatGPT —— 是生死级威胁。其他三家在边界处竞争（文档、wiki、数据库），并且在「宽度」上被 Notion 甩开，不是在「深度」上被打败。",
    "COMP_1_NAME": "Google Workspace",
    "COMP_2_NAME": "Confluence（Atlassian）",
    "COMP_3_NAME": "Coda / Airtable",
    "COMP_4_NAME": "ChatGPT / OpenAI（工作界面）",
    "COMP_DIM_1": "产品哲学",
    "COMP_DIM_2": "速度与手艺",
    "COMP_DIM_3": "AI 深度与依据（2026）",
    "COMP_DIM_4": "「公司 OS」的野心",
    "COMP_OWN_D1": "一个 block 原语，涌现式结构，画布即工作空间",
    "COMP_1_D1":   "分离的应用（Docs / Sheets / Drive），靠 Drive + Gemini 拼在一起",
    "COMP_2_D1":   "结构化 wiki + 企业治理；Jira 味道的纪律",
    "COMP_3_D1":   "Coda 数据库优先；Airtable 关系表；两家都偏高手",
    "COMP_4_D1":   "聊天优先的工作空间，agent 作为主界面，还没有画布",
    "COMP_OWN_D2": "较强；2024–26 同步显著改善，但在规模上仍不到亚 100 毫秒",
    "COMP_1_D2":   "Docs / Sheets 快，Drive / Sites / Chat 慢且老",
    "COMP_2_D2":   "慢、老界面、用户真心讨厌；页面加载肉眼可见",
    "COMP_3_D2":   "Coda 又快又重；Airtable 在表格里丝滑，导航更沉",
    "COMP_4_D2":   "聊天极快；还没有富画布，速度比不构成公平对比",
    "COMP_OWN_D3": "深、有依据：工作空间上下文 + agent + Enterprise Search",
    "COMP_1_D3":   "Gemini 能力强，但在割裂的应用间「依据」很弱",
    "COMP_2_D3":   "Atlassian Intelligence：加法式；依据不稳定",
    "COMP_3_D3":   "Coda AI 依据在表内、能力强；Airtable AI 还早",
    "COMP_4_D3":   "最强的原始模型 + agent；依据靠 connector；没有原生工作空间",
    "COMP_OWN_D4": "高：真心把自己卖成「那个公司 OS」",
    "COMP_1_D4":   "拥有邮件 + 日历 + 存储；作为 OS 是割裂的",
    "COMP_2_D4":   "锁死在工程 + 运维；品牌过不了界",
    "COMP_3_D4":   "Coda 尝试过并撞了天花板；Airtable 更窄",
    "COMP_4_D4":   "最可怕的方向 —— 如果 OpenAI 出第一方 Work OS，就是 Notion 的头号直接对手",
    "COMP_WHERE_OWN_WINS":
        "有依据的 AI + 积木画布 + 工作空间上下文 + 品牌 + 创作者经济。五样同时齐的只有 Notion。Google 和 Atlassian 有分发但没协调；Coda / Airtable 在数据库上有深度但没宽度；ChatGPT 有模型但没画布。",
    "COMP_WHERE_RIVALS_CATCH":
        "OpenAI 的「工作」野心是生死级方向 —— 24 个月内必须盯紧。Google 正在悄悄把 Gemini + Drive + Chat 重打包成一个工作空间的姿态。Confluence 在输，但 Atlassian 的企业装机量意味着它死得没有那么快。",

    # ----- §11 Metrics they optimize for -----
    "METRICS_INTRO":
        "Notion 不公开 OKR，但你可以从产品面读出他们的指标栈：他们投什么、守什么、以及最能说明问题的 —— 他们拒绝去看什么。",
    "NORTH_STAR_METRIC": "周活跃工作空间 × 深度（≥3 人 × 每周 ≥5 次协作编辑）",
    "NORTH_STAR_WHY":
        "不是席位数、也不是月活。一个多成员、持续协作编辑的工作空间才是价值的最小单位 —— 也是付费转化、AI 附加率和留存的最强领先信号。",
    "INPUT_METRIC_1_NAME": "AI 附加率（每周活跃使用 AI 的付费席位比例）",
    "INPUT_METRIC_1_WHY":
        "2026 年这是楼里最重要的一个数字。AI 使用推动升级 + 留存 + 支撑 agent 转向的叙事。这一条卡住，整个战略故事都晃。",
    "INPUT_METRIC_2_NAME": "每个工作空间创建的数据库数",
    "INPUT_METRIC_2_WHY":
        "block 是原子单位；数据库是「从文档跨到应用」的那一步。有真数据库的工作空间，留存是纯文档工作空间的 3–5 倍。Notion 每个季度都在让创建数据库变得更便宜，就是在守这条。",
    "INPUT_METRIC_3_NAME": "「第二次装 Notion」的时间（校友循环）",
    "INPUT_METRIC_3_WHY":
        "有人从一家公司走了、去开新公司，Notion 要成为下意识。从公司 #1 到公司 #2 的间隔时间，告诉你品牌循环还在不在 —— 这可能是本品类里最便宜的获客渠道。",
    "GUARDRAIL_METRIC": "核心交互的感知延迟（页面打开、斜杠命令、数据库视图切换）",
    "GUARDRAIL_WHY":
        "每一毫秒可见的加载都是用户拿 Notion 跟 Linear / Figma 做的一次比较，Notion 输一次。速度是每一个新功能 —— 尤其 AI —— 必须被卡的那道栏。守不住，规模化后采纳会反向。",
    "METRIC_BLINDSPOT": "嵌套页面腐烂（12 个月以上工作空间的可查找性衰减）",
    "METRIC_BLINDSPOT_WHY":
        "几乎可以断定不在核心看板上。这也正是大企业还在替 Confluence 说话的原因。你不看的指标，就赢不了 —— 而这正是 OpenAI 或 Google 可能借之把工作空间重构成「问，别搜」的那把楔子。",

    # ----- §13 Risk matrix -----
    "RISK_INTRO":
        "四条值得单独列出的风险，按严重程度排列。每一条都给出应盯的领先指标和 Notion 应该落地的具体缓解动作。",
    "RISK_1_NAME": "OpenAI（或 Google / Microsoft）发布第一方「Work OS」",
    "RISK_1_CAT": "竞争",
    "RISK_1_SEV": "高", "RISK_1_SEV_CLASS": "high",
    "RISK_1_LIK": "中偏高 · 12–24 个月",
    "RISK_1_MIT": "把「有依据的 agent + 工作空间上下文」加倍下注，作为可防守的一层；在超大规模玩家追平之前发布 agent 应用市场；让 Notion 变成「他们的模型愿意跑在上面的底层」。",
    "RISK_2_NAME": "企业级「记忆之战」输给 Confluence / Google，因为腐烂",
    "RISK_2_CAT": "市场",
    "RISK_2_SEV": "高", "RISK_2_SEV_CLASS": "high",
    "RISK_2_LIK": "已经在发生，五百强 RFP 里可见",
    "RISK_2_MIT": "发布信息架构治愈 agent；把「可查找性」做成一等指标；公布 5000+ 席位不腐烂的企业级案例。",
    "RISK_3_NAME": "AI 计量侵蚀免费档口碑，拖慢流量入口",
    "RISK_3_CAT": "增长",
    "RISK_3_SEV": "中", "RISK_3_SEV_CLASS": "med",
    "RISK_3_LIK": "中 · 12 个月",
    "RISK_3_MIT": "保留真正好用的免费 AI 基线；靠深度（agent、企业搜索、connector）收钱，而不是靠给入口设卡；每周盯「注册 → 首次用 AI」的转化。",
    "RISK_4_NAME": "大工作空间下的「感知延迟」技术债",
    "RISK_4_CAT": "技术",
    "RISK_4_SEV": "中", "RISK_4_SEV_CLASS": "med",
    "RISK_4_LIK": "中 · 18 个月",
    "RISK_4_MIT": "同步引擎的投入必须与 AI 投入同强度地持续；即使 block + AI 输出 + agent 让图谱膨胀，也要死守页面打开时间的 SLO。",
}


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

subprocess.run(["open", str(OUT_EN)])
print("Opened EN. Click 中文 in the bottom-right to switch.")
