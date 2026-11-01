<!-- Generated from catalog/datasets/browsecomp.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# BrowseComp

[English](browsecomp.md)

通过短参考答案评测持续搜索能力的实时网页浏览问题，要求寻找隐蔽的多步事实。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-11-01 |
| RAG 角色 | `rag_native` |
| 主分类 | `text_rag` |
| 任务 | agentic_search, multi_hop_qa |
| 模态 | text |
| 已发布真值标注层级 | answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | external / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

人工出题者构建难以检索的事实问题，供具有网页搜索与浏览工具的代理作答。公开参考加载器从作者托管的 CSV 读取混淆后的问题与答案，不提供固定网页语料。

发布规模：共 1,266 道评测题；论文另行开展的人工验证覆盖 1,255 道问题，两者统计口径不同。
数据划分：公开测试集；BrowseComp-Plus 是独立的固定语料改造，不是相同评测设置。
格式：Obfuscated CSV with an author-provided reference loader.。

## 真值与评测

人工提供简短且意图无歧义的答案。此发布不提供完整文档相关性、来源片段或金标准浏览轨迹。

官方指标：accuracy, calibration_error。

评测协议：使用论文的答案等价判定与置信度校准协议，记录浏览工具、搜索提供方、日期和推理预算。答案正确率不等于证据召回。归档参考评分器使用前须核对具体版本，本目录没有复现其执行。

## 适用场景

- 在固定预算下评测持续多步网页搜索
- 比较实时网页代理与固定语料 BrowseComp-Plus

## 限制与注意事项

- 没有固定来源语料或检索相关性标签，网页与搜索服务变化会影响复现
- 原作者要求不要以明文公开评测样例，本仓库不镜像问题或答案
- simple-evals 代码采用 MIT，但未确认独立数据许可；其 README 说明 2025 年 7 月停止积极更新

## 获取方式与来源

- [官方资源](https://openai.com/index/browsecomp/)
- [论文](https://arxiv.org/abs/2504.12516)
- [数据](https://openaipublic.blob.core.windows.net/simple-evals/browse_comp_test_set.csv)
- official：[来源](https://openai.com/index/browsecomp/) — 支持字段 `summary`、`data.description`、`data.size`、`ground_truth.description`、`ground_truth.provenance`、`use.caveats`
- paper：[来源](https://arxiv.org/html/2504.12516) — 支持字段 `classification.rag_role`、`evaluation.official_metrics`、`evaluation.protocol`
- repository：[来源](https://github.com/openai/simple-evals/blob/main/browsecomp_eval.py) — 支持字段 `data.format`、`data.splits`、`access.data`、`evaluation.evaluator`、`evaluation.protocol`
- repository：[来源](https://github.com/openai/simple-evals) — 支持字段 `access.license`、`use.caveats`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
