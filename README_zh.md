# Product Teardown Skill

> [English](README.md) · **中文**

Principal-PM 级别的产品拆解 skill：把任何产品当成一个系统去逆向工程 — 循环 / 战略 / 护城河 / 机会点 — 并生成一份中英双语、可直接打印的 HTML 报告，内置产品截图画廊。

**两步流程：**
1. 对话内输出：11 节完整拆解（产品快照 → 用户 & JTBD → 核心循环 → 架构 → UX 质量 → 商业模式 → 增长 → AI 就绪度 → 摩擦 → 机会 → PM 终评）。
2. HTML 报告：EN + 中文 两份互相链接的文件（右下角一键切换语言），保存到 `~/Desktop/Claude skills/`。

## 仓库内容

- [product-teardown-prompt.md](product-teardown-prompt.md) — 可移植的 skill prompt（可粘进 ChatGPT / Claude / 任何工具）。
- [templates/product-teardown-template-en.html](templates/product-teardown-template-en.html) — 英文报告模板。
- [templates/product-teardown-template-zh.html](templates/product-teardown-template-zh.html) — 中文报告模板。占位符集合与英文完全一致，只是 UI 文本翻译过。
- [scripts/fill_linear.py](scripts/fill_linear.py) — 参考实现。用平行的 `V_EN` / `V_ZH` 字典渲染两份模板，互相链接语言切换按钮，自动打开英文版。
- [scripts/translate_template_zh.py](scripts/translate_template_zh.py) — 一次性脚本：从英文模板派生出中文模板。

## 设计要点

- **视觉：** 米色纸感 + 衬线标题 + 黄色 accent。打印优化（Cmd+P → 干净 PDF）。
- **占位符：** `{{ALL_CAPS_KEYS}}`。用 `str.replace` 填充；键按长度从长到短排序，避免前缀撞车。
- **产品截图画廊：** 6 张截图，来自产品官网的 `og:image` 素材 —  `curl -s <url> | grep og:image` 一把抓。
- **AI 成熟度指示器：** 在 `{{ACTIVE_IF_ASSISTIVE}}` / `{{ACTIVE_IF_EMBEDDED}}` / `{{ACTIVE_IF_AUTONOMOUS}}` 三个中选一个填 `active`，其余留空。
- **语言切换按钮：** `{{LANG_EN_HREF}}` / `{{LANG_ZH_HREF}}` = 目标文件名；`{{ACTIVE_IF_EN}}` / `{{ACTIVE_IF_ZH}}` 只在自己所在语言的那份文件里设为 `active`。
- **品牌 footer：** 包含 `TEARDOWN.` mark + LinkedIn / X / 小红书 链接。不要删。

## 作为 VS Code slash command 使用

把 [product-teardown-prompt.md](product-teardown-prompt.md) 复制到 VS Code 的 prompts 目录并改名为 `product-teardown.prompt.md`，然后用 `/product-teardown <产品名>` 触发。

macOS 路径：`~/Library/Application Support/Code/User/prompts/`

## 示例输出

Linear 拆解样例 —— `product-teardown-linear-en-202607.html` + `-zh-` 对应版本，右下角 EN / 中文 互链切换，6 张产品截图导览，11 节深度拆解。

---

作者：[Yan Liu](https://yanliudesign.live) · [LinkedIn](https://www.linkedin.com/in/yanliudesign/) · [X](https://x.com/yanliudreamer) · [小红书 · Dreameryanyan](https://www.xiaohongshu.com/user/profile/5b2afdf311be104ac3c22931)
