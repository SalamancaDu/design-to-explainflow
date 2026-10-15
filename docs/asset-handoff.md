# 分层资产与 manifest 模板

分层用于独立编辑、动画或复用。scene.manifest.json 默认是人和代理之间的交接说明，不是 HyperFrames 原生输入，也不假定已有自动读取器。简单项目可使用等价定位说明。

## 资产职责

| 文件或内容 | 用途 | 约束 |
|---|---|---|
| master-frame-preview.png | 确定视觉方向的母版 | 建立色彩、光影、镜头、材质和主视觉比例；可复用已有母版 |
| background.png | 背景 | 为真实文字与图形保留空间；需要移动主体时补全其后方背景 |
| subject.png | 需独立控制的主体 | 与背景共享光线和透视；按运动需要分离投影、部件或遮挡层 |
| decorations.png 或独立装饰文件 | 必要位图装饰 | 只有共同运动的内容才合并；准确连线、箭头和数据关系优先可编辑图形 |
| 标题字资产（按需） | 定制标题字形 | 核对准确字符与透明边缘，保存源文本；普通正文直接排版 |
| composite-preview.png | 含真实文字、数据与素材的合成静帧 | 据此检查最终构图，不能只凭单层或视觉母版判断 |

透明输出检查实际 Alpha、正常与放大视图、目标背景上的边缘和安全留白。色键去底仅在选用工具不支持原生透明或实际结果需要替代方法时使用。

## run 目录

需要保存多份产物或复用时使用；沿用项目现有目录也可以。只创建实际需要的文件。

~~~text
runs/YYYY-MM-DD_project-name/
├─ brief.md
├─ layout.md
├─ image-style.md
├─ assets/
│  ├─ source/
│  ├─ bitmap/
│  └─ fonts/
├─ scenes/
│  └─ s01/
│     ├─ scene.manifest.json
│     ├─ motion-brief.md
│     ├─ composite-preview.png
│     └─ hyperframes/
│        └─ index.html
├─ exports/
└─ review.md
~~~

片段使用 s01、s02 等独立目录或项目已有唯一编号；修订保留需要回退的已选版本，避免同日同项目覆盖。静态或局部修改不强制创建上述整套目录。

## 坐标、路径与权威来源

- 本模板使用画布像素，原点在左上，x 向右、y 向下；x/y 始终表示元素布局框的左上角，width/height 表示其尺寸。
- anchor 仅表示缩放、旋转等变换的原点，不改变 x/y 的含义。支持 top-left、center、left-center 等明确位置。
- 所有文件路径都相对 manifest 所在目录解析。写入 HTML 的 src 时，先定位实际文件，再换算成相对该 HTML 的路径；不能直接照抄 manifest 的 file。
- layoutSource 指向最终布局源文件。默认由该文件中的 HTML/CSS、SVG 或设计文档维护布局；manifest 是交接快照，布局修改后同步对应字段。
- 若某项目已有 manifest 驱动的生成器，明确声明其为权威来源并使用该生成器的结构约定，避免再手工维护两套布局。
- 旧 manifest 未声明坐标含义或使用其他锚点约定时，先结合原实现确认，不直接按新模板解释历史坐标。

## manifest 基础模板

以下文字、数值、字体和路径均为结构示例，不是实际业务数据或已存在的资产。

~~~json
{
  "schemaVersion": 1,
  "purpose": "handoff",
  "layoutSource": "hyperframes/index.html",
  "coordinateSpace": "canvas-px",
  "positionOrigin": "top-left",
  "pathBase": "manifest-directory",
  "canvas": {"width": 1920, "height": 1080},
  "elements": [
    {
      "id": "background",
      "type": "bitmap",
      "file": "../../assets/bitmap/background.png",
      "x": 0, "y": 0, "width": 1920, "height": 1080,
      "anchor": "center",
      "zIndex": 0,
      "fit": "cover",
      "motionRole": "slow push-in with sufficient edge coverage"
    },
    {
      "id": "primary-number",
      "type": "html-text",
      "text": "6000m+",
      "x": 260, "y": 500, "width": 420, "height": 120,
      "anchor": "left-center",
      "zIndex": 8,
      "typography": {
        "fontFamily": "ProjectSans",
        "fontFile": "../../assets/fonts/project-sans.woff2",
        "fontSize": 96, "fontWeight": 700, "lineHeight": 1.1,
        "color": "#202020", "textAlign": "left"
      },
      "motionRole": "emphasize after the supporting visual is readable"
    },
    {
      "id": "relation-line",
      "type": "svg-path",
      "x": 1000, "y": 600, "width": 450, "height": 80,
      "anchor": "top-left",
      "zIndex": 4,
      "viewBox": "0 0 450 80",
      "d": "M 10 40 L 440 40",
      "stroke": "#9E3B32", "strokeWidth": 4, "fill": "none",
      "motionRole": "reveal the verified relationship"
    }
  ]
}
~~~

例如本目录结构中的 background.png 相对 manifest 是 ../../assets/bitmap/background.png，相对 hyperframes/index.html 是 ../../../assets/bitmap/background.png。

## 交接需要的信息

| 信息 | 使用条件 |
|---|---|
| id、type、布局框、anchor、zIndex | 需要逐元素定位时；ID 唯一且与实现可对应 |
| file、实际尺寸、透明状态、fit / 裁切方式 | 位图元素 |
| text、字体来源、字号、行高、颜色、对齐 | 需重建文字时；若已由布局源明确，可引用对应元素样式 |
| 路径、viewBox、描边或形状参数 | 需重建 SVG 图形时 |
| 数据、单位、时间范围、来源与数值到几何的映射 | 表达真实数据关系时，可引用项目已有数据文件 |
| motionRole、需要独立控制的范围 | 动效元素；详细时间与音频对应放在 motion-brief |

有交接 JSON 不代表自动化已实现。只有项目确实需要机器消费时，才补相应结构校验和读取逻辑。交付前核对实际路径、字体可用性、坐标与合成预览的一致性。
