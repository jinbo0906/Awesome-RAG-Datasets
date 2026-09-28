# Dataset、benchmark、suite、corpus 与 evaluator

[English](benchmark-vs-dataset.md)

这些词在论文标题中常被混用，但回答的问题不同。**Dataset（数据集）**是发布的样本、标注或来源资产集合。**Benchmark（评测基准）**是一份评测契约：任务、允许使用的输入与来源池、划分、真值、指标、评测器及比较规则。只有这些决策明确后，数据集才能作为某个 benchmark 使用。论文可能用同一名称指数据和协议；本目录只记录一次数据，并在同一张卡片中描述原生协议，不会为了重复名称再造一个对象。

| 对象 | 必须说明什么 | 例子 | 目录位置 |
|---|---|---|---|
| Dataset | 样本、标注、来源关系、版本与访问 | [RAGTruth](../dataset-cards/text-rag/ragtruth.md) 有来源与生成回答配对，以及幻觉片段标注 | `catalog/datasets/` |
| Benchmark 协议 | 任务、输入与允许的证据、划分、指标和评测器 | [RGB](../dataset-cards/text-rag/rgb.md) 在指定噪声率和段落数量下测试固定上下文的鲁棒性 | 数据集的 `evaluation`；共享协议写在套件的 `protocol` |
| Suite（套件） | 共享比较协议下的多个数据集或任务变体 | [BEIR](../suite-cards/beir.md) 统一检索评测；[ALCE](../suite-cards/alce.md) 将三个长回答 QA 数据集改造为引用评测 | `catalog/suites/` |
| Corpus（语料） | 可供多个 benchmark 使用的版本化来源集合 | [KILT Wikipedia](../catalog/corpora/kilt-wikipedia-2019.yaml) 是固定快照；播客文本是一个 [GraphRAG 语料](../catalog/corpora/ms-graphrag-podcasts.yaml) | `catalog/corpora/` |
| Evaluator 或框架 | 计算或组织分数的软件 | [Ragas](https://docs.ragas.io/en/stable/concepts/metrics/overview/) 提供指标，本身不是固定问题语料 | 数据集目录之外 |
| Paper（论文） | 介绍、重处理或评测某一对象的出版物 | 检索论文使用 QA 数据集，不会使其自动变成原生 RAG 数据集 | `catalog/papers/` |

这一区别会直接影响实验设计。[MS MARCO Passage Ranking](../dataset-cards/text-rag/msmarco-passage.md)有语料、查询和稀疏相关性标注，可以评测检索器，但其排序变体没有生成回答真值；它属于 RAG 的 `auxiliary` 组件，不是端到端回答 benchmark。[ToTTo](../dataset-cards/table-rag/totto.md)把高亮单元格**作为输入**提供给生成器，并不测试能否找回这些单元格。[MTRAG](../dataset-cards/text-rag/mtrag.md)包含语料、检索任务、对话答案及不同的参考证据/完整 RAG 设置，因此有条件区分检索和生成失败。

## 新条目的判断规则

1. 是否存在发布了样本或来源资产的权威版本？如果没有，仅有方法名称不是数据集。
2. 是否有固定或明确按时间索引的来源池、查询，以及答案/证据关系？如果没有，应说明 RAG 改造还需补建什么，不得称原始任务为端到端 RAG。
3. 是否为带版本、共享评测规则的多个子数据集包？如果是，应建为 suite；只有核查具体变体后才关联子项。原始数据集不能等同于套件中重处理的子集。
4. 标注位于**来源材料**还是**生成回答**？`span` 与 `response_span` 不同。只有答案标签无法直接评测证据检索。
5. 换语料、划分、评测器或金标准上下文的可见范围后，系统能看到的内容是否变化？若变化，应报告独立设置或版本，分数不能直接互比。

README 的主分类按来源表示形式划分为文本、多模态、图和表格。QA、事实核查、检索、对话与引用是**任务**；医疗、金融与法律是**领域**。它们是交叉维度，不应再当作互斥的顶层分类。具体用法参见[分类体系](taxonomy.zh-CN.md)与[选型指南](selecting-a-benchmark.zh-CN.md)。
