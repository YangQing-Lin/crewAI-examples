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
    agents_config: dict = 'config/agents.yaml'  # type: ignore[assignment]
    tasks_config: dict = 'config/tasks.yaml'  # type: ignore[assignment]

    @agent
    def RequirementsManager(self) -> Agent:
        return Agent(  # type: ignore[call-arg]
            config=self.agents_config['Requirements_Manager'],
            tools=[markdown_validation_tool],
            allow_delegation=False,
            verbose=False,
            llm=llm
        )

    @task
    def syntax_review_task(self) -> Task:
        return Task(
            config=self.tasks_config['syntax_review_task'],  # type: ignore[arg-type]
            agent=self.RequirementsManager(),  # type: ignore[call-arg]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the MarkDownValidatorCrew crew"""
        return Crew(
            agents=self.agents,  # type: ignore[attr-defined]
            tasks=self.tasks,  # type: ignore[attr-defined]
            process=Process.sequential,
            verbose=False,
        )
