<!-- Generated from catalog/datasets/ok-vqa.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# OK-VQA

[English](ok-vqa.md)

图像本身信息不足、需要外部知识的视觉问答。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-10-02 |
| RAG 角色 | `rag_convertible` |
| 主分类 | `multimodal_rag` |
| 任务 | visual_qa, multimodal_retrieval |
| 模态 | text, image |
| 已发布真值标注层级 | answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | not_provided / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

发布内容提供问题、答案标注和 COCO 输入图像链接，没有固定外部知识语料。CVPR 2025 的 NoteMR 配合段落检索使用它；M2KR 则定义另一种改造。

发布规模：14,055 个问题，每题五份人工参考答案。
数据划分：官方训练集和测试集；v1.1 更新答案词干处理，不改问题或图像。
格式：VQA-format question and annotation JSON; COCO images acquired separately.。

## 真值与评测

提供可接受答案字符串，原始版本没有指定金标准维基百科段落或支持图像区域。后续检索监督需明确归属于其构建方法。

官方指标：VQA_accuracy。

评测协议：使用官方答案归一化并固定 v1.1 标签。记录外部语料及检索监督；不同知识池或 M2KR 转换版本的分数不能直接互换。

## 适用场景

- 以图像和问题共同驱动知识检索
- 比较外部知识与模型直接回答

## 限制与注意事项

- 原生标注提供答案而非段落检索真值
- COCO 图像条款与问答标注分开适用

## 获取方式与来源

- [官方资源](https://okvqa.allenai.org/)
- [论文](https://arxiv.org/abs/1906.00067)
- [数据](https://okvqa.allenai.org/download.html)
- official：[来源](https://okvqa.allenai.org/) — 支持字段 `summary`、`data.size`、`ground_truth.description`
- official：[来源](https://okvqa.allenai.org/download.html) — 支持字段 `data.description`、`data.splits`、`data.format`、`evaluation.protocol`
- paper：[来源](https://arxiv.org/abs/1906.00067) — 支持字段 `evaluation.official_metrics`、`classification.rag_role`
- repository：[来源](https://github.com/Jorffy/NoteMR) — 支持字段 `data.description`、`use.best_for`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
