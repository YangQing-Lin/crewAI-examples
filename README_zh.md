# CrewAI 完整示例

## 简介
欢迎来到 **CrewAI 完整应用程序**的官方示例集合。本仓库包含端到端的实现，展示如何使用 CrewAI 框架构建真实世界的 AI Agent 编排应用程序。

> **🍳 想找特定功能的教程？** 请查看 [CrewAI Cookbook](https://github.com/crewAIInc/crewAI-cookbook)，获取针对特定 CrewAI 功能和模式的专项指南。

## 内容概览

这些是**完整的应用程序**，展示了：
- 完整的项目结构和组织方式
- 真实世界的集成模式（API、数据库、外部服务）
- 包含错误处理的完整代码实现
- 从输入到输出的端到端工作流
- 跨多个领域的行业特定实现

每个示例都是一个独立的应用程序，您可以运行、修改和部署。

**注意**：所有示例使用 **CrewAI 0.152.0 版本**和 **UV 包管理工具**，以获得最佳性能和开发体验。

## 📁 仓库结构

### 🌊 [Flows（工作流）](/flows)
使用 CrewAI Flows 进行高级编排的示例，支持复杂工作流和状态管理。

- [内容创作流](flows/content_creator_flow) - 用于博客、LinkedIn 帖子和研究报告的多 Crew 内容生成系统
- [邮件自动回复流](flows/email_auto_responder_flow) - 自动化邮件监控和回复生成
- [线索评分流](flows/lead-score-flow) - 带人工审核环节的线索质量评估
- [会议助手流](flows/meeting_assistant_flow) - 会议记录处理，集成 Trello/Slack
- [自我评估循环流](flows/self_evaluation_loop_flow) - 带自我审查的迭代式内容改进
- [用 Flows 写书](flows/write_a_book_with_flows) - 支持并行章节生成的自动化图书写作

### 👥 [Crews（团队）](/crews)
传统 CrewAI 实现，展示多 Agent 协作。

#### 内容创作与营销
- [游戏构建团队](crews/game-builder-crew) - 设计和构建 Python 游戏的多 Agent 团队
- [Instagram 帖子](crews/instagram_post) - 创意社交媒体内容生成
- [落地页生成器](crews/landing_page_generator) - 从概念到完整落地页的创建
- [营销策略](crews/marketing_strategy) - 全面的营销活动策划
- [剧本写作](crews/screenplay_writer) - 将文本/邮件转换为剧本格式

#### 商业与生产力
- [职位发布](crews/job-posting) - 自动化职位描述创建
- [会议准备](crews/prep-for-a-meeting) - 会议准备研究和策略
- [招聘](crews/recruitment) - 自动化候选人搜索和评估
- [股票分析](crews/stock_analysis) - 集成 SEC 数据的财务分析

#### 数据与研究
- [行业 Agent](crews/industry-agents) - 行业特定的 Agent 实现
- [简历职位匹配](crews/match_profile_to_positions) - 使用向量搜索的简历与职位匹配
- [Meta Quest 知识](crews/meta_quest_knowledge) - 基于 PDF 的问答系统
- [Markdown 校验器](crews/markdown_validator) - 自动化 Markdown 验证和修正

#### 旅行与规划
- [惊喜旅行](crews/surprise_trip) - 个性化惊喜旅行规划
- [行程规划](crews/trip_planner) - 目的地比较和行程优化

#### 模板
- [入门模板](crews/starter_template) - 新 CrewAI 项目的基础模板

### 🔌 [Integrations（集成）](/integrations)
展示 CrewAI 与其他平台和服务集成的示例。

- [CrewAI-LangGraph](integrations/CrewAI-LangGraph) - 与 LangGraph 框架集成
- [Azure 模型](integrations/azure_model) - 在 CrewAI 中使用 Azure OpenAI
- [NVIDIA 模型](integrations/nvidia_models) - 与 NVIDIA AI 生态系统集成

### 📓 [Notebooks（笔记本）](/Notebooks)
用于交互式探索和学习的 Jupyter 笔记本示例。

## 🚀 快速开始

1. **克隆仓库**
   ```bash
   git clone https://github.com/crewAIInc/crewAI-examples.git
   cd crewAI-examples
   ```

2. **选择示例类别**
   - 多 Crew 编排 → 查看 `/flows`
   - 标准 Crew → 查看 `/crews`
   - 平台集成 → 查看 `/integrations`

3. **导航到具体示例**
   ```bash
   cd crews/marketing_strategy  # 或其他任何示例
   ```

4. **使用 UV 安装依赖**
   ```bash
   uv sync  # 安装所有依赖并创建虚拟环境
   ```

5. **按照示例的 README 操作**
   每个示例都包含具体的设置说明和使用指南

## 📚 学习路径

### 初学者
从以下开始：
1. [入门模板](crews/starter_template) - 基础 Crew 结构
2. [Instagram 帖子](crews/instagram_post) - 简单的内容创作
3. [职位发布](crews/job-posting) - 直接的商业用例

### 中级
探索：
1. [营销策略](crews/marketing_strategy) - 多 Agent 协作
2. [自我评估循环流](flows/self_evaluation_loop_flow) - 迭代式工作流
3. [股票分析](crews/stock_analysis) - 外部 API 集成

### 高级
深入研究：
1. [内容创作流](flows/content_creator_flow) - 带动态路由的多 Crew 编排
2. [用 Flows 写书](flows/write_a_book_with_flows) - 复杂的并行执行
3. [线索评分流](flows/lead-score-flow) - 人工介入模式
4. [CrewAI-LangGraph](integrations/CrewAI-LangGraph) - 框架集成

## 🛠 常见模式

- **配置**：大多数示例使用 YAML 文件定义 Agent/任务
- **工具**：示例展示与 API、数据库和文件系统的集成
- **工作流**：高级示例演示状态管理和编排
- **训练**：多个示例包含 Agent 训练功能

## 📝 贡献

欢迎贡献！请随时提交展示新用例的示例或对现有示例的改进。

## 📄 许可证

本仓库由 CrewAI 团队维护。请查看各个示例的具体许可信息。

---

## 🔗 相关资源

- **[CrewAI 框架](https://github.com/crewAIInc/crewAI)** - CrewAI 主仓库
- **[CrewAI Cookbooks](https://github.com/crewAIInc/crewAI-cookbook)** - 功能专项教程和指南
- **[CrewAI 文档](https://docs.crewai.com)** - 完整文档
- **[CrewAI 社区](https://community.crewai.com)** - 加入社区讨论

## 使用 uv 管理环境（推荐）

[uv](https://github.com/astral-sh/uv) 是新一代 Python 包管理器，比 pip 快 10-100 倍，可完全替代 conda + pip 组合。

### 安装 uv

```bash
# Linux / macOS
curl -LsSf https://astral.sh/uv/install.sh | sh

# 或使用 pip
pip install uv
```

### 配置代理加速（可选）

如果你有代理服务器，可配置环境变量加速 GitHub 和 PyPI 访问：

```bash
# 临时使用（当前终端生效）
export HTTP_PROXY=http://192.168.2.52:7897
export HTTPS_PROXY=http://192.168.2.52:7897

# 永久配置（写入 shell 配置文件）
echo 'export HTTP_PROXY=http://192.168.2.52:7897' >> ~/.bashrc
echo 'export HTTPS_PROXY=http://192.168.2.52:7897' >> ~/.bashrc
source ~/.bashrc
```

### 配置 PyPI 镜像源（可选）

国内用户可配置镜像源加速包下载：

```bash
# 临时使用
uv pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple

# 永久配置（环境变量）
export UV_INDEX_URL=https://mirrors.aliyun.com/pypi/simple

# 或全局配置文件 ~/.config/uv/uv.toml
# index-url = "https://mirrors.aliyun.com/pypi/simple"
```

常用镜像源：
- 阿里云：`https://mirrors.aliyun.com/pypi/simple`
- 清华：`https://pypi.tuna.tsinghua.edu.cn/simple`
- 腾讯：`https://mirrors.cloud.tencent.com/pypi/simple`

### 快速开始 crewAI-examples

```bash
# 1. 克隆仓库
git clone https://github.com/crewAIInc/crewAI-examples.git
cd crewAI-examples

# 2. 安装 Python 3.11（如系统未安装）
uv python install 3.11

# 3. 创建虚拟环境
uv venv --python 3.11

# 4. 激活环境
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows

# 5. 安装依赖
uv pip install -r requirements.txt

# 6. 运行示例
cd crews/marketing_strategy
uv pip install -r requirements.txt  # 如有额外依赖
python src/marketing_strategy/main.py
```

### 单个示例项目的标准流程

```bash
# 进入示例目录
cd crews/marketing_strategy

# 使用 uv sync 自动创建环境并安装依赖
uv sync

# 运行
uv run run_crew
```

### uv 常用命令速查

| 命令 | 说明 |
|------|------|
| `uv python install 3.11` | 安装 Python 3.11 |
| `uv python list` | 列出已安装的 Python 版本 |
| `uv venv` | 创建虚拟环境 |
| `uv pip install pkg` | 安装包 |
| `uv pip install -r req.txt` | 从 requirements.txt 安装 |
| `uv add pkg` | 添加依赖到 pyproject.toml |
| `uv sync` | 同步 pyproject.toml 依赖 |
| `uv run cmd` | 在虚拟环境中运行命令 |