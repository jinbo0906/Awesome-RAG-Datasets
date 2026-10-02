# Multimodal RAG：先检索，再进行视觉推理

[English](multimodal-rag.md)

本类涵盖证据跨越文本、图像、文档版面、表格、图表、音频或视频的来源集合。关键不在于样本是否包含图片，而在于发布的评测协议是否让系统在回答前**找到**所需来源证据。先看[多模态目录](../../README.zh-CN.md#multimodal-rag)。

| 证据场景 | 建议查看 | 原生标注的边界 |
|---|---|---|
| 页面与区域检索 | [MMDocIR](../../dataset-cards/multimodal-rag/mmdocir.zh-CN.md)、[ViDoRe](../../suite-cards/vidore.zh-CN.md) | 有检索标注，但不能单独评测回答生成 |
| 跨页回答与引用 | [MMDocRAG](../../dataset-cards/multimodal-rag/mmdocrag.zh-CN.md)、[XL-DocBench](../../dataset-cards/multimodal-rag/xl-docbench.zh-CN.md)、[MAVIS](../../dataset-cards/multimodal-rag/mavis.zh-CN.md) | 页面、原文摘录或事实引用，粒度各不相同 |
| 图文混合网页证据 | [WebQA](../../dataset-cards/multimodal-rag/webqa.zh-CN.md)、[MultiModalQA](../../dataset-cards/multimodal-rag/multimodalqa.zh-CN.md) | 来源 ID，不一定有针对问题标注的像素区域或单元格 |
| 给定视觉上下文 | [ChartQA](../../dataset-cards/multimodal-rag/chartqa.zh-CN.md)、[MP-DocVQA](../../dataset-cards/multimodal-rag/mp-docvqa.zh-CN.md)、[InfoSeek](../../dataset-cards/multimodal-rag/infoseek.zh-CN.md) | 答案及部分页面或版面元数据；开放检索属于后续改造 |
| 通用多模态检索 | [M-BEIR](../../suite-cards/m-beir.zh-CN.md)、[M2KR](../../suite-cards/m2kr.zh-CN.md) | 检索子集与指标；转换版须与原始 QA 数据分开 |

针对证据碎片化，可建模“文档 → 页面 → 区域 → 来源元素 → 原子事实”，再记录 `caption_of`、`table_header_of`、`continued_on` 等带类型的关系。页面召回和回答正确率都可能很高，图与图注之间的联系却仍然缺失。因此应分别评测页面、区域、关系、完整证据链和引用。一个版面框可能只标识页面对象，并不是**针对当前问题**的支持证据。保留原始 PDF 或图像坐标，以及解析器和 OCR 版本。

视频会进一步引入时间区间、字幕、帧及跨模态同步。仅有视频 QA 论文或算法仓库，不足以证明可复用的视频 RAG 数据、时间相关性标注和原始资产已经公开；本目录核对发布边界后才新增此类条目。缺失的证据链标注如何补建，见[新 benchmark 构建流程](../benchmark-construction.zh-CN.md)。

## 近期论文驱动的补充

[论文采用索引](../recent-paper-index.zh-CN.md)注明来源数据用于训练、评测还是检索改造。新增卡片提供以下对照：

| 设置 | 新增入口 | 评测边界 |
|---|---|---|
| 明确的开放文档检索 | [OpenDocVQA](../../dataset-cards/multimodal-rag/opendocvqa.zh-CN.md) | 过滤后的来源问答及独立许可、需同意条款的图像语料，不是单页 DocVQA |
| 查询改写鲁棒性 | [REAL-MM-RAG](../../dataset-cards/multimodal-rag/real-mm-rag.zh-CN.md) | 四个文档子集和合成页面相关性；基础查询、措辞版本及 Parquet 行属于不同计数单位 |
| 文档阅读与抽取 | [DocVQA](../../dataset-cards/multimodal-rag/docvqa.zh-CN.md)、[InfographicVQA](../../dataset-cards/multimodal-rag/infographicvqa.zh-CN.md)、[DUDE](../../dataset-cards/multimodal-rag/dude.zh-CN.md)、[TAT-DQA](../../dataset-cards/multimodal-rag/tat-dqa.zh-CN.md) | 给定文档，答案框可能缺失，支持事实可能是启发式标签 |
| OCR 级联影响 | [OHRBench](../../dataset-cards/multimodal-rag/ohrbench.zh-CN.md) | 转录参考、页面或引用文本证据及 LCS 包含度不同于区域相关性 |
| 外部视觉知识 | [MRAG-Bench](../../dataset-cards/multimodal-rag/mrag-bench.zh-CN.md)、[Visual-RAG](../../dataset-cards/multimodal-rag/visual-rag.zh-CN.md)、[Encyclopedic-VQA](../../dataset-cards/multimodal-rag/encyclopedic-vqa.zh-CN.md)、[OK-VQA](../../dataset-cards/multimodal-rag/ok-vqa.zh-CN.md)、[A-OKVQA](../../dataset-cards/multimodal-rag/a-okvqa.zh-CN.md) | 原生图像、金标准检索知识与固定候选池是不同配置 |
| 交错生成与混合任务 | [RAG-IGBench](../../dataset-cards/multimodal-rag/rag-igbench.zh-CN.md)、[M²RAG](../../dataset-cards/multimodal-rag/m2rag.zh-CN.md) | 图像选择与位置不同于多模态问答、核查 |
| 感知或改造检索对照 | [TextVQA](../../dataset-cards/multimodal-rag/textvqa.zh-CN.md)、[ArXivQA](../../dataset-cards/multimodal-rag/arxivqa.zh-CN.md)、[PlotQA](../../dataset-cards/multimodal-rag/plotqa.zh-CN.md) | 答案或 OCR 对象不自动等于按问题标注的检索相关性 |

新增数据不意味着图注、OCR 框或文字解释可以代替完整跨模态证据链。自定义划分需按文档家族隔离，并独立标注缺失的来源元素关系。
