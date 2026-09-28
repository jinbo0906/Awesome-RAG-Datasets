<!-- Generated from catalog/datasets/infoseek.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# InfoSeek

[English](infoseek.md)

基于 OVEN 图像与维基百科衍生信息的知识密集型视觉问答数据。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `rag_convertible` |
| 主分类 | `multimodal_rag` |
| 任务 | visual_qa, multimodal_retrieval |
| 模态 | text, image |
| 已发布真值标注层级 | answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

项目发布与图像关联的问题、可接受的答案别名、知识库映射及约六百万条维基百科文本资源。 图像来自 OVEN，须另行获取；原始问答与 M2KR 的检索改造属于不同协议。


## 真值与评测

提供答案及等价表达。已发布映射可支持检索改造，但不能据此声称每题都有人工标注的最小证据页面或图像区域。

官方指标：answer_accuracy。

评测协议：指明图像、维基百科和问题版本。RAG 实验需披露知识候选池和 qrels 的构建方式，不能把 M2KR 的 qrels 视为原生 InfoSeek 真值。

## 适用场景

- 依赖外部知识的视觉问题
- 利用维基百科文本进行检索改造

## 限制与注意事项

- 获取图像还依赖单独的上游资源
- 原生问答不保证有针对问题的视觉区域证据

## 获取方式与来源

- [官方资源](https://github.com/open-vision-language/infoseek)
- [论文](https://arxiv.org/abs/2302.11713)
- repository：[来源](https://github.com/open-vision-language/infoseek) — 支持字段 `summary`、`data.description`、`ground_truth.description`、`evaluation.protocol`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
