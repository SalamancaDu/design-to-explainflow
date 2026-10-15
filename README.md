<p align="center">
  <img src="assets/readme/cover.png" alt="design-to-explainflow：从信息设计到科普视频的 AI 创作工作流。串联版式、视觉素材、标题字、动效与质量审阅。" width="100%">
</p>

# design-to-explainflow｜科普视频工作流

**从信息设计到科普视频的 AI 创作工作流**

串联版式、视觉素材、标题字、动效与质量审阅，为视频剪辑提供清晰、准确、可复用的资产。

[开始使用](#开始使用) · [四条生产路线](#四条生产路线) · [五个-skill](#五个-skill) · [演示案例](#演示案例每滴有数) · [完整文档](#完整文档) · [English](README.en.md)

适合制作科普视频中的解释画面、信息图、片头字卡、章节卡与短时动效，也可用于封面和海报。你可以只完成一个阶段，也可以在已授权范围内连续制作到所需交付。

## 先把信息讲清楚

一个视频资产，往往要同时解决几个问题：观众先看哪里，图像表达什么，文字和数据是否准确，哪些内容应该运动，以及结果能否继续编辑。

本项目把这些判断拆成明确分工，再用统一的交接串起来：

**信息 → 版式 → 必要视觉素材 → 准确合成 → 按需动效 → 检查交付**

已有素材、确定的视觉方向与可用源文件可以直接继承。定制标题、素材生成和动效均按需求调用，无需每次走完所有环节。

## 四条生产路线

![四条路线：A 静态整图，B 可编辑静态合成，C 整帧动效，D 逐元素动效。选择依据是最终交付和所需控制范围。](assets/readme/routes.png)

| 路线 | 你要的结果 | 典型请求 | 关键交付 |
|---|---|---|---|
| **A · 静态整图** | 以氛围与构图为主的完整静帧 | “做一张无文字的水滴主题封面” | 检查后的整图；只要提示词时停在提示词 |
| **B · 可编辑静态合成** | 准确文字、数据与可替换元素 | “日期可改，图形严格对应数据” | 静态图与所需可编辑源文件 |
| **C · 整帧动效** | 让整张图片运动 | “已有整图做 6 秒缓慢推近” | 整帧动画的预览、成片或源文件，按请求交付 |
| **D · 逐元素动效** | 独立控制主体、文字或图形 | “按讲解顺序逐项强调图表” | 可控元素、静态合成、详细动作及所需动画产物 |

准确文字或数据需要可靠控制时选 **B**；整图内部元素需要独立运动时选 **D**。改日期不需要动画，整图推近不需要拆层。

→ [静态路线 A / B](docs/static-workflows.md) · [动效路线 C / D](docs/motion-workflows.md)

## 五个 Skill

| Skill | 核心问题 | 输出与交接 |
|---|---|---|
| [**layout-design**](skills/layout-design/SKILL.md) | 观众先看什么、再看什么？ | 信息层级、构图、安全区与生产路线 |
| [**image-style**](skills/image-style/SKILL.md) | 素材用什么视觉语言？ | 配色、光影、材质、参考角色与生成提示词 |
| [**title-text-design**](skills/title-text-design/SKILL.md) | 标题字形如何承载主题？ | 字体骨架、逐字结构、主题符号与标题资产方案 |
| [**motion-style**](skills/motion-style/SKILL.md) | 什么需要动，为什么，何时？ | 前期运动意图、详细动作、停留与实现交接 |
| [**design-review**](skills/design-review/SKILL.md) | 当前产物能否进入下一步？ | 有依据的问题、修复位置与质量判断 |

每个 Skill 都有独立入口和按需读取的参考文件。普通排字无需定制字形，普通创作也不自动触发独立审阅流程。

生图工具负责生成或编辑图像；合成与动画工具负责准确排版、实现和导出。本仓库提供这五个设计 Skill，工具本身需要在使用环境中可用。详见[调用索引](docs/skill-index.md)与[能力范围](docs/compatibility.md)。

## 怎样衔接，才不返工

- **视觉母版确定风格，真实合成稿验证信息。** 没有准确文字和数据的主视觉，不能替代最终版式检查。
- **先说明运动意图，再决定怎么拆层。** 只拆需要独立编辑或运动的部分；详细时序基于已成立的静态合成。
- **文字与数据保持准确。** 真实图表的长度、面积、位置和标签都依据数据绘制；示意图标明其性质。
- **透明资产检查实际像素与边缘。** 优先使用工具支持的原生透明输出，保留已选字形和主体结构。
- **质量条件与用户授权分别判断。** 保留用户指定的审阅节点，完整授权不额外变成多轮等待。

[分层与 manifest](docs/asset-handoff.md) 统一了坐标、路径和布局来源。manifest 默认是交接说明；只有项目实现了读取器，它才会成为程序输入。

## 演示案例：每滴有数

同一份简报，因交付要求不同，走向不同路线。

![每滴有数：可编辑静态合成。洗浴 40、厨房 30、洗衣 20、其他 10，合计 100；全部为演示数据，不代表真实用水统计。](examples/every-drop/B/static-export.svg)

| 分支 | 实际提供的内容 | 证据范围 |
|---|---|---|
| **A** | 水滴主题氛围图提示词 | 完成生成前交接，未生成图像 |
| **B** | 准确 SVG 静态图与可编辑 HTML 源 | 文字、总量与图形比例可检查 |
| **C** | 单个整帧对象的 6 秒无声推近 | 浏览器预览，无视频导出 |
| **D** | 8 秒无声逐项强调与元素交接 | 浏览器预览，无视频导出 |
| **标题分支** | “每滴有数”的字形方案与透明资产提示词 | 未生成定制标题图像 |

演示数据为自拟 **40 / 30 / 20 / 10**，页面始终标明其性质。这个案例展示路由选择、静态编辑和动效交接，不据此宣称真实统计、生图质量或成片导出已获验证。

→ [运行案例](examples/every-drop/README.md) · [输入简报](examples/every-drop/brief.md) · [查看源文件](examples/every-drop/preview.html) · [检查与限制](examples/every-drop/review.md)

## 开始使用

### 1. 直接作为项目上下文

下载仓库，在能读取本地文件的代理中打开项目，使用下面的请求。这样可以先体验流程，无需安装到全局目录。

```text
请阅读 docs/overview.md 和 docs/skill-index.md，
按当前需求读取 skills/ 中对应的 SKILL.md 与必要参考。

我要制作一张科普视频解释图，1920×1080。
准确内容：标题“每滴有数”；四项演示数据 40 / 30 / 20 / 10，合计 100。
请明确标注“演示数据 · 不代表真实用水统计”。
日期与文字需要可编辑，图形比例必须准确。
本轮只交付静态图和可编辑源文件，使用已有 HTML/SVG 能力。
```

预期选择 **B 可编辑静态合成**。完整的[常用提示词](docs/prompt-recipes.md)覆盖标题、分层、动效、局部修改和审阅。

### 2. 安装为常用 Skill

将 `skills/` 下的五个目录放进宿主支持的 Skill 目录。保留每个目录中的 `SKILL.md`、`references/` 与 `agents/`，并保持五个目录互为同级。

Codex 的具体安装位置、同名冲突处理及调用示例见[安装与使用](docs/getting-started.md)。其他代理需要自行验证工具与触发方式。

### 3. 运行无生成费用的演示

需要本机已有 Python 3.10+ 和现代浏览器。在仓库根目录执行：

```bash
python -m http.server 8000 --bind 127.0.0.1 --directory examples/every-drop
```

打开 **http://127.0.0.1:8000/preview.html**。可以切换 A / B / C / D、试改日期、播放与拖动时间。本例使用原生 HTML/SVG/JavaScript，不调用图像或视频生成服务。

## 完整文档

| 阅读目的 | 文档 |
|---|---|
| 理解生产系统 | [工作流总览](docs/overview.md) |
| 制作静态画面 | [A / B 静态路线](docs/static-workflows.md) |
| 制作动效资产 | [C / D 动效路线](docs/motion-workflows.md) |
| 定义素材与交接 | [分层资产与 manifest](docs/asset-handoff.md) |
| 选择和调用 Skill | [调用索引](docs/skill-index.md) |
| 选择版式、视觉和标题方向 | [风格菜单](docs/style-menu.md) |
| 直接开始一次创作 | [提示词与可选复盘模板](docs/prompt-recipes.md) |
| 安装与理解依赖 | [开始使用](docs/getting-started.md) · [能力范围](docs/compatibility.md) |

<details>
<summary>查看项目目录</summary>

```text
.
├── README.md / README.en.md
├── docs/                      工作流、交接、提示词与使用说明
├── skills/
│   ├── layout-design/
│   ├── image-style/
│   ├── title-text-design/
│   ├── motion-style/
│   └── design-review/
├── examples/every-drop/        可编辑静帧与浏览器动效演示
├── assets/readme/              README 图示与可编辑 SVG
├── scripts/check_project.py   仓库一致性检查
├── CONTRIBUTING.md
├── NOTICE.md
└── LICENSE
```

</details>

## 验证与参与

```bash
python scripts/check_project.py
python examples/every-drop/check_trial.py
```

第一个命令检查仓库引用、Skill 结构、JSON/SVG 和可移植性；第二个核对案例静态产物与已保存的浏览器观察，包含错误数据几何、元素 ID 与资产路径的反例。它们不重新驱动浏览器，也不执行生图、音频同步或视频编码。

改进方法见 [CONTRIBUTING.md](CONTRIBUTING.md)。公开版本以本仓库为维护入口，个人安装副本的更新需明确同步，避免多份规则各自漂移。

## 授权与来源

本项目采用 [MIT 许可证](LICENSE)，Copyright (c) 2026 [SalamancaDu](https://github.com/SalamancaDu)。允许使用、修改与再分发，保留版权和许可声明即可。来源与外部工具边界见 [NOTICE.md](NOTICE.md)。
