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
        super().init(unique_id, model)
        # leadership
        self.compassion=random.random()
        self.fairness=random.random()
        self.micromanage= (model.scenario=='micromanagement')
        self.assign_count={}

    def step(self):
        day = (self.model.current_step // self.model.work_hours) % 7
        emps = [a for a in self.model.schedule.agents if isinstance(a, EmployeeAgent)]
        # apply fairness sort
        emps.sort(key=lambda e: self.assign_count.get(e.unique_id, 0))
        for emp in emps:
            if self.model.scenario == 'four_day_week' and day >= 4:
                num = 0
            else:
                base = random.randint(1, 5)
                if self.micromanage:
                    base += random.randint(1, 5)
                # fairness adjust
                fair_adj = int(
                    (sum(self.assign_count.get(e.unique_id, 0) for e in emps) / len(emps) - self.assign_count.get(emp.unique_id, 0))
                    * self.fairness
                )
                num = max(0, base + fair_adj)
            emp.task_queue.extend(range(num))
            self.assign_count[emp.unique_id] = self.assign_count.get(emp.unique_id, 0) + num
        # compassion relief
        for emp in emps:
            if emp.stress > emp.resilience * 5 and random.random() < self.compassion:
                emp.stress = max(0.0, emp.stress - self.compassion * emp.resilience * 2)

