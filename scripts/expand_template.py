#!/usr/bin/env python3
"""One-shot template expansion: insert 4 new PM-analysis sections and renumber.

New sections:
  §5  Design Language & Craft Signals
  §8  Competitor Landscape
  §11 What Metrics They Actually Optimize For
  §13 Risk Matrix

Old numbering (11 sections) → new numbering (15 sections):
  §5  UX Quality       → §6
  §6  Business Model   → §7
  §7  Growth           → §9
  §8  AI Readiness     → §10
  §9  Friction         → §12
  §10 Opportunities    → §14
  §11 Final Verdict    → §15
"""
from pathlib import Path

TMPL_DIR = Path("/Users/yanliu/personal/product teardown/templates")

# ---------------- Shared CSS to inject before @media print ----------------
NEW_CSS = """  /* Craft signals */
  .craft-list { display: grid; gap: 12px; margin-top: 8px; }
  .craft-item { border: 1px solid var(--line); background: var(--paper-2); padding: 14px 18px; border-radius: 4px; display: grid; grid-template-columns: 42px 1fr; gap: 14px; align-items: start; }
  .craft-item .idx { font-family: var(--serif); font-style: italic; font-size: 22px; color: var(--muted); line-height: 1; padding-top: 2px; }
  .craft-item .name { font-family: var(--display); font-weight: 700; font-size: 14px; color: var(--ink); display: block; margin-bottom: 6px; }
  .craft-item .body { font-size: 13px; color: #2a2a26; line-height: 1.6; }

  /* Competitor + risk tables */
  .comp-wrap { overflow-x: auto; margin-bottom: 6px; }
  .comp-table, .risk-table { width: 100%; border-collapse: collapse; margin: 6px 0 12px; font-size: 12.5px; background: white; border: 1px solid var(--line); border-radius: 6px; overflow: hidden; }
  .comp-table th, .comp-table td, .risk-table th, .risk-table td { padding: 10px 12px; text-align: left; border-bottom: 1px solid var(--line-soft); vertical-align: top; line-height: 1.5; }
  .comp-table thead th, .risk-table thead th { background: var(--paper-2); font-size: 10.5px; letter-spacing: 0.08em; text-transform: uppercase; color: var(--muted); font-weight: 700; }
  .comp-table tbody th { font-weight: 700; color: var(--ink); background: var(--paper); font-size: 12.5px; text-transform: none; letter-spacing: 0; }
  .comp-table td.own { background: #fff8e6; font-weight: 600; color: var(--ink); }
  .comp-verdict { font-size: 13px; padding: 12px 16px; border-left: 3px solid var(--go); background: var(--go-soft); border-radius: 0 4px 4px 0; margin-top: 10px; line-height: 1.55; }
  .comp-verdict.warn { border-left-color: var(--stop); background: var(--stop-soft); }
  .risk-table td.sev-high { color: var(--stop); font-weight: 700; }
  .risk-table td.sev-med { color: var(--warn); font-weight: 700; }
  .risk-table td.sev-low { color: var(--go); font-weight: 700; }

  /* Metrics grid */
  .metrics-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; }
  .metric-card { background: white; border: 1px solid var(--line); border-radius: 6px; padding: 18px 20px; border-left: 3px solid var(--line); }
  .metric-card .tag { display: inline-block; font-size: 10px; letter-spacing: 0.14em; text-transform: uppercase; color: var(--muted); background: var(--paper-2); padding: 3px 9px; border-radius: 999px; margin-bottom: 10px; font-weight: 700; }
  .metric-card h5 { font-size: 14px; margin: 0 0 8px; font-weight: 700; line-height: 1.4; }
  .metric-card p { font-size: 12.5px; color: #2a2a26; line-height: 1.55; margin: 0; }
  .metric-card.north { border-left-color: var(--ink); }
  .metric-card.north .tag { background: var(--ink); color: var(--paper); }
  .metric-card.guard { border-left-color: var(--warn); }
  .metric-card.guard .tag { background: var(--warn-soft); color: var(--warn); }
  .metric-card.blind { border-left-color: var(--stop); }
  .metric-card.blind .tag { background: var(--stop-soft); color: var(--stop); }

"""

