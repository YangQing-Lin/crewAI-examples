import os
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from markdown_validator.tools.markdownTools import markdown_validation_tool

# 从环境变量读取 LLM 配置
# 使用 Anthropic 格式（ANTHROPIC_API_KEY + ANTHROPIC_BASE_URL）
llm = LLM(
    model=os.getenv("OPENAI_MODEL_NAME", "claude-sonnet-4-5-20250929"),
    base_url=os.getenv("ANTHROPIC_BASE_URL"),
    api_key=os.getenv("ANTHROPIC_API_KEY")
)


@CrewBase
class MarkDownValidatorCrew():
    """MarkDownValidatorCrew crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def RequirementsManager(self) -> Agent:
        return Agent(
            config=self.agents_config['Requirements_Manager'],
            tools=[markdown_validation_tool],
            allow_delegation=False,
            verbose=False,
            llm=llm
        )

    @task
    def syntax_review_task(self) -> Task:
        return Task(
            config=self.tasks_config['syntax_review_task'],
            agent=self.RequirementsManager()
        )

    @crew
    def crew(self) -> Crew:
        """Creates the MarkDownValidatorCrew crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=False,
        )
