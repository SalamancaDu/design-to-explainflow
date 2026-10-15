# 风格菜单

菜单提供选择维度，具体方向由主题、受众、媒介和参考决定。通常确定一个主版式、一种主视觉语言和必要标题方向；素材用途与文件格式单独选择。用户已有明确方向时直接继承。

## 版式结构

对应 [layout-patterns.md](../skills/layout-design/references/layout-patterns.md)，按标题名称查找。

| 菜单名 | 对应模式 | 适合场景 |
|---|---|---|
| 日式留白型 | Quiet center with large negative space | 人物、纪录片、克制封面 |
| 强数字主视觉型 | Type as image + 有序辅助信息 | 数字本身是主信息；真实图形仍按数据绘制 |
| 杂志封面型 | Asymmetric subject / Full-bleed image with text reserve | 人物、专题、商业叙事 |
| 左右对照型 | Split field | 两条路线、前后变化 |
| 对角动势型 | Diagonal momentum | 冲突、方向和趋势 |
| 中心主视觉型 | Quiet center | 单一观点、产品或符号 |
| 路线 / 时间线型 | Geometric point-line-plane system | 历史、地理、流程、事件演进 |
| 信息图框架型 | Repeated modules / Geometric point-line-plane system | 结构化解释、知识卡、报告图 |
| 极简标题卡型 | Motion title-card layout（静态也可用） | 章节卡、片头、观点停顿 |
| 数据标签分层型 | Small image as guide / Repeated modules | 信息较多但需有序呈现 |

## 图片视觉方向

对应 [visual-directions.md](../skills/image-style/references/visual-directions.md)；具体色彩、光影和纹理见 [color-light-texture.md](../skills/image-style/references/color-light-texture.md)。

| 菜单名 / 常用别名 | 对应方向 | 使用重点 |
|---|---|---|
| 财经杂志感 | Editorial finance restraint | 编辑式层级、有限配色、可信的视觉表达 |
| 日式留白 / 留白插画感 | Japanese white-space editorial | 非对称、低密度、明确留白用途 |
| 手作拼贴 / 纸张颗粒感 | Handmade explainer collage | 纸片、手绘痕迹、受控的不规则 |
| 冷峻纪录片档案感 / 科考资料感 | Documentary archive mood | 文档、地图和档案气氛；不伪造真实证据 |
| 低饱和数据图感 | Minimal data clarity | 清楚的图形与标签，真实几何依据数据 |
| 高对比海报感 | High-contrast symbolic poster | 单一强符号、尺度对比、清晰轮廓 |
| 柔和系统插画感 | Soft illustrated systems | 用简洁插画解释抽象系统 |
| 低饱和报纸网点拼贴风 | Low-saturation newspaper halftone collage | 网点、剪报、低饱和人物和物件 |

“高级克制单色”是可叠加的配色约束，不单独替代视觉方向。“测绘感”需说明线条、标注和纹理的具体作用；准确路线仍由可编辑图形绘制。

## 标题文字方向

对应 [title-text-system.md](../skills/title-text-design/references/title-text-system.md) 的字体基底与主题符号方法。这里只选方向，实际定制标题仍需确定骨架、字形结构与可读性。

| 方向 | 适合场景 / 方法对应 |
|---|---|
| 现代片名手写体 | 人物、旅行、情绪标题；现代片名手写基底 |
| 飞白干刷标题 | 历史、冲突、强情绪；笔势先于飞白材质 |
| 方重黑主标题 | 财经、数据、现实观点；宽扁重黑基底 |
| 宽扁压缩标题 | 海报、体育、商业标题；明确宽高和字距 |
| 宋 / 明式标题 | 人文、历史、东方叙事；宋体或碑刻方向 |
| 档案打字机 / 编号感 | 案例、调查；准确副标题或编号层级 |
| 票据印章 / 标签感 | 案例拆解、票据；复古招牌或票券结构 |
| 测绘线框标题 | 地理、工程；主题符号进入字形结构 |
| 纸张拼贴标题 | 人物、历史；字体骨架与拼贴材质分别确定 |
| 冷峻纪录片标题 | 严肃叙事的语气，不是固定字体；按主题选择基底 |

## 素材角色与输出形式

- 素材角色：背景氛围图、独立主体、定制标题、位图装饰、准确数据图形、完整合成图。
- 输出形式：普通位图、原生透明 PNG、可编辑文字或 SVG、静态导出、动画源文件、成片；按实际工具能力和交付要求选择。
- 透明 PNG 是输出形式，不定义审美风格；背景氛围图是用途，仍需指定其视觉方向。

## 调用示例

~~~text
使用 layout-design，主版式为“强数字主视觉型”。
使用 image-style，主视觉方向为“财经杂志感”，配色采用克制单色加一个主题强调色。
素材角色：背景与一个独立主体；输出：透明主体、可编辑数字及最终静态合成图。
标题只有在需要定制字形时使用 title-text-design，并按当前主题选择骨架。
~~~
