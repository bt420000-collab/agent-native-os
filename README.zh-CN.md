# Agent-Native OS

语言：[English](README.md) | [简体中文](README.zh-CN.md)

面向长任务 AI Agent 与可安装 Skill App 的上下文原生操作系统架构。

![Spec](https://img.shields.io/badge/spec-v0.2.13-blue)
![License](https://img.shields.io/badge/license-Apache--2.0-green)
![Status](https://img.shields.io/badge/status-draft-orange)

<p align="center">
  <a href="./docs/assets/homepage/poster-not-human-desktop.png">
    <img src="./docs/assets/homepage/poster-not-human-desktop.png" alt="不是让 AI 接管电脑，是给 AI 装一台自己的电脑" width="88%" />
  </a>
</p>

<p align="center">
  <a href="./docs/assets/homepage/poster-token-effective-work.png">
    <img src="./docs/assets/homepage/poster-token-effective-work.png" alt="让 Token 花在有效工作上" width="43%" />
  </a>
  <a href="./docs/assets/homepage/poster-robot-os-standard.png">
    <img src="./docs/assets/homepage/poster-robot-os-standard.png" alt="给下一代智能机器人建立操作系统规范" width="43%" />
  </a>
</p>

> **不是让 AI 接管电脑。**  
> **是给 AI 装一台自己的电脑。**

Agent-Native OS 是给 AI Agent 使用的原生工作系统：提供唯一常驻 Host、干净工作区、可安装 Skill App、上下文权限申请、Subagent 生命周期管理、跨 App Bridge、用户自定义 Agent 阵容，以及可恢复的长任务运行秩序。

## 核心架构

```txt
Agent-Native OS Core = 常驻 Host、运行时、调度器、权限与标准
Skill App = 由 OS 挂载的可安装能力包
Subagent = 由 OS Host 启动、暂停、关闭或归档的工作进程
```

```txt
App 不拥有上下文，App 只能申请上下文。
上下文、Agent、工作区权限和调度权，全部归 ANO Host 管理。
```

Host 只属于母系统。App 可以定义 Coordinator，但 App 永远不是 Host。

每次 App 运行前必须提交上下文权限申请表。OS 展示 Agent 运行审批卡，列出角色阵容、上下文预算、工作区权限、跨 App 桥接和商业状态。用户可以批准、拒绝，或用自然语言修改阵容。

## 生态模型

Agent Native OS Core 永久免费开源并持续更新。Skill App 可由官方、社区、私有团队或商业开发者开发，并自由决定免费、开源、买断、订阅或企业授权模式。

```txt
系统提供秩序。
App 提供能力。
```

## 视觉总览

### 从 code-for-machines 到 context-for-agents

<p align="center">
  <a href="./docs/assets/homepage/diagram-from-code-to-agents.png">
    <img src="./docs/assets/homepage/diagram-from-code-to-agents.png" alt="从代码到 Agent 原生工作" width="82%" />
  </a>
</p>

### 系统架构与最小工作闭环

<p align="center">
  <a href="./docs/assets/homepage/diagram-core-architecture.png">
    <img src="./docs/assets/homepage/diagram-core-architecture.png" alt="系统架构图" width="46%" />
  </a>
  <a href="./docs/assets/homepage/diagram-operating-loop.png">
    <img src="./docs/assets/homepage/diagram-operating-loop.png" alt="最小工作闭环图" width="46%" />
  </a>
</p>

### Agent 原生系统与工作区布局

<p align="center">
  <a href="./docs/assets/homepage/diagram-agent-native-system.png">
    <img src="./docs/assets/homepage/diagram-agent-native-system.png" alt="Agent 原生系统图" width="46%" />
  </a>
  <a href="./docs/assets/homepage/diagram-workspace-layout.png">
    <img src="./docs/assets/homepage/diagram-workspace-layout.png" alt="工作区布局图" width="46%" />
  </a>
</p>

## 快速开始

ANO 只能安装到当前获得授权的工作目录根目录，不准创建 `ano-workspace/` 或其他套娃子目录。

```bash
python scripts/init_workspace.py
```

OS 初始化完成后必须停止，不得自动安装任何 App。

```bash
python ano/scripts/list_app_packages.py
python ano/scripts/install_app_package.py apps/_inbox/official/<package>.zip
python ano/scripts/install_app_package.py apps/_inbox/official/<package>.zip --yes
python ano/scripts/validate_workspace.py
```

第一次安装命令只预览安装卡。只有用户明确批准后，才能使用 `--yes`。

## 安装后的标准文件系统

```txt
README.md
USER_LOG.md
ano/
user/
apps/
res/
out/
```

- `ano/`：Host、内核、运行时、注册表、调度器、权限、Bridge、日志
- `user/`：用户资料、记忆、偏好、导入文件和项目
- `apps/`：已安装 App 与待安装包收件箱
- `res/`：共享资源
- `out/`：用户最终可取走的输出

旧安装路径 `.agent-os/` 和 `skills/` 已禁止使用。

## OS Host 指令门禁

安装完成后，用户任意指令都必须先由 ANO Host / 管理员 Agent 接管。

```bash
python ano/scripts/ano_host.py "列出应用"
python ano/scripts/ano_host.py "打开 ANO Tiandao Furnace Skill AppAgent"
python ano/scripts/ano_host.py "打开 ANO 小说工坊"
```

Host 会检查安装状态、展示权限申请和 Agent 阵容，然后停下等待用户批准。不得直接运行 App 内部脚本绕过母系统。

## 官方可选 App 包

当前 `app_packages/official/` 包含：

- `ano-calculator-skill-app_v0.1.2.zip`
- `ano-tiandao-furnace-skill-app_v0.4.0.zip`
- `ano-novel-skill-app_v0.3.1.zip`

小说 App 包含基础行文参考层、文学滤镜、独立素材采集实验室，以及素材使用度、交接、素材债务和章节开工前检查。

详见 [OFFICIAL_APPS.md](OFFICIAL_APPS.md)。

## 开发者入口

- [APP_DEVELOPER_GUIDE.md](APP_DEVELOPER_GUIDE.md)
- [SPEC.md](SPEC.md)
- [VERSIONING.md](VERSIONING.md)
- [ECOSYSTEM.md](ECOSYSTEM.md)
- [templates/APP_MANIFEST.yaml](templates/APP_MANIFEST.yaml)
- [templates/CONTEXT_PERMISSION_REQUEST.yaml](templates/CONTEXT_PERMISSION_REQUEST.yaml)

## 协议

Apache-2.0。见 [LICENSE](LICENSE)。
