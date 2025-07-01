"""
manager.py

Defines the manager agent, which gives tasks to employees on each step. 

"""

#TODO: Implement humanziation features like leadership style and communication skills.

import random
from mesa import Agent
from agents.employee import EmployeeAgent


class ManagerAgent(Agent):
    """An agent that assigns work to the EmployeeAgents"""

    def __init__(self, unique_id, model):
        """Intializes the ManagerAgent

        Args:
            unique_id (int): Unique identifier for this agent
            mode (Model): Referesnce to the simulation model

        """
        super().__init__(unique_id, model)

    def step(self):
        """Gives a random number of tasks to every EmployeeAgent
        
        For each employee agent in the sachedule, generate 1 to 5 tasks
        and add them to the employees queue. 
        """

        for agent in self.model.schedule.agents:
            if isinstance(agent, EmployeeAgent):
                num_tasks = random.randint(1, 5)
                # Give each task a number
                agent.task_queue.extend(range(num_tasks))
