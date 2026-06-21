# Agent-Native OS

语言：[English](README.md) | [简体中文](README.zh-CN.md)

面向长任务 AI Agent 与可安装 Skill App 的上下文原生操作系统架构。

![Spec](https://img.shields.io/badge/spec-v0.2.8-blue)
![License](https://img.shields.io/badge/license-Apache--2.0-green)
![Status](https://img.shields.io/badge/status-draft-orange)

<p align="center">
  <a href="./docs/assets/homepage/poster-not-human-desktop.png">
    <img src="./docs/assets/homepage/poster-not-human-desktop.png" alt="不是让 AI 接管电脑，是给 AI 装一台自己的电脑" width="88%" />
  </a>
</p>

> **不是让 AI 接管电脑。**  
> **是给 AI 装一台自己的电脑。**

Agent-Native OS 不是给人类桌面用的操作系统。它是给 AI Agent 用的原生工作系统：一个可治理的工作空间，让 Agent 可以安装 Skill App、申请上下文、隔离工作区、通过系统 Host 启动子 Agent、交接状态，并维持长任务工作的稳定秩序。

通俗说，它就是 **AI Agent 的操作系统层**。

## v0.2 重点：唯一 Host 运行时

Agent-Native OS v0.2 明确了更干净的生态边界：

```txt
Agent-Native OS Core = 常驻 Host、运行时、调度器、权限与标准
Skill App = 由 OS 挂载的可安装能力包
Subagent = 由 OS Host 启动、暂停、关闭、归档的工作进程
```

Host 属于母系统。App 不是 Host。App 可以有 Coordinator，但只有 OS Host 拥有子 Agent 生命周期主权和全局上下文调度权。

## 核心原则

```txt
App 不拥有上下文，App 只能申请上下文。
上下文、Agent、工作区权限和调度权，全部归 Host 管理。
```

Skill App 运行前，必须提交 **上下文权限申请表**。系统打印 **Agent 运行审批卡**，展示计划启动的 Agent 阵容、上下文预算、工作区权限、跨 App 桥接和商业状态。用户可以批准、拒绝，或用自然语言修改方案。

例如用户可以说：

```txt
这小说评论区会炸，再给我加个喷子模拟 Agent。
```

系统可以将这个经用户批准的修改写入用户自定义上下文配置，并在后续运行中继承。

## Agent-Native OS 管什么

- 唯一常驻 OS Host
- 上下文权限申请
- Skill App 安装与挂载
- Subagent 调度与生命周期
- 工作区权限沙箱
- 进程表与上下文分配表
- 事件总线与恢复记录
- 跨 App Bridge
- 输出契约与交接报告
- 用户自定义 Agent 拓扑

## 生态模型

Agent-Native OS Core 应永久免费开源并持续更新。

Skill App 可以由官方、社区、私有团队或商业开发者开发。App 可以免费、开源、付费、免费增值、订阅、企业授权或私有部署。

```txt
系统提供秩序。
App 提供能力。
```

## 快速开始

### 当前目录安装规则

ANO v0.2.8 只能安装到当前获得用户授权的工作目录根目录，不准再创建 `ano-workspace/` 之类子目录。OS 初始化完成后必须停止，等待用户下一条指令，不能自动继续安装 Skill App。



初始化一个空白 v0.2 工作区：

```bash
python scripts/init_workspace.py
```

验证工作区：

```bash
python ano/scripts/validate_workspace.py
```

本仓库不再内置旧 demo。后续 demo 应全部按 `ano-<domain>-skill-app` 格式制作成标准可安装 App。


## v0.2.2 安装后工作区文件系统

开发仓库可以保留 docs、scripts、spec、templates 和官方 App 源码包。用户安装后的 ANO 工作区必须保持干净：

```txt
README.md
USER_LOG.md
ano/
user/
apps/
res/
out/
```

`ano/` 是系统发动机舱，`user/` 是用户数据，`apps/` 是已安装 Skill App，`res/` 是共享资源，`out/` 是最终导出。v0.2.2 起，安装后工作区禁止继续使用旧路径 `.agent-os/` 和 `skills/`。

## 开发者入口

- [APP_DEVELOPER_GUIDE.md](APP_DEVELOPER_GUIDE.md) - Skill App 标准开发说明
- [SPEC.md](SPEC.md) - v0.2 核心规范
- [VERSIONING.md](VERSIONING.md) - 版本定义与发布规则
- [ECOSYSTEM.md](ECOSYSTEM.md) - 开源母系统与 App 生态模型
- [templates/APP_MANIFEST.yaml](templates/APP_MANIFEST.yaml) - App manifest 模板
- [templates/CONTEXT_PERMISSION_REQUEST.yaml](templates/CONTEXT_PERMISSION_REQUEST.yaml) - 运行时资源申请模板

## 仓库结构

```txt
agent-native-os/
  README.md
  README.zh-CN.md
  SPEC.md
  ROADMAP.md
  CHANGELOG.md
  VERSIONING.md
  ECOSYSTEM.md
  APP_DEVELOPER_GUIDE.md
  CORE_THEORY_AND_GLOSSARY.md
  docs/
  spec/
  templates/
  scripts/
```

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

## 官方 App 安装包

主系统发布包可以在 `app_packages/official/` 中附带官方免费 demo app 的 ZIP 安装包。初始化工作区时，系统会把它们暂存到 `apps/_inbox/official/`，但不会自动安装。

当前官方包：

- `ano-calculator-skill-app_v0.1.2.zip`
- `ano-tiandao-furnace-skill-app_v0.4.0.zip`

详见 [OFFICIAL_APPS.md](OFFICIAL_APPS.md)。

## v0.2.8 OS Host Command Gate

After installation, every user instruction must be handled by the ANO Host/Admin Agent first. Do not bypass the OS by directly running app internals. Use:

```bash
python ano/scripts/ano_host.py "打开 ANO Tiandao Furnace Skill AppAgent"
```

The Host will resolve installation status, show permission/approval cards, and stop for user approval.


## Tiandao Furnace v0.4.0

The official multi-agent demo now starts with previous-draw intake, supports ANO Host web/weather lookup requests, handles overflow user choices without blocking, and adds feng-shui direction/weather/geography top-up. It remains entertainment-only and does not provide prediction or betting advice.
