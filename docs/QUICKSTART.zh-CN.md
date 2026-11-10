# 快速开始

1. 按首页说明安装完整 skill 目录。使用 [Agent Skills 通用格式](https://agentskills.io/specification)。Codex 项目可用 `.agents/skills/<名称>/`；Claude Code 项目可用 `.claude/skills/<名称>/`。以当前 Agent 版本支持为准，不需要修改全局设置。
2. 新对话中，Codex 使用 `$skill-name`，Claude Code 使用 `/skill-name`；把名称换为实际已安装项。也支持自然语言任务，明确调用更便于验证。
3. 粘贴任务与证据。说明具体交付、买家、已知地区，以及主业或副业目标；提供影响判断的时间和现金条件。
4. 阅读结果与证据限制。无法核验最新资料时，结果保持暂定；补充证据会影响决策时再要求完整分析。

## 名称与升级

新安装使用 `idea-validation`，在 Codex 中通过 `$idea-validation` 调用。`business-opportunity-evaluator` 保留为可独立安装的兼容名称，旧命令、旧路径和旧 Release 安装包不变。两份 skill 除名称之外使用相同评估说明。安装其中一个即可；升级前先保存自己修改过的内容，不要直接覆盖。

## 依赖与隔离

不需要脚本运行环境。依赖最新事实的结论才需要检索；工作簿输出不是硬性条件。

用户记录放在 skill 和源仓库之外。升级测试使用临时项目，避免覆盖已有自定义版本。示例全部为虚构，不是客户成绩。[验证报告](VALIDATION.md)区分实际测试与仅格式兼容。
