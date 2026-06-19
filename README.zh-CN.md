# Agent-Native OS

语言：[English](README.md) | [简体中文](README.zh-CN.md)

面向长任务 AI Agent 与可安装 Skill App 的上下文原生操作系统架构。

![Spec](https://img.shields.io/badge/spec-v0.2-blue)
![License](https://img.shields.io/badge/license-Apache--2.0-green)
![Status](https://img.shields.io/badge/status-draft-orange)

## 这是什么？

今天的大多数 AI Agent 正在学习如何使用人类电脑：屏幕、按钮、浏览器、终端、API 和 GUI 工作流。

Agent-Native OS 问的是另一个问题：

> Agent 自己工作时，需要什么样的操作系统？

人类操作系统围绕应用、窗口、文件和设备构建。

Agent 原生系统应该围绕上下文、法源层级、任务隔离、角色运行时、输出契约、审查门禁、交接协议、归档和恢复点构建。

## 核心判断

在人类 OS 里，应用是第一公民。

在 Agent OS 里，上下文是第一公民。

Agent-Native OS 是一种开放架构，用于在可治理、上下文感知的 Agent 工作空间中安装和运行 Skill App。

通俗说，它就是 AI Agent 的 Windows 层：一个原生工作空间，让 Agent 可以安装 Skill App、管理上下文、执行权限、审查输出，并保存长期项目状态。

## 五大原则

Agent-Native OS 建立在五个原则上：

1. 上下文是第一资源。
2. 契约化自然语言是源代码。
3. 上下文内核是运行时。
4. 结构化输出是 Context ABI。
5. Skill App 是可安装应用。

## 本项目定义什么

这个仓库定义以下开放架构：

- Context Kernel：上下文内核
- Skill App Runtime：技能应用运行时
- Source File System：法源文件系统
- Role & Permission System：角色权限系统
- Task Scheduler：任务调度器
- Output Contract Engine：输出契约引擎
- Audit Gate：审查门禁
- Handoff Bus：交接总线
- Memory & Archive Layer：记忆与归档层
- Recovery System：恢复系统

## 它不是什么

Agent-Native OS 不是：

- 提示词包
- GUI 自动化工具
- 单 Agent 脚本
- 简单工作流模板
- 绑定某个厂商的 Agent 框架
- 某个私有领域发行版

更准确地说：

- 模型框架管模型调用。
- Agent 框架管工具调用。
- 工作流引擎管步骤编排。
- Agent-Native OS 管长期 Agent 工作的秩序。

## 试跑 Demo

运行：

```bash
python scripts/run_docs_brief_demo.py
```

然后打开：

```txt
examples/docs-brief-demo/PROMPT_FOR_AGENT.md
```

把提示词复制给 Codex、ChatGPT、Claude 或其他 Agent，让它按 Agent-Native OS 的任务契约生成产物。

验证工作区：

```bash
python scripts/validate_workspace.py examples/docs-brief-demo
```

这个 Demo 展示最小可治理闭环：

```txt
Source -> Task -> Mount -> Output Contract -> Agent Prompt -> Handoff -> Audit
```

## 最小可行内核

MVP 很小：

1. Skill App Manifest：技能应用声明
2. Source Mount：资料挂载协议
3. Task Card：任务卡协议
4. Output Contract：输出契约
5. Handoff Report：交接报告

建议扩展：

6. Audit Gate：审查门禁
7. Recovery Point：恢复点
8. Role Runtime：角色运行时
9. Skill Registry：技能注册表
10. Source Policy：法源策略

## 仓库结构

```txt
agent-native-os/
  README.md
  README.zh-CN.md
  MANIFESTO.md
  SPEC.md
  ROADMAP.md
  CORE_THEORY_AND_GLOSSARY.md
  NAMING_STRATEGY.md
  BILINGUAL_POLICY.md
  docs/
  spec/
  templates/
  examples/
  scripts/
```

## 开放内核，私有发行版

本仓库定义开放架构。

领域专用发行版可以基于本架构构建。私有发行版可能包含行业工艺、商业逻辑、评分系统和专有工作流，不包含在本仓库内。

开放架构，保留私有发行版。

## 建议 GitHub 简介

```txt
A context-native operating system architecture for long-running AI agents and installable Skill Apps.
```

## 建议 topics

```txt
ai-agents
agent-os
agent-native
context-engineering
context-native
multi-agent
skill-apps
workflow-automation
agent-framework
ai-native
```

## 协议

Apache-2.0。见 `LICENSE`。
