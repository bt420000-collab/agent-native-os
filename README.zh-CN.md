# Agent-Native OS

语言：[English](README.md) | [简体中文](README.zh-CN.md)

面向长任务 AI Agent 的上下文原生操作系统架构。

今天的大多数 AI Agent 正在学习如何使用人类电脑：屏幕、按钮、浏览器、终端、API 和 GUI 工作流。

Agent-Native OS 问的是另一个问题：

> Agent 自己工作时，需要什么样的操作系统？

人类操作系统围绕应用、窗口、文件和设备构建。Agent 原生系统应该围绕上下文、法源层级、任务隔离、角色运行时、输出契约、审查门禁、交接协议、归档和恢复点构建。

## 核心判断

在人类 OS 里，应用是第一公民。

在 Agent OS 里，上下文是第一公民。

Agent-Native OS 是一种开放架构，用于在可治理、上下文感知的 Agent 工作空间中安装和运行 Skill App。

## 本项目定义什么

这个仓库是一个“Agent Windows”层的规范与项目种子：

- Context Kernel：上下文内核
- Skill App Runtime：技能应用运行时
- Source File System：法源文件系统
- Role & Permission System：角色权限系统
- Task Scheduler：任务调度器
- Output Contract Engine：输出契约引擎
- Audit Gate：审查门禁
- Handoff Bus：交接总线
- Memory & Archive Layer：记忆与归档层
- Recovery System：事故恢复系统

## 它不是什么

Agent-Native OS 不是另一个聊天提示词包。

它不是 GUI 自动化工具。

它也不是模型框架、工具框架或工作流引擎的替代品。

更准确地说：

- 模型框架管模型调用。
- Agent 框架管工具调用。
- 工作流引擎管步骤编排。
- Agent-Native OS 管长期 Agent 工作的秩序。

## 为什么现在需要它

工具正在爆炸式增加：浏览器、终端、API、MCP、文件编辑器、向量数据库、GUI 控制。工具越多，Agent 越强，也越容易乱。

没有 OS 层，Agent 会出现：

- 上下文爆炸
- 角色串线
- 法源污染
- 交接失忆
- 输出漂移
- 越权修改
- 审查失效
- 旧档闹鬼
- 用户意见丢失
- 长程退化

Agent-Native OS 要把 Agent 工作变成一个可治理的环境。

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
  AUTHORS.md
  BILINGUAL_POLICY.md
  MANIFESTO.md
  NAMING_STRATEGY.md
  SPEC.md
  ROADMAP.md
  CODEX_HANDOFF.md
  docs/
  spec/
  templates/
  examples/
  scripts/
```

## 开放内核，私有发行版

本仓库定义开放架构。

领域专用发行版可以基于本架构构建。私有发行版可能包含行业工艺、商业逻辑、评分系统和专有工作流，不包含在本仓库内。

## 参与贡献

这是一个规范优先的项目。欢迎贡献架构澄清、模板改进、中立示例，以及安全与治理模型方面的增强。

请参见 `CONTRIBUTING.md`、`GOVERNANCE.md`、`SECURITY.md`、`CODE_OF_CONDUCT.md` 和 `BILINGUAL_POLICY.md`。

## 作者与联系方式

维护者：[bt420000-collab](https://github.com/bt420000-collab)

- 邮箱：bt420@126.com
- 微信：iMelodyJust

## 口号

> 别只教 Agent 使用人类桌面。给它们一个原生工作空间。

更直接一点：

> 我们在做 Agent 的 Windows 层：一个上下文原生操作系统，开发者可以在里面安装 Skill App，组合出可靠的工作流。

## 协议

Apache-2.0。见 `LICENSE`。
