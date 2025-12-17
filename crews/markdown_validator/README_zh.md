# AI Crew 用于审查 Markdown 语法

## 简介
本项目演示如何使用 CrewAI 框架自动化审查 Markdown 文件的语法问题。通用助手 Agent 利用自定义工具获取 Markdown 语法错误列表，然后将这些错误汇总为文档修改建议。

## 运行脚本

本示例使用 OpenAI API 调用模型。可以通过本地部署的方案（如 LM Studio）或使用 API Key 连接 OpenAI API 端点。

### 使用 uv 运行（推荐）

```bash
# 进入项目目录
cd crews/markdown_validator

# 安装依赖
uv sync

# 运行示例
uv run markdown_validator

# 带训练运行
uv run train <n_iterations>
```

### 环境配置

将 `.env.example` 重命名为 `.env`，配置模型、端点 URL 和 API Key。

## 项目结构

```
markdown_validator/
├── src/markdown_validator/
│   ├── main.py           # 入口文件
│   ├── crew.py           # Crew 定义（@agent/@task/@crew 装饰器）
│   ├── config/
│   │   ├── agents.yaml   # Agent 配置（role/goal/backstory）
│   │   └── tasks.yaml    # Task 配置
│   └── tools/
│       └── markdownTools.py  # 自定义 Markdown 验证工具
```

## 核心概念

| 组件 | 说明 |
|------|------|
| `@CrewBase` | 标记 Crew 类 |
| `@agent` | 定义 Agent 方法 |
| `@task` | 定义 Task 方法 |
| `@crew` | 组装 Crew |

## 许可证
本项目基于 MIT 许可证发布。