# ---------------- New section templates (chrome text varies by language) ----------------
def craft_section(title, pill):
    return f"""<!-- §5 CRAFT SIGNALS -->
<section id="s5">
  <div class="section-head">
    <span class="num">05</span>
    <h3>{title}</h3>
    <span class="pill">{pill}</span>
  </div>
  <p class="section-intro">{{{{CRAFT_PRINCIPLE}}}}</p>
  <div class="craft-list">
    <div class="craft-item"><div class="idx">01</div><div><span class="name">{{{{CRAFT_1_NAME}}}}</span><div class="body">{{{{CRAFT_1_DETAIL}}}}</div></div></div>
    <div class="craft-item"><div class="idx">02</div><div><span class="name">{{{{CRAFT_2_NAME}}}}</span><div class="body">{{{{CRAFT_2_DETAIL}}}}</div></div></div>
    <div class="craft-item"><div class="idx">03</div><div><span class="name">{{{{CRAFT_3_NAME}}}}</span><div class="body">{{{{CRAFT_3_DETAIL}}}}</div></div></div>
    <div class="craft-item"><div class="idx">04</div><div><span class="name">{{{{CRAFT_4_NAME}}}}</span><div class="body">{{{{CRAFT_4_DETAIL}}}}</div></div></div>
    <div class="craft-item"><div class="idx">05</div><div><span class="name">{{{{CRAFT_5_NAME}}}}</span><div class="body">{{{{CRAFT_5_DETAIL}}}}</div></div></div>
  </div>
</section>

"""


def comp_section(title, pill, dim_h, win_label, risk_label):
    return f"""<!-- §8 COMPETITOR LANDSCAPE -->
<section id="s8">
  <div class="section-head">
    <span class="num">08</span>
    <h3>{title}</h3>
    <span class="pill">{pill}</span>
  </div>
  <p class="section-intro">{{{{COMP_INTRO}}}}</p>
  <div class="comp-wrap">
    <table class="comp-table">
      <thead>
        <tr>
          <th>{dim_h}</th>
          <th>{{{{PRODUCT}}}}</th>
          <th>{{{{COMP_1_NAME}}}}</th>
          <th>{{{{COMP_2_NAME}}}}</th>
          <th>{{{{COMP_3_NAME}}}}</th>
          <th>{{{{COMP_4_NAME}}}}</th>
        </tr>
      </thead>
      <tbody>
        <tr><th>{{{{COMP_DIM_1}}}}</th><td class="own">{{{{COMP_OWN_D1}}}}</td><td>{{{{COMP_1_D1}}}}</td><td>{{{{COMP_2_D1}}}}</td><td>{{{{COMP_3_D1}}}}</td><td>{{{{COMP_4_D1}}}}</td></tr>
        <tr><th>{{{{COMP_DIM_2}}}}</th><td class="own">{{{{COMP_OWN_D2}}}}</td><td>{{{{COMP_1_D2}}}}</td><td>{{{{COMP_2_D2}}}}</td><td>{{{{COMP_3_D2}}}}</td><td>{{{{COMP_4_D2}}}}</td></tr>
        <tr><th>{{{{COMP_DIM_3}}}}</th><td class="own">{{{{COMP_OWN_D3}}}}</td><td>{{{{COMP_1_D3}}}}</td><td>{{{{COMP_2_D3}}}}</td><td>{{{{COMP_3_D3}}}}</td><td>{{{{COMP_4_D3}}}}</td></tr>
        <tr><th>{{{{COMP_DIM_4}}}}</th><td class="own">{{{{COMP_OWN_D4}}}}</td><td>{{{{COMP_1_D4}}}}</td><td>{{{{COMP_2_D4}}}}</td><td>{{{{COMP_3_D4}}}}</td><td>{{{{COMP_4_D4}}}}</td></tr>
      </tbody>
    </table>
  </div>
  <div class="comp-verdict"><strong>{win_label}:</strong> {{{{COMP_WHERE_OWN_WINS}}}}</div>
  <div class="comp-verdict warn"><strong>{risk_label}:</strong> {{{{COMP_WHERE_RIVALS_CATCH}}}}</div>
</section>

"""


