# Awesome RAG Datasets

这是一个面向研究者与工程实践者的 RAG 数据集和 benchmark 目录。它把 TextRAG、多模态 RAG、GraphRAG、TableRAG 的数据对象、评测套件、原始语料与任务分开记录，并重点说明“能测什么、真值到哪一级、怎样复现、在哪些场景不适用”。完整条目和英文数据集卡片见 [主目录](README.md)。

## 如何使用

先看 [选型指南](guides/selecting-a-benchmark.md)，按研究问题选择候选；再打开具体卡片，核对 corpus、query、answer、证据粒度、官方指标、许可与限制。不要把数据集原始任务和某个论文中的 RAG 改造版混为一谈。[分类与审查状态](guides/taxonomy.md)解释 `rag_native`、`rag_convertible`、`auxiliary` 和 `source_checked` 等字段。目录是经过来源核对的导航工具，不是排行榜，也不表示每个数据集都已经下载和跑通。

针对“分块缺乏唯一真值”和“多模态证据碎片化”，[证据真值设计](guides/evidence-ground-truth.md)给出源坐标、可替代证据集合、完整证据链、分层指标和对照实验原则。[新 benchmark 构建流程](guides/benchmark-construction.md)说明如何选择源资产、标注、划分、复现与发布。这里提供的是设计框架；尚未声称两个新 benchmark 已经完成标注。

## 目录边界

项目不镜像上游数据，不把普通知识问答自动视为 RAG benchmark，不把检索指标等同于最终回答质量。所有数据集许可和访问规则以原作者为准。`catalog/` 的 YAML 是唯一事实源，主目录和卡片自动生成；贡献与核验方法见 [CONTRIBUTING.md](CONTRIBUTING.md)。

```bash
python -m pip install -e ".[dev]"
python -m scripts.validate_catalog
python -m scripts.generate --check
python -m pytest -q
```
