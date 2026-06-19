# Docs Brief Demo

语言：[English](README.md) | [简体中文](README.zh-CN.md)

这个 Demo 展示 Agent-Native OS 的最小闭环：

```txt
Source -> Task -> Mount -> Output Contract -> Agent Prompt -> Handoff -> Audit
```

目标是把零散项目资料整理成一份可治理的项目文档简报。

这个 Demo 不调用任何 API，也不需要外部依赖。它可以复制给 Codex、ChatGPT、Claude 或其他 Agent 执行。

## 这个 Demo 证明什么

这不是“让 AI 总结一下资料”。

这是一个可治理的 Agent 工作空间：

- 资料被挂载
- 任务有作用域
- Skill App 被声明
- 禁止路径被定义
- 输出受契约约束
- 未知信息必须标记
- 必须生成交接报告
- 输出需要审查

## Demo 文件

```txt
examples/docs-brief-demo/
  README.md
  README.zh-CN.md
  PROMPT_FOR_AGENT.md
  EXPECTED_OUTPUT_SAMPLE.md

  .agent-os/
    sources/
      project_notes.md
      current_requirements.md
    tasks/
      TASK-001.md
    mounts/
      MOUNT-001.yaml
    contracts/
      CONTRACT-TASK-001.yaml
    outputs/
      TASK-001/
    handoffs/
    reviews/

  skills/
    documentation-brief/
      manifest.yaml
      instructions.md
      output_contract.md
      permissions.yaml
```

## 运行检查

从仓库根目录执行：

```bash
python scripts/run_docs_brief_demo.py
python scripts/validate_workspace.py examples/docs-brief-demo
```

## 执行 Agent 任务

打开：

```txt
examples/docs-brief-demo/PROMPT_FOR_AGENT.md
```

把提示词复制给你的 Agent。

Agent 应该生成：

```txt
examples/docs-brief-demo/.agent-os/outputs/TASK-001/documentation_brief.md
examples/docs-brief-demo/.agent-os/handoffs/HANDOFF-TASK-001.md
```

然后 Host 或 Auditor 可以生成：

```txt
examples/docs-brief-demo/.agent-os/reviews/AUDIT-TASK-001.md
```

## 预期输出

见：

```txt
examples/docs-brief-demo/EXPECTED_OUTPUT_SAMPLE.md
```
