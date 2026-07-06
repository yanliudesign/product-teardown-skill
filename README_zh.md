<div align="center">

**中文** · [English](./README.md)

# 🔬 Product Teardown Skill · 产品拆解 Skill

---

**把任何产品当成一个系统去逆向工程 — 一键生成中英双语、可直接打印的 HTML 报告。**

[![License](https://img.shields.io/badge/LICENSE-MIT-4c8bf5?style=flat-square&labelColor=333)](./LICENSE)
[![Version](https://img.shields.io/badge/VERSION-1.0.0-2ea44f?style=flat-square&labelColor=333)]()
[![Stars](https://img.shields.io/github/stars/yanliudesign/product-teardown-skill?style=flat-square&label=STARS&color=e37f2c&labelColor=333)](https://github.com/yanliudesign/product-teardown-skill/stargazers)

[![Claude Code](https://img.shields.io/badge/Claude_Code-Skill-d97757?style=flat-square&labelColor=1a1a1a&logo=anthropic&logoColor=white)](https://claude.ai/code)
[![Codex](https://img.shields.io/badge/Codex-Skill-2ea44f?style=flat-square&labelColor=1a1a1a)]()
[![OpenCode](https://img.shields.io/badge/OpenCode-Skill-4c8bf5?style=flat-square&labelColor=1a1a1a)]()
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Skill-8b5cf6?style=flat-square&labelColor=1a1a1a)]()
[![Hermes](https://img.shields.io/badge/Hermes-Skill-e879a8?style=flat-square&labelColor=1a1a1a)]()

</div>

Principal-PM 级别的产品拆解 skill。指定任何一款产品（Linear / Notion / Cursor / Perplexity…），它会把这个产品当成一个**系统**逆向工程 —— 循环 / 战略 / 护城河 / 机会点 —— 并生成一份中英双语、可直接打印的 HTML 报告，内置产品截图画廊。**不是**"我用了这个 app 觉得挺好"式的体验测评，而是把产品的骨骼拆给你看：**它为什么赢、在哪里漏水、下一步该走哪里**。

---

## 整个 skill 只有 2 步

用任何模糊的话调用（"帮我拆解一下 Linear" / "teardown Notion" / "分析下 Cursor"）都会走同一条路径：

1. **对话内输出** —— 11 节完整拆解（产品快照 → 用户 & JTBD → 核心循环 → 架构 → UX 质量 → 商业模式 → 增长 → AI 就绪度 → 摩擦 → 机会 → PM 终评）。
2. **HTML 报告自动生成** —— 两份互相链接的单文件（EN + 中文，右下角一键切换），保存到 `~/Desktop/Claude skills/product-teardown-<slug>-{en,zh}-<yyyymm>.html`。打印优化（Cmd+P → 干净 PDF）。

---

## Teardown Report · 11 节报告框架

每一次运行都交付两份单文件 HTML 报告到 `~/Desktop/Claude skills/`。固定 11 节骨架 + 产品截图导览：

| # | 章节 | 回答什么 |
|---|------|----------|
| — | **Product Tour** | 6 张截图，来自产品官网自己的 `og:image` 营销素材。 |
| **1** | **产品快照** | 一句话定位 · 品类 · 阶段 · 定价 · 关键数字。 |
| **2** | **用户 & JTBD** | 谁在雇这个产品，为什么雇 —— 包括被它**替换掉**的那个方案。 |
| **3** | **核心循环** | 让产品成瘾（或不成瘾）的那个原子级用户循环。 |
| **4** | **架构** | 对象模型 · 界面 · 集成 · 哪些是 primitive、哪些是 feature。 |
| **5** | **UX 质量** | 招牌交互 · 延迟 · 信息密度 · 空状态。 |
| **6** | **商业模式** | 变现路径 · 单元经济 · 扩张策略（PLG / sales / hybrid）。 |
| **7** | **增长** | 获客循环 · 病毒路径 · 留存钩子 · 护城河。 |
| **8** | **AI 就绪度** | Assistive / Embedded / Autonomous —— 拿证据把它钉在光谱上。 |
| **9** | **摩擦** | 产品在哪里漏水 —— 冷启动 / 中段漏斗 / 高阶用户天花板。 |
| **10** | **机会** | 3–5 条具体的下一步下注（feature、wedge、相邻品类）。 |
| **11** | **PM 终评** | 一句话 —— Principal PM 会在内部文档上写的那一句。 |

报告打印优化（Cmd+P → 干净 PDF），右下角按钮一键切换 EN ↔ 中文。

---

## 5 条设计原则

1. **结构 > 观点。** 每一节回答一个具体问题，不写 "我觉得这个 app 怎么样怎么样"。
2. **循环 > feature。** 核心循环这一节是整份拆解的脊柱，feature 都是循环的下游。
3. **AI 位置是光谱不是徽章。** Assistive / Embedded / Autonomous —— 只能钉一个，且要给证据。
4. **截图必须来自产品自己。** 用 `og:image` 素材（`curl -s <url> | grep og:image` 一把抓），不用博客随便找的图。
5. **默认双语。** 每次拆解同一 run 同时产出 EN + 中文，互相链接，不是先英后中翻译出来的。

---

## 仓库内容

```
product-teardown-skill/
├── product-teardown-prompt.md              # 可移植 skill prompt（可粘进任何工具）
├── templates/
│   ├── product-teardown-template-en.html   # 英文报告模板
│   └── product-teardown-template-zh.html   # 中文报告模板（占位符与英文完全一致）
└── scripts/
    ├── fill_linear.py                      # 参考实现 —— 同时渲染两份模板
    └── translate_template_zh.py            # 一次性脚本：从英文模板派生中文模板
```

- **视觉：** 米色纸感 + 衬线标题 + 黄色 accent。打印优化。
- **占位符：** `{{ALL_CAPS_KEYS}}`。用 `str.replace` 填充；键按长度从长到短排序，避免前缀撞车。
- **AI 成熟度指示器：** 在 `{{ACTIVE_IF_ASSISTIVE}}` / `{{ACTIVE_IF_EMBEDDED}}` / `{{ACTIVE_IF_AUTONOMOUS}}` 三个中选一个填 `active`，其余留空。
- **语言切换按钮：** `{{LANG_EN_HREF}}` / `{{LANG_ZH_HREF}}` = 目标文件名；`{{ACTIVE_IF_EN}}` / `{{ACTIVE_IF_ZH}}` 只在自己所在语言的那份文件里设为 `active`。
- **品牌 footer：** 包含 `TEARDOWN.` mark + LinkedIn / X / 小红书 链接。不要删。

---

## 作为 VS Code slash command 使用

把 [product-teardown-prompt.md](product-teardown-prompt.md) 复制到 VS Code 的 prompts 目录并改名为 `product-teardown.prompt.md`，然后用 `/product-teardown <产品名>` 触发。

macOS 路径：`~/Library/Application Support/Code/User/prompts/`

---

## 设计思路

- **产品是一个系统，不是一屏界面。** 界面是你看到的，**循环**才是让它跑起来的东西。拆解永远先找到循环，再往外推到界面、商业模式、护城河。
- **JTBD 比 persona 更值钱。** "谁在用" 远不如 "他们**换掉了什么**" 有信息量。真正有意思的答案几乎从来不是显而易见的那个。
- **AI 就绪度是定位问题，不是打勾问题。** 每一个 AI feature 都落在 Assistive → Embedded → Autonomous 这条光谱的某个点上。**能把点钉准，就是分析本身。**
- **机会必须可执行。** 不接受 "他们应该加个 AI"。§10 里每一条机会都是下个季度能真的 ship 的具体 wedge。

---

## 示例输出

Linear 拆解样例 —— `product-teardown-linear-en-202607.html` + `-zh-` 对应版本，右下角 EN / 中文 互链切换，6 张产品截图导览，11 节深度拆解。

---

## License

MIT 协议 —— 随便 fork、改造、发一个你自己的版本。

Created by [Dreameryanyan](https://www.linkedin.com/in/yanliudesign/) · [LinkedIn](https://www.linkedin.com/in/yanliudesign/) · [X](https://x.com/yanliudreamer) · [小红书](https://www.xiaohongshu.com/user/profile/5b2afdf311be104ac3c22931)
