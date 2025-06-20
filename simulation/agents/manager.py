import random
from mesa import Agent
from simulation.agents.employee import EmployeeAgent

class ManagerAgent(Agent):
    """
    Manager agent that assigns tasks to employees.
    """
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

    def step(self):
        # Assign random tasks (1-5) to each employee
        for agent in self.model.schedule.agents:
            if isinstance(agent, EmployeeAgent):
                num_tasks = random.randint(1, 5)
                agent.task_queue.extend(range(num_tasks))