def metrics_section(title, pill, north_tag, input_tag, guard_tag, blind_tag):
    return f"""<!-- §11 METRICS -->
<section id="s11">
  <div class="section-head">
    <span class="num">11</span>
    <h3>{title}</h3>
    <span class="pill">{pill}</span>
  </div>
  <p class="section-intro">{{{{METRICS_INTRO}}}}</p>
  <div class="metrics-grid">
    <div class="metric-card north">
      <span class="tag">{north_tag}</span>
      <h5>{{{{NORTH_STAR_METRIC}}}}</h5>
      <p>{{{{NORTH_STAR_WHY}}}}</p>
    </div>
    <div class="metric-card">
      <span class="tag">{input_tag} · 1</span>
      <h5>{{{{INPUT_METRIC_1_NAME}}}}</h5>
      <p>{{{{INPUT_METRIC_1_WHY}}}}</p>
    </div>
    <div class="metric-card">
      <span class="tag">{input_tag} · 2</span>
      <h5>{{{{INPUT_METRIC_2_NAME}}}}</h5>
      <p>{{{{INPUT_METRIC_2_WHY}}}}</p>
    </div>
    <div class="metric-card">
      <span class="tag">{input_tag} · 3</span>
      <h5>{{{{INPUT_METRIC_3_NAME}}}}</h5>
      <p>{{{{INPUT_METRIC_3_WHY}}}}</p>
    </div>
    <div class="metric-card guard">
      <span class="tag">{guard_tag}</span>
      <h5>{{{{GUARDRAIL_METRIC}}}}</h5>
      <p>{{{{GUARDRAIL_WHY}}}}</p>
    </div>
    <div class="metric-card blind">
      <span class="tag">{blind_tag}</span>
      <h5>{{{{METRIC_BLINDSPOT}}}}</h5>
      <p>{{{{METRIC_BLINDSPOT_WHY}}}}</p>
    </div>
  </div>
</section>

"""


def risk_section(title, pill, risk_h, cat_h, sev_h, lik_h, mit_h):
    return f"""<!-- §13 RISK MATRIX -->
<section id="s13">
  <div class="section-head">
    <span class="num">13</span>
    <h3>{title}</h3>
    <span class="pill">{pill}</span>
  </div>
  <p class="section-intro">{{{{RISK_INTRO}}}}</p>
  <table class="risk-table">
    <thead>
      <tr><th>{risk_h}</th><th>{cat_h}</th><th>{sev_h}</th><th>{lik_h}</th><th>{mit_h}</th></tr>
    </thead>
    <tbody>
      <tr><td><strong>{{{{RISK_1_NAME}}}}</strong></td><td>{{{{RISK_1_CAT}}}}</td><td class="sev-{{{{RISK_1_SEV_CLASS}}}}">{{{{RISK_1_SEV}}}}</td><td>{{{{RISK_1_LIK}}}}</td><td>{{{{RISK_1_MIT}}}}</td></tr>
      <tr><td><strong>{{{{RISK_2_NAME}}}}</strong></td><td>{{{{RISK_2_CAT}}}}</td><td class="sev-{{{{RISK_2_SEV_CLASS}}}}">{{{{RISK_2_SEV}}}}</td><td>{{{{RISK_2_LIK}}}}</td><td>{{{{RISK_2_MIT}}}}</td></tr>
      <tr><td><strong>{{{{RISK_3_NAME}}}}</strong></td><td>{{{{RISK_3_CAT}}}}</td><td class="sev-{{{{RISK_3_SEV_CLASS}}}}">{{{{RISK_3_SEV}}}}</td><td>{{{{RISK_3_LIK}}}}</td><td>{{{{RISK_3_MIT}}}}</td></tr>
      <tr><td><strong>{{{{RISK_4_NAME}}}}</strong></td><td>{{{{RISK_4_CAT}}}}</td><td class="sev-{{{{RISK_4_SEV_CLASS}}}}">{{{{RISK_4_SEV}}}}</td><td>{{{{RISK_4_LIK}}}}</td><td>{{{{RISK_4_MIT}}}}</td></tr>
    </tbody>
  </table>
</section>

"""


