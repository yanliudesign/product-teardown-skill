# Product Teardown Skill

A Principal-PM-level product-teardown skill that reverse-engineers any product as a system — loops, strategy, moat, opportunities — and renders the analysis as a bilingual (EN + 中文), print-ready HTML report with an embedded product-screenshot gallery.

**Two-step flow:**
1. Chat response: full teardown in 11 sections (Snapshot → Users & JTBD → Core Loop → Architecture → UX Quality → Business Model → Growth → AI Readiness → Friction → Opportunities → Final PM Verdict).
2. HTML report: two cross-linked files (EN + 中文, toggle in the bottom-right), saved to `~/Desktop/Claude skills/`.

## Repo contents

- [product-teardown-prompt.md](product-teardown-prompt.md) — the portable skill prompt (paste into ChatGPT, Claude, or any tool).
- [templates/product-teardown-template-en.html](templates/product-teardown-template-en.html) — English report template.
- [templates/product-teardown-template-zh.html](templates/product-teardown-template-zh.html) — Chinese report template. Same `{{PLACEHOLDER}}` set, translated chrome.
- [scripts/fill_linear.py](scripts/fill_linear.py) — reference implementation. Renders both templates from parallel `V_EN` / `V_ZH` dicts, cross-links the language switcher, opens the EN version.
- [scripts/translate_template_zh.py](scripts/translate_template_zh.py) — one-shot script that produced the ZH template from the EN one.

## Design notes

- **Aesthetic:** cream paper + serif display + yellow accent. Print-optimized (Cmd+P → clean PDF).
- **Placeholders:** `{{ALL_CAPS_KEYS}}`. Fill via `str.replace` with keys sorted longest-first so prefixes don't collide.
- **Product Tour gallery:** 6 screenshots from the product's `og:image` marketing assets — grab via `curl -s <url> | grep og:image`.
- **AI meter:** put `active` on exactly one of `{{ACTIVE_IF_ASSISTIVE}}` / `{{ACTIVE_IF_EMBEDDED}}` / `{{ACTIVE_IF_AUTONOMOUS}}`; empty on the other two.
- **Language switcher:** `{{LANG_EN_HREF}}` / `{{LANG_ZH_HREF}}` = target filenames; `{{ACTIVE_IF_EN}}` / `{{ACTIVE_IF_ZH}}` = `active` on the file's own language.
- **Brand footer:** contains `TEARDOWN.` mark + LinkedIn / X / Xiaohongshu links. Do not remove.

## Use as a VS Code slash command

Copy [product-teardown-prompt.md](product-teardown-prompt.md) into your VS Code prompts folder as `product-teardown.prompt.md` and invoke via `/product-teardown <product name>`.

macOS: `~/Library/Application Support/Code/User/prompts/`

## Example output

Sample: Linear teardown — [`product-teardown-linear-en-202607.html`] + `-zh-` counterpart, cross-linked EN / 中文 switcher, 6-image product tour, 11-section deep dive.

---

Built by [Yan Liu](https://yanliudesign.live) · [X](https://x.com/yanliudreamer) · [LinkedIn](https://www.linkedin.com/in/yanliudreamer/)
