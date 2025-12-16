# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is the official CrewAI examples repository containing complete end-to-end applications demonstrating AI agent orchestration. All examples use **CrewAI 0.152.0** and **UV package manager**.

## macOS 环境配置

### Conda 安装路径

macOS (Apple Silicon) 下 conda 安装位置：
```
/opt/homebrew/anaconda3
```

如果 shell 中 `conda` 命令不可用，使用完整路径：
```bash
/opt/homebrew/anaconda3/bin/conda <command>
```

### 环境初始化

首次使用需创建 conda 环境：
```bash
# 创建环境（Python 3.11）
/opt/homebrew/anaconda3/bin/conda create -n crew-ai python=3.11 -y

# 安装依赖
/opt/homebrew/anaconda3/bin/conda run -n crew-ai pip install crewai crewai-tools
```

### Conda 环境

本项目使用 conda 环境 `crew-ai` 管理依赖：

```bash
# 环境位置：/opt/homebrew/anaconda3/envs/crew-ai
# 包含 crewai 1.7.1 + crewai-tools
# 所有命令通过 conda run 执行，无需手动 activate

# 验证安装
conda run -n crew-ai python -c "import crewai; print(crewai.__version__)"

# 或使用完整路径
/opt/homebrew/anaconda3/bin/conda run -n crew-ai python -c "import crewai; print(crewai.__version__)"
```

## 运行示例

### 方式一：conda run（推荐）

无需手动 activate 环境，直接执行：
```bash
# 运行 crews 目录下的示例
conda run -n crew-ai python crews/marketing_strategy/src/marketing_strategy/main.py

# 运行 flows 目录下的示例
conda run -n crew-ai python flows/self_evaluation_loop_flow/src/self_evaluation_loop_flow/main.py

# 使用完整 conda 路径（shell 未初始化时）
/opt/homebrew/anaconda3/bin/conda run -n crew-ai python <script_path>
```

### 方式二：激活环境后运行

```bash
# 激活环境
conda activate crew-ai

# 运行示例
python crews/marketing_strategy/src/marketing_strategy/main.py

# 退出环境
conda deactivate
```

### 方式三：uv（进入具体示例目录）

```bash
cd crews/marketing_strategy
uv sync                    # 安装依赖
uv run run_crew            # 运行
uv run train <n_iterations> # 训练
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