# ---------------- Language-specific TOC / footer ----------------
EN_TOC = """<nav class="toc">
  <span class="kicker">Inside</span>
  <ol>
    <li><a href="#tldr">Verdict · TL;DR</a></li>
    <li><a href="#metrics">Key Signals</a></li>
    <li><a href="#s1">1. Product Snapshot</a></li>
    <li><a href="#gallery">· Product Tour</a></li>
    <li><a href="#s2">2. Users & JTBD</a></li>
    <li><a href="#s3">3. Core Product Loop</a></li>
    <li><a href="#s4">4. Architecture & UX System</a></li>
    <li><a href="#s5">5. Design Language & Craft</a></li>
    <li><a href="#s6">6. Value Delivery & UX Quality</a></li>
    <li><a href="#s7">7. Business Model</a></li>
    <li><a href="#s8">8. Competitor Landscape</a></li>
    <li><a href="#s9">9. Growth Strategy</a></li>
    <li><a href="#s10">10. AI / Future Readiness</a></li>
    <li><a href="#s11">11. Metrics They Optimize For</a></li>
    <li><a href="#s12">12. Friction & Weaknesses</a></li>
    <li><a href="#s13">13. Risk Matrix</a></li>
    <li><a href="#s14">14. Opportunities & Redesign</a></li>
    <li><a href="#s15">15. Final PM Verdict</a></li>
  </ol>
</nav>"""

ZH_TOC = """<nav class="toc">
  <span class="kicker">目录</span>
  <ol>
    <li><a href="#tldr">核心结论 · TL;DR</a></li>
    <li><a href="#metrics">关键信号</a></li>
    <li><a href="#s1">1. 产品快照</a></li>
    <li><a href="#gallery">· 产品截图</a></li>
    <li><a href="#s2">2. 目标用户 & JTBD</a></li>
    <li><a href="#s3">3. 核心产品循环</a></li>
    <li><a href="#s4">4. 架构 & 交互体系</a></li>
    <li><a href="#s5">5. 设计语言 & 手艺细节</a></li>
    <li><a href="#s6">6. 价值交付 & 体验质感</a></li>
    <li><a href="#s7">7. 商业模式</a></li>
    <li><a href="#s8">8. 竞品全景 & 定位</a></li>
    <li><a href="#s9">9. 增长策略</a></li>
    <li><a href="#s10">10. AI · 未来就绪度</a></li>
    <li><a href="#s11">11. 他们真正在优化的指标</a></li>
    <li><a href="#s12">12. 摩擦 & 短板</a></li>
    <li><a href="#s13">13. 风险矩阵</a></li>
    <li><a href="#s14">14. 机会 & 重设计</a></li>
    <li><a href="#s15">15. 终局判断</a></li>
  </ol>
</nav>"""


EN_FOOTER_NEW = "Structured per the 15-section teardown framework (Snapshot → JTBD → Loop → Architecture → Craft → UX → Business → Competitors → Growth → AI → Metrics → Friction → Risks → Opportunities → Verdict)."
ZH_FOOTER_NEW = "按 15 节拆解框架构造（快照 → JTBD → 循环 → 架构 → 手艺 → 体验 → 商业 → 竞品 → 增长 → AI → 指标 → 摩擦 → 风险 → 机会 → 终局）。"


