# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is the official CrewAI examples repository containing complete end-to-end applications demonstrating AI agent orchestration. All examples use **CrewAI 0.152.0** and **UV package manager**.

## 运行示例

本项目统一使用 uv 管理依赖，进入具体示例目录后执行：

```bash
cd crews/markdown_validator
uv sync                    # 安装依赖
uv run markdown_validator  # 运行
uv run train <n_iterations> # 训练
```

### 虚拟环境（uv 特性）

**重要：uv 创建的虚拟环境与传统 venv 不同！**

- `.venv/bin/` 中**没有 pip**，只有 python 符号链接
- 安装包必须用 `uv pip install`，不能用 `.venv/bin/pip`
- 每个子项目（如 `crews/markdown_validator/`）有独立的 `.venv`
- 类型检查、lint 等工具需要从**子项目目录**运行，以正确解析依赖

```bash
# ❌ 错误用法
.venv/bin/pip install pyright          # uv 虚拟环境没有 pip
pyright src/                           # 找不到项目依赖

# ✅ 正确用法
uv pip install pyright                 # 用 uv 安装包
cd crews/markdown_validator && uv run pyright src/  # 从子项目目录运行
```

### 常用命令

```bash
# 安装依赖（在子项目目录执行）
cd crews/markdown_validator
uv sync

# 运行示例
uv run markdown_validator

# 安装开发工具
uv pip install pyright ruff

# 类型检查（必须从子项目目录运行）
uv run pyright src/

# Lint 检查
uv run ruff check src/

# 直接运行 Python 文件
uv run python src/<project>/main.py
```

### 代理设置

网络受限时，设置代理加速下载：

```bash
export HTTP_PROXY=http://192.168.2.52:7897
export HTTPS_PROXY=http://192.168.2.52:7897
uv pip install <package>
```

## Architecture

### Directory Structure
- `/crews` - Traditional multi-agent crews (single crew, multiple agents)
- `/flows` - Advanced orchestration with state management (multiple crews)
- `/integrations` - Third-party platform integrations (Azure, NVIDIA, LangGraph)
- `/notebooks` - Jupyter notebook tutorials

### Crew Pattern (crews/)
Standard project layout:
```
crew_name/
├── pyproject.toml          # Dependencies and CLI scripts
├── src/crew_name/
│   ├── main.py             # Entry point with run()/train() functions
│   ├── crew.py             # @CrewBase class with @agent/@task/@crew decorators
│   └── config/
│       ├── agents.yaml     # Agent definitions (role, goal, backstory)
│       └── tasks.yaml      # Task definitions
```

Key classes:
- `@CrewBase` decorator on crew class
- `@agent` methods return `Agent()` with config from YAML
- `@task` methods return `Task()` with optional `output_json` for structured output
- `@crew` method returns `Crew()` with `Process.sequential` or `Process.hierarchical`

### Flow Pattern (flows/)
Flows orchestrate multiple crews with state:
```
flow_name/
├── src/flow_name/
│   ├── main.py             # Flow class with @start/@listen/@router decorators
│   └── crews/              # Embedded crew definitions
│       ├── crew_a/
│       └── crew_b/
```

Key decorators:
- `@start("event_name")` - Entry point or retry trigger
- `@listen("event_name")` - React to events
- `@router(method)` - Conditional routing, returns event name string

Flow state uses Pydantic `BaseModel` subclass passed to `Flow[StateClass]`.

### Tools
Common tools from `crewai_tools`:
- `SerperDevTool()` - Web search
- `ScrapeWebsiteTool()` - Web scraping

Custom tools extend `BaseTool` with `_run()` method.

## Environment Variables

示例需要的 API keys 配置在 `.env` 文件中：
```bash
OPENAI_API_KEY=sk-xxx
SERPER_API_KEY=xxx          # 用于 SerperDevTool 搜索
ANTHROPIC_API_KEY=xxx       # 如果使用 Claude 模型
```

各示例的具体配置参考其目录下的 `.env.example` 文件。
