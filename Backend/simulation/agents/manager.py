"""
manager.py

Defines the manager agent, which gives tasks to employees on each step. 

"""

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

        #Leader traits
        self.compassion = random.uniform(0.0, 1.0)
        self.fairness = random.uniform(0.0, 1.0)
        self.motivativational_skills = random.uniform(0.0, 1.0)
        self.assign_history = {}  # Track task assignments to employees

    def step(self):
        """Gives a random number of tasks to every EmployeeAgent
        
        For each employee agent in the sachedule, generate 1 to 5 tasks
        and add them to the employees queue. 
        """
        employees = [agent for agent in self.model.schedule.agents if isinstance(agent, EmployeeAgent)]
        employees.sort(key = lambda e: self.assign_history.get(e.unique_id, 0))
        

        for employee in employees:
            base_load = random.randint(1, 5)  # Base number of tasks
            # Fairness adjustment
            fair_adgustment = int((sum(self.assign_history.get(e.unique_id, 0) for e in employees) / len(employees)) - 
                                  self.assign_history.get(employee.unique_id, 0)*self.fairness)
            num_tasks = max(0, base_load + fair_adgustment)
            employee.task_queue.extend(range(num_tasks))
            self.assign_history[employee.unique_id] = self.assign_history.get(employee.unique_id, 0) + num_tasks
        
        # Compassionate check
        for employee in employees:
            if employee.stress > employee.resilience * 5 and random.random() < self.compassion:
                employee.stress = max(0.0, employee.stress - self.compassion * employee.resilience * 2)

        #Motivational boost
        if random.random() < self.motivativational_skills * 0.05:
            target_employee = random.choice(employees)
            target_employee.productivity = min(1.0, target_employee.productivity + 0.1)