CONFIG = {
    "en": {
        "path": TMPL_DIR / "product-teardown-template-en.html",
        "toc_old_kicker": "Inside",
        "toc_new": EN_TOC,
        "footer_old": "Structured per the 11-section teardown framework (Snapshot → JTBD → Loop → Architecture → UX → Business → Growth → AI → Friction → Opportunities → Verdict).",
        "footer_new": EN_FOOTER_NEW,
        "sections_to_renumber": [
            # (old_n, new_n, title_in_h3)
            (5, 6, "Value Delivery & UX Quality"),
            (6, 7, "Business Model & Monetization"),
            (7, 9, "Growth Strategy"),
            (8, 10, "AI / Future Readiness"),
            (9, 12, "Friction & Weaknesses"),
            (10, 14, "Opportunities & Redesign Ideas"),
            (11, 15, "Final PM Verdict"),
        ],
        "old_section_comments": {
            5: "<!-- §5 UX QUALITY -->",
            6: "<!-- §6 BUSINESS MODEL -->",
            7: "<!-- §7 GROWTH -->",
            8: "<!-- §8 AI READINESS -->",
            9: "<!-- §9 FRICTION & WEAKNESSES -->",
            10: "<!-- §10 OPPORTUNITIES -->",
            11: "<!-- §11 FINAL VERDICT -->",
        },
        "new_section_comments": {
            5: "<!-- §6 UX QUALITY -->",
            6: "<!-- §7 BUSINESS MODEL -->",
            7: "<!-- §9 GROWTH -->",
            8: "<!-- §10 AI READINESS -->",
            9: "<!-- §12 FRICTION & WEAKNESSES -->",
            10: "<!-- §14 OPPORTUNITIES -->",
            11: "<!-- §15 FINAL VERDICT -->",
        },
        "craft": craft_section("Design Language & Craft Signals", "What craft actually means"),
        "comp": comp_section(
            "Competitor Landscape",
            "Positioning matrix",
            "Dimension",
            "Where the product wins",
            "Where rivals are catching up",
        ),
        "metrics": metrics_section(
            "What Metrics They Actually Optimize For",
            "[Inferred] north-star + guardrails",
            "North Star", "Input metric", "Guardrail", "Blindspot",
        ),
        "risk": risk_section(
            "Risk Matrix",
            "Severity × Likelihood",
            "Risk", "Category", "Severity", "Likelihood", "Mitigation",
        ),
    },
    "zh": {
        "path": TMPL_DIR / "product-teardown-template-zh.html",
        "toc_new": ZH_TOC,
        "footer_old": "按 11 节拆解框架构造（快照 → JTBD → 循环 → 架构 → 体验 → 商业 → 增长 → AI → 摩擦 → 机会 → 终局）。",
        "footer_new": ZH_FOOTER_NEW,
        "sections_to_renumber": [
            (5, 6, "价值交付 & 体验质感"),
            (6, 7, "商业模式 & 变现"),
            (7, 9, "增长策略"),
            (8, 10, "AI · 未来就绪度"),
            (9, 12, "摩擦 & 短板"),
            (10, 14, "机会 & 重设计"),
            (11, 15, "终局判断"),
        ],
        "old_section_comments": {
            5: "<!-- §5 UX QUALITY -->",
            6: "<!-- §6 BUSINESS MODEL -->",
            7: "<!-- §7 GROWTH -->",
            8: "<!-- §8 AI READINESS -->",
            9: "<!-- §9 FRICTION & WEAKNESSES -->",
            10: "<!-- §10 OPPORTUNITIES -->",
            11: "<!-- §11 FINAL VERDICT -->",
        },
        "new_section_comments": {
            5: "<!-- §6 UX QUALITY -->",
            6: "<!-- §7 BUSINESS MODEL -->",
            7: "<!-- §9 GROWTH -->",
            8: "<!-- §10 AI READINESS -->",
            9: "<!-- §12 FRICTION & WEAKNESSES -->",
            10: "<!-- §14 OPPORTUNITIES -->",
            11: "<!-- §15 FINAL VERDICT -->",
        },
        "craft": craft_section("设计语言 & 手艺细节", "「品味」到底体现在哪"),
        "comp": comp_section(
            "竞品全景 & 定位对比",
            "定位矩阵",
            "维度",
            "本产品的赢面",
            "竞品正在追平的地方",
        ),
        "metrics": metrics_section(
            "他们真正在优化什么指标",
            "[推断] 北极星 + 护栏",
            "北极星", "输入指标", "护栏指标", "盲区",
        ),
        "risk": risk_section(
            "风险矩阵",
            "严重程度 × 发生概率",
            "风险", "类别", "严重程度", "发生概率", "缓解方案",
        ),
    },
}


