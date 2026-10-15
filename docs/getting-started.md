# 安装与使用

## 先决定怎么使用

- **只想读方法或试一次**：直接读取 `docs/overview.md` 和所需 Skill 文件。无需全局安装。
- **经常在代理中调用**：安装五个 Skill 目录，保留其相对结构。
- **只想看案例**：运行下文的本地 HTTP 服务；不需要模型服务或 API 密钥。

Skill 是指令与参考文件。它不会为宿主添加生图、浏览器、文件、音频或视频导出能力。

## 在 Codex 中安装

按 [OpenAI 当前 Skill 文档](https://developers.openai.com/codex/skills/)，项目级目录是 `.agents/skills/`，用户级目录是 `~/.agents/skills/`。先确认当前环境支持的位置；不要同时安装到多个目录造成同名重复。

手动复制本仓库 `skills/` 下的五个目录到选定位置：

```text
.agents/skills/
├── layout-design/
├── image-style/
├── title-text-design/
├── motion-style/
└── design-review/
```

五个目录中的 `SKILL.md`、`references/` 和 `agents/openai.yaml` 都需保留。部分参考通过相对路径引用同级 Skill，建议先安装完整五个目录。

已有同名目录时，先比较并保留本地修改，不直接覆盖。更新以本仓库为公开维护源，明确同步安装副本；不要把插件缓存当作持久修改位置。

安装后检查宿主是否发现各 Skill；若列表未更新，按宿主说明刷新或重启。可显式调用：

```text
$layout-design 请为这张科普解释图规划信息层级。
准确文案和数据如下……最终需要可编辑静态图。
```

各 `openai.yaml` 保留原有调用策略；显式使用 Skill 不表示授权任何付费或外部发布动作。

## 在其他代理中使用

可把对应 `SKILL.md` 与需要的参考文件作为上下文，但要核对该环境的目录规则、工具名、文件读取能力和自动触发方式。`agents/openai.yaml` 是 Codex 元数据，不能据此宣称其他平台已兼容。

图像工具不同，保留视觉、准确性与交接要求；具体参数按实际工具能力转换。更多说明见[能力与兼容范围](compatibility.md)。

## 提供一次完整输入

按实际任务给出已有内容即可，不必机械填满模板：

1. 用途、受众、比例或尺寸。
2. 准确文案、数据依据、可改写范围。
3. 已有素材与参考图各自的用途。
4. 哪些文字、数字或元素需要独立修改或运动。
5. 交付到提示词、静态图、动画预览还是成片；是否需要源文件。
6. 动效的声音模式：已有音频、明确无声或等待配音。
7. 用户明确保留的选择和审阅节点。

可直接改用[提示词模板](prompt-recipes.md)。

## 运行演示

在仓库根目录，用本机已有 Python 3.10+ 执行：

```bash
python -m http.server 8000 --bind 127.0.0.1 --directory examples/every-drop
```

打开 `http://127.0.0.1:8000/preview.html`，结束后在终端按 Ctrl+C 停止服务。该服务只用于本机预览。

运行静态检查：

```bash
python scripts/check_project.py
python examples/every-drop/check_trial.py
```

案例里的日期输入只改变当前页面，不保存到磁盘。长期修改请编辑 `examples/every-drop/preview.html` 的布局源，并同步其静态导出和受影响的 manifest。详情见[案例说明](../examples/every-drop/README.md)。
