# Docs Brief Demo

语言：[English](README.md) | [简体中文](README.zh-CN.md)

这个 Demo 展示 Agent-Native OS 的最小工作闭环：

```txt
Source -> Task -> Mount -> Output Contract -> Agent Prompt -> Handoff -> Audit
```

## 目的

用 Agent-Native OS 把零散项目资料整理成可审查、可交接、可继续处理的项目简报。

场景保持中立：一个小团队正在搭建内部知识库，需要从零散会议记录和当前需求中整理出简明文档简报。

## 它展示什么

- 资料必须被显式挂载。
- Task Card 定义角色、目标、可读资料、禁用区域、输出和审查要求。
- Output Contract 定义必需章节和输出路径。
- Skill App 声明说明、权限和输出契约。
- 可复制提示词允许人类用任意合适的编码 Agent 或 LLM 执行任务。
- 交接报告保留可继续处理的状态。
- 审查清单展示产物进入主线前如何被检查。

## 试跑

在仓库根目录运行：

```bash
python scripts/run_docs_brief_demo.py
```

然后打开：

```txt
examples/docs-brief-demo/PROMPT_FOR_AGENT.md
```

把提示词复制给你的编码 Agent 或 LLM。Agent 应创建：

```txt
examples/docs-brief-demo/.agent-os/outputs/TASK-001/documentation_brief.md
examples/docs-brief-demo/.agent-os/handoffs/HANDOFF-TASK-001.md
```

## 验证工作区

运行：

```bash
python scripts/validate_workspace.py examples/docs-brief-demo
```

验证器会检查最小 Agent-Native OS 工作区骨架，以及是否至少存在一个任务文件。