def transform(cfg):
    path = cfg["path"]
    html = path.read_text(encoding="utf-8")
    original_len = len(html)

    # 1. Inject new CSS before @media print
    print_anchor = "  @media print {"
    assert print_anchor in html, "print media query not found"
    html = html.replace(print_anchor, NEW_CSS + print_anchor, 1)

    # 2. Add new selectors to print break-inside list
    old_break = ".ux-bar, .jtbd-row {\n      break-inside: avoid; page-break-inside: avoid;\n    }"
    new_break = ".ux-bar, .jtbd-row, .craft-item, .metric-card, .comp-wrap, .risk-table {\n      break-inside: avoid; page-break-inside: avoid;\n    }"
    assert old_break in html, "print break-inside block not found"
    html = html.replace(old_break, new_break, 1)

    # 3. Add .metrics-grid to mobile 1fr collapse
    old_mobile = ".verdict, .numbers, .info-grid, .biz-grid, .surface-grid, .growth-cols, .ai-meter, .final { grid-template-columns: 1fr; }"
    new_mobile = ".verdict, .numbers, .info-grid, .biz-grid, .surface-grid, .growth-cols, .ai-meter, .final, .metrics-grid { grid-template-columns: 1fr; }"
    assert old_mobile in html, "mobile 1fr rule not found"
    html = html.replace(old_mobile, new_mobile, 1)

    # 4. Replace TOC (find full <nav class="toc">...</nav> block by matching pattern)
    import re
    toc_pattern = re.compile(r'<nav class="toc">.*?</nav>', re.DOTALL)
    assert toc_pattern.search(html), "TOC block not found"
    html = toc_pattern.sub(cfg["toc_new"], html, count=1)

    # 5. Update footer description
    assert cfg["footer_old"] in html, f"footer old not found: {cfg['footer_old'][:50]}"
    html = html.replace(cfg["footer_old"], cfg["footer_new"], 1)

    # 6. Renumber existing sections. Match the 4-line block:
    #    <!-- §OLD NAME -->
    #    <section id="sOLD">
    #      <div class="section-head">
    #        <span class="num">NN_OLD</span>
    for old_n, new_n, _title in cfg["sections_to_renumber"]:
        old_comment = cfg["old_section_comments"][old_n]
        new_comment = cfg["new_section_comments"][old_n]  # keyed by old_n

        old_block = f'{old_comment}\n<section id="s{old_n}">\n  <div class="section-head">\n    <span class="num">{old_n:02d}</span>'
        new_block = f'{new_comment}\n<section id="s{new_n}">\n  <div class="section-head">\n    <span class="num">{new_n:02d}</span>'
        assert old_block in html, f"renumber anchor not found for §{old_n}"
        html = html.replace(old_block, new_block, 1)

    # 7. Insert new sections in reverse order (so earlier anchors don't shift)
    # Anchors are the NEW comment strings after renumber
    insertions = [
        (cfg["new_section_comments"][10], cfg["risk"]),      # §13 before §14 Opportunities
        (cfg["new_section_comments"][9],  cfg["metrics"]),   # §11 before §12 Friction
        (cfg["new_section_comments"][7],  cfg["comp"]),      # §8 before §9 Growth
        (cfg["new_section_comments"][5],  cfg["craft"]),     # §5 before §6 UX
    ]
    for anchor, block in insertions:
        assert anchor in html, f"insert anchor not found: {anchor}"
        html = html.replace(anchor, block + anchor, 1)

    path.write_text(html, encoding="utf-8")
    print(f"Wrote {path.name}: {original_len} → {len(html)} bytes")


if __name__ == "__main__":
    for lang, cfg in CONFIG.items():
        transform(cfg)
    print("Done.")
