<!-- Generated from catalog/datasets/oaks.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# OAKS (Online Adaptation to Continual Knowledge Streams)

[English](oaks.md)

按时间顺序释放片段并为每个时间步标注答案，用来测量事实变化后的适应速度。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-11-18 |
| RAG 角色 | `auxiliary` |
| 主分类 | `text_rag` |
| 任务 | time_sensitive_qa, long_context_qa |
| 模态 | text |
| 已发布真值标注层级 | sentence, answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | Adobe Research License (academic research or teaching and noncommercial use) |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

OAKS-B 是频繁状态变化的合成叙事，OAKS-N 是公版小说片段与多项选择题。按流顺序回放，到达时再开放片段。

发布规模：固定公开版本的 OAKS-B 有 12 条流、1,224 个问题 ID、78,994 个问题与时间步标签。OAKS-N 有 19 部小说、435 个问题 ID、32,403 个标签，论文描述的规模为 39 部小说与 870 题。
数据划分：已发布的 OAKS-B 叙事和 OAKS-N 小说分别评估，同一问题的多时间步仅计一个唯一问题。
格式：JSON with ordered chunks and question-to-answer maps indexed by chunk。

## 真值与评测

chunk_to_answer 记录各时间步的答案。小说轨保存选项正文，option_sources 将选项关联到相应时间步的支持句。答案状态用于适应评分。

官方指标：interval_accuracy, acquisition_latency_AL, distraction_susceptibility_DS, phase_miss_rate_PM。

评测协议：按时间步答题后对问题做宏平均。论文区分首次答对前的错误、首次答对后的回退和从未答对的阶段。发布脚本会把整段答错计入迟滞，记录采用哪一口径。原 RAG 预取邻居后过滤尚未开放的片段。

## 适用场景

- 回放反复变化的事实并测量恢复正确状态所需的步数
- 在相同时间流下比较检索与在线适应方案

## 限制与注意事项

- 公开实验应报告实际使用的小说子集分母
- 逐时间步答案状态与小说支持信息需区分
- 若测在线索引可见性延迟应另行报告

## 获取方式与来源

- [官方资源](https://github.com/adobe-research/OAKS)
- [论文](https://aclanthology.org/2026.acl-long.1956/)
- [数据](https://github.com/adobe-research/OAKS/tree/0bbc4b3877eae5f9335f07c5e485aabf1d9136e9/data)
- paper：[来源](https://aclanthology.org/2026.acl-long.1956.pdf) — 支持字段 `summary`、`classification`、`data.description`、`ground_truth`、`evaluation.official_metrics`、`evaluation.protocol`、`use`
- repository：[来源](https://github.com/adobe-research/OAKS/tree/0bbc4b3877eae5f9335f07c5e485aabf1d9136e9/data) — 支持字段 `data.size`、`data.splits`、`data.format`、`ground_truth.description`、`access.data`
- repository：[来源](https://github.com/adobe-research/OAKS/blob/0bbc4b3877eae5f9335f07c5e485aabf1d9136e9/LICENSE) — 支持字段 `access.license`
- repository：[来源](https://github.com/kaistAI/OAKS/tree/c1a76e66b5b2276973ee8ee3de7063721e22a88f) — 支持字段 `evaluation.evaluator`、`evaluation.protocol`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
