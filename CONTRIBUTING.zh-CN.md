# 参与贡献

[English](CONTRIBUTING.md)

欢迎纠错或新增数据集记录。本项目是经过来源核对的目录：一条有充分依据的小修正，比未经核实的大名单更有价值。

1. 先选对实体类型：dataset、suite、corpus、task 或 paper。不要把仅测信息检索的套件标为完整 RAG benchmark。
2. 在 `catalog/` 下新增或修改一条 YAML 记录；文件名主体必须等于 `id`。许可或事实无法确认时写 `unknown`，不能推断缺失的证据标注。
3. 把原生任务与建议的 RAG 改造分开描述。说明来源池、查询、答案、证据粒度、指标、适用场景和限制。数量须附单位、变体或划分及一手来源。新增套件时请填写 `summary_zh`，避免中文 README 退回显示英文摘要。
4. 在 `sources` 中填写官方论文、作者项目页、作者仓库或官方数据卡 URL，并列出各来源支持的字段路径。关键字段未核对时从 `screened` 开始；只有具备核对日期和字段级引用才使用 `source_checked`；没有运行记录不能声称 `reproduced`。
5. 执行下列命令，并将生成的中英文 README 与卡片随 YAML 一起提交。不要手工修改生成文件。

```bash
python -m pip install -e ".[dev]"
python -m scripts.validate_catalog
python -m scripts.generate --write
python -m scripts.generate --check
python -m scripts.check_secrets
python -m pytest -q
```

事实纠错应提供记录 ID、准确字段、旧值/新值、官方来源及核对日期。新增记录应解释为何属于 RAG 原生、可改造或辅助数据。不要提交数据集二进制文件、访问令牌、私人研究笔记或仅在个人机器上有效的路径。原始数据集沿用各自的条款；本仓库许可仅适用于原创目录代码与说明文字。
