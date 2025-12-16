# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is the official CrewAI examples repository containing complete end-to-end applications demonstrating AI agent orchestration. All examples use **CrewAI 0.152.0** and **UV package manager**.

## Conda Environment

本项目使用 conda 环境 `crew-ai` 管理依赖：

```bash
# 环境已创建，包含 crewai 1.7.0 + crewai-tools
# 所有命令通过 conda run 执行，无需手动 activate

# 验证安装
conda run -n crew-ai python -c "import crewai; print(crewai.__version__)"
```

## Common Commands

```bash
# 使用 conda run 执行命令（推荐）
conda run -n crew-ai python -m marketing_posts.main        # 运行 crew
conda run -n crew-ai python -m self_evaluation_loop_flow.main  # 运行 flow

# 或使用 uv（需进入具体示例目录）
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

Most examples require API keys in `.env`:
```
OPENAI_API_KEY=...
SERPER_API_KEY=...  # for web search tools
```

Check each example's `.env.example` for specific requirements.
