<!-- Generated from catalog/datasets/rag-rewardbench.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# RAG-RewardBench

[English](rag-rewardbench.md)

使用优选与拒选回答对，评测奖励模型对 RAG 特有偏好的判断。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-11-01 |
| RAG 角色 | `auxiliary` |
| 主分类 | `text_rag` |
| 任务 | response_preference, rag_robustness, attribution |
| 模态 | text |
| 已发布真值标注层级 | response_preference |
| 证据标注来源 | synthetic |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | Apache-2.0 |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

每条记录包含 prompt 中的检索参考资料、question、chosen/reject 候选回答、生成模型和子集标签。构建采用六个检索器和 24 个回答模型扩展多样性；这是固定上下文回答比较数据，不是开放检索语料。

发布规模：1,485 个偏好对，来源于 18 个 RAG 来源子集并加入 RAG 特定的比较情境。
数据划分：Hugging Face 将唯一划分命名为 train，但引入论文将其用于评测，不能假设已有独立留出测试集。
格式：JSON with prompt, question, chosen, reject, model and subset fields。

## 真值与评测

发布目标是 chosen 优于 reject 的偏好顺序，而不是参考问答答案或来源证据片段。多个模型评判候选回答并过滤低一致性对；人工偏好核验只针对抽样，不代表每个发布对都有人工标签。

官方指标：pairwise_preference_accuracy。

评测协议：在同一组参考资料下，让 chosen 的得分高于 reject。对生成式评判模型交换候选顺序，运行两次并平均准确率，以减少位置偏差。先报告各场景/子集再汇总。多跳推理、细粒度引用、拒答与冲突鲁棒性是偏好条件，不是四个各自带相关性标注的检索 benchmark。

## 适用场景

- 为有依据生成选择奖励模型或回答评判器
- 检查偏好评分器能否识别引用错误和不当拒答

## 限制与注意事项

- 模型生成偏好可能继承一致性筛选和评判模型偏差
- 高偏好对准确率不等于端到端检索或答案准确率
- 公开 GitHub 仓库链接数据与论文，但本身没有完整评测器实现
- 2024 年预印本和 Findings ACL 2025 正式发表是不同节点

## 获取方式与来源

- [官方资源](https://github.com/jinzhuoran/RAG-RewardBench)
- [论文](https://aclanthology.org/2025.findings-acl.877/)
- [数据](https://huggingface.co/datasets/jinzhuoran/RAG-RewardBench)
- paper：[来源](https://aclanthology.org/2025.findings-acl.877.pdf) — 支持字段 `summary`、`classification`、`data.size`、`ground_truth`、`evaluation`、`use`
- dataset_card：[来源](https://huggingface.co/datasets/jinzhuoran/RAG-RewardBench) — 支持字段 `data.description`、`data.corpus`、`data.queries`、`data.answers`、`data.splits`、`data.format`、`access.license`、`access.gated`
- repository：[来源](https://github.com/jinzhuoran/RAG-RewardBench) — 支持字段 `access.data`、`use.caveats`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
