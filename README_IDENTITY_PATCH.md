# README Identity Patch

Codex should insert the following section near the top of `README.md`, preferably after the opening description and before "Why this project exists".

```md
## Repository identity

Agent-Native OS is **spec-first** and **natural-language-first**.

This repository is primarily a set of Markdown/YAML architecture specifications, workspace protocols, and demo contracts. Its core idea is not "Python code runs agents." Its core idea is:

> Contracted natural language is source code.  
> Context Kernel is the runtime.  
> Structured output is the Context ABI.

The small Python scripts in `scripts/` are reference helpers for demo checks and workspace validation. They are not the main implementation language of Agent-Native OS.
```

Codex should insert the following section near the top of `README.zh-CN.md`:

```md
## 仓库身份说明

Agent-Native OS 是 **规范优先**、**自然语言优先** 的项目。

这个仓库主要由 Markdown/YAML 架构规范、工作区协议和 demo 契约组成。它的核心不是“用 Python 代码运行 Agent”，而是：

> 契约化自然语言是源代码。  
> 上下文内核是运行时。  
> 结构化输出是 Context ABI。

`scripts/` 里的少量 Python 脚本只是 demo 检查和工作区验证工具，不是 Agent-Native OS 的主体实现语言。
```
