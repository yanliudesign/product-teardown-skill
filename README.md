<div align="center">

[Chinese](./README_zh.md) · **English**

# 🔬 Product Teardown Skill

---

**Reverse-engineer any product as a system — and get a bilingual, print-ready HTML report. In one shot.**

[![License](https://img.shields.io/badge/LICENSE-MIT-4c8bf5?style=flat-square&labelColor=333)](./LICENSE)
[![Version](https://img.shields.io/badge/VERSION-1.0.0-2ea44f?style=flat-square&labelColor=333)]()
[![Stars](https://img.shields.io/github/stars/yanliudesign/product-teardown-skill?style=flat-square&label=STARS&color=e37f2c&labelColor=333)](https://github.com/yanliudesign/product-teardown-skill/stargazers)

[![Claude Code](https://img.shields.io/badge/Claude_Code-Skill-d97757?style=flat-square&labelColor=1a1a1a&logo=anthropic&logoColor=white)](https://claude.ai/code)
[![Codex](https://img.shields.io/badge/Codex-Skill-2ea44f?style=flat-square&labelColor=1a1a1a)]()
[![OpenCode](https://img.shields.io/badge/OpenCode-Skill-4c8bf5?style=flat-square&labelColor=1a1a1a)]()
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Skill-8b5cf6?style=flat-square&labelColor=1a1a1a)]()
[![Hermes](https://img.shields.io/badge/Hermes-Skill-e879a8?style=flat-square&labelColor=1a1a1a)]()

</div>

A Principal-PM-level product-teardown skill. Point it at any product (Linear, Notion, Cursor, Perplexity…) and it reverse-engineers the thing as a *system* — loops, strategy, moat, opportunities — then renders the analysis as a bilingual (EN + ZH), print-ready HTML report with an embedded product-screenshot gallery. Not a "5 things I like about this app" review. A structural read of *why the product wins, where it leaks, and what the next move should be*.

---

## How it works — just 2 steps

Invoke the skill with anything like "teardown Linear" / "break down Notion" / "analyze Cursor" and it runs the same flow every time:

1. **Chat response** — full teardown in 11 sections (Snapshot → Users & JTBD → Core Loop → Architecture → UX Quality → Business Model → Growth → AI Readiness → Friction → Opportunities → Final PM Verdict).
2. **HTML report auto-generates** — two cross-linked files (EN + ZH, toggle in the bottom-right), saved to `~/Desktop/Claude skills/product-teardown-<slug>-{en,zh}-<yyyymm>.html`. Print-optimized (Cmd+P → clean PDF).

---

## Teardown Report · the 11-section spine

Every run ends with two single-file HTML reports at `~/Desktop/Claude skills/`. Fixed 11-section spine, plus a product-tour gallery:

| # | Section | What it answers |
|---|---------|-----------------|
| — | **Product Tour** | 6 screenshots pulled from the product's own `og:image` marketing assets. |
| **1** | **Snapshot** | One-line pitch · category · stage · pricing · notable numbers. |
| **2** | **Users & JTBD** | Who hires this product, and for what job — including the *replaced* alternative. |
| **3** | **Core Loop** | The atomic user loop that makes the product habit-forming (or doesn't). |
| **4** | **Architecture** | Object model · surfaces · integrations · what's a primitive vs a feature. |
| **5** | **UX Quality** | Signature interactions, latency, information density, empty states. |
| **6** | **Business Model** | Monetization vector · unit economics · expansion path (PLG / sales / hybrid). |
| **7** | **Growth** | Acquisition loops · virality vector · retention hooks · notable moats. |
| **8** | **AI Readiness** | Assistive / Embedded / Autonomous — placed on the spectrum with evidence. |
| **9** | **Friction** | Where the product leaks — onboarding, mid-funnel, power-user ceiling. |
| **10** | **Opportunities** | 3–5 concrete next-move bets (features, wedges, adjacencies). |
| **11** | **Final PM Verdict** | The one sentence a Principal PM would write on the internal doc. |

Reports are print-optimized (Cmd+P → clean PDF) and cross-linked EN ↔ ZH via a bottom-right language switcher.

---

## Five design principles

1. **Structure over opinion.** Every section answers a specific question. No "here's what I think about this app."
2. **Loops, not features.** The Core Loop section is the spine of the teardown — features are downstream of the loop.
3. **AI placement is a spectrum, not a badge.** Assistive / Embedded / Autonomous — pick one and defend it with evidence.
4. **Screenshots must come from the product itself.** Pull from `og:image` marketing assets (`curl -s <url> | grep og:image`), not random blog posts.
5. **Bilingual by default.** Every teardown ships EN + ZH in the same run, cross-linked. Not translated later.

---

## Repo contents

```
product-teardown-skill/
├── product-teardown-prompt.md              # Portable skill prompt (paste into any tool)
├── templates/
│   ├── product-teardown-template-en.html   # English report template
│   └── product-teardown-template-zh.html   # Chinese report template (same placeholders)
└── scripts/
    ├── fill_linear.py                      # Reference implementation — renders both templates
    └── translate_template_zh.py            # One-shot: derives the ZH template from EN
```

- **Aesthetic:** cream paper + serif display + yellow accent. Print-optimized.
- **Placeholders:** `{{ALL_CAPS_KEYS}}`. Fill via `str.replace` with keys sorted longest-first so prefixes don't collide.
- **AI meter:** put `active` on exactly one of `{{ACTIVE_IF_ASSISTIVE}}` / `{{ACTIVE_IF_EMBEDDED}}` / `{{ACTIVE_IF_AUTONOMOUS}}`; empty on the other two.
- **Language switcher:** `{{LANG_EN_HREF}}` / `{{LANG_ZH_HREF}}` = target filenames; `{{ACTIVE_IF_EN}}` / `{{ACTIVE_IF_ZH}}` = `active` on the file's own language.
- **Brand footer:** contains `TEARDOWN.` mark + LinkedIn / X / Xiaohongshu links. Do not remove.

---

## Use as a VS Code slash command

Copy [product-teardown-prompt.md](product-teardown-prompt.md) into your VS Code prompts folder as `product-teardown.prompt.md` and invoke via `/product-teardown <product name>`.

macOS: `~/Library/Application Support/Code/User/prompts/`

---

## How it thinks

- **A product is a system, not a screen.** The screen is what you see; the *loop* is what makes it work. The teardown always finds the loop first, then works outward to surfaces, business model, and moat.
- **JTBD beats persona.** "Who uses it" is less useful than "what did they hire it to *replace*." The interesting answer is almost never the obvious one.
- **AI readiness is a placement problem, not a checkbox.** Every AI feature sits somewhere on Assistive → Embedded → Autonomous. Naming the point is the analysis.
- **Opportunities must be actionable.** No "they should add AI." Every opportunity in §10 is a concrete wedge you could ship next quarter.

---

## Example output

Sample: Linear teardown — `product-teardown-linear-en-202607.html` + `-zh-` counterpart, cross-linked EN / ZH switcher, 6-image product tour, 11-section deep dive.

---

## License

MIT — fork it, remix it, ship your own version.

Created by [Dreameryanyan](https://www.linkedin.com/in/yanliudesign/) · [LinkedIn](https://www.linkedin.com/in/yanliudesign/) · [X](https://x.com/yanliudreamer) · [Xiaohongshu](https://www.xiaohongshu.com/user/profile/5b2afdf311be104ac3c22931)
