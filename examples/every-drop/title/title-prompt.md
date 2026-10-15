# 同案例的定制标题分支：仅提示词

调用：title-text-design → design-review（prompt / typography plan）。此分支不阻塞B/C/D的普通排字，也不输出虚构的标题资产路径。

准确标题：每滴有数。用途：横排科普片头标题，透明资产放在暖白底。只做一条“可数的水滴”方向；不新增备选或审批。中文单层，无英文和副标题。

骨架：清晰的现代中黑，保留开放内白与平直基线；不使用厚重标志、书法或3D结构。题材是日常用水，因此用便于阅读的字体底稿，而不是戏剧化笔势。

| 字 | 角色与主要结构 | 内白、符号和关系 | 不可改动 |
|---|---|---|---|
| 每 | 起始锚点；横向主笔稳定，轮廓略宽 | 保留内部间隙，与“滴”之间留足气口 | 不连接或删去辨识笔画 |
| 滴 | 主题承载；右部保持直立、三点水保留三笔节奏 | 三点水的笔端形成清晰的滴状收笔，主题只集中在此字 | 不把右部改成水瓶或把三点水改成一枚独立图标 |
| 有 | 呼吸与过渡；撇画自然引向右下，宽度略收 | 保持“月”部内白，基线稳定 | 不闭合内部两道间隙 |
| 数 | 收束；左右重量均衡，末捺形成温和收尾 | 不再加入水滴符号，避免主题过密 | 保留左右部件及关键点画 |

记忆点是“滴”的三点水在结构内形成可数的滴状收笔，必须在缩小后仍读作正确汉字；若生图无法稳定呈现，使用真实字体底稿或矢量修字。其他字不堆叠主题物件。

## 透明标题生成提示词（未执行）

Create a flat 2D Chinese title asset containing exactly “每滴有数”. Use a clear contemporary medium-bold Chinese skeleton, open counters, a stable baseline and calm horizontal rhythm. The first character is a slightly wider opening anchor. In the second character, preserve all three water-radical strokes and shape their terminals as readable drop-like ends; keep its right component upright and intact. The third character is slightly narrower, with its internal horizontal gaps open. The final character closes the title with balanced left/right weight and a calm terminal diagonal. Concentrate the water motif only in the water radical, integrated into the strokes. Use graphite lettering with a restrained muted-green treatment on that radical, flat print edges and generous safe padding. Native transparent background, no secondary text, no watermark. Keep every Chinese character correct and readable; no 3D extrusion or pasted object illustrations.

计划资产框：1400×360，四边至少80px留白，整体动画时作为一层；不需要逐字动画。上述尺寸是目标规格，实际文件存在后再测尺寸、可见内容范围与Alpha。没有生成或检查实际透明像素。

B/C/D本轮所用标题：preview.html内的普通可编辑文字，不是本分支的定制字形结果。将来采用本定制标题时，重新核对字形、素材留白和最终合成尺度。
