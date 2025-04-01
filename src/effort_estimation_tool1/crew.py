from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class EffortEstimationTool():
    """EffortEstimationTool crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def sow_processor(self) -> Agent:
        return Agent(config=self.agents_config['sow_processor'], verbose=True)

    @agent
    def business_analyst(self) -> Agent:
        return Agent(config=self.agents_config['business_analyst'], verbose=True)

    @agent
    def technical_estimator(self) -> Agent:
        return Agent(config=self.agents_config['technical_estimator'], verbose=True)

    @agent
    def qa_specialist(self) -> Agent:
        return Agent(config=self.agents_config['qa_specialist'], verbose=True)

    @agent
    def project_manager(self) -> Agent:
        return Agent(config=self.agents_config['project_manager'], verbose=True)

    @agent
    def proposal_generator(self) -> Agent:
        return Agent(config=self.agents_config['proposal_generator'], verbose=True)

    @agent
    def output_formatter(self) -> Agent:
        return Agent(config=self.agents_config['output_formatter'], verbose=True)

    @task
    def sow_processing_task(self) -> Task:
        return Task(config=self.tasks_config['sow_processing_task'])

    @task
    def requirement_analysis_task(self) -> Task:
        return Task(config=self.tasks_config['requirement_analysis_task'])

    @task
    def decomposition_task(self) -> Task:
        return Task(config=self.tasks_config['decomposition_task'])

    @task
    def effort_estimation_task(self) -> Task:
        return Task(config=self.tasks_config['effort_estimation_task'])

    @task
    def qa_estimation_task(self) -> Task:
        return Task(config=self.tasks_config['qa_estimation_task'])

    @task
    def aggregation_task(self) -> Task:
        return Task(config=self.tasks_config['aggregation_task'])

    @task
    def proposal_generation_task(self) -> Task:
        return Task(config=self.tasks_config['proposal_generation_task'])

    @task
    def output_formatting_task(self) -> Task:
        return Task(
            config=self.tasks_config['output_formatting_task'],
            output_file='effort_estimation_report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the EffortEstimationTool crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )