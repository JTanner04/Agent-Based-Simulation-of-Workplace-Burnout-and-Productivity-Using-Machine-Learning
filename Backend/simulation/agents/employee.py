"""
employee.py

Defines the employee agent, which tracks stress & productivity.
"""
import random
from mesa import Agent

class EmployeeAgent(Agent):
    """An employee who changes productivity based on amount of stress"""


    def __init__(self, unique_id, model):
        """Initializes stress, productivity, and task queue."""
        super().__init__(unique_id, model)
        self.stress = 0.0
        self.productivity = 1.0
        self.task_queue = []

        # Personaity traits
        self.resilience = random.uniform(0.0, 1.0)
        self.sociability = random.uniform(0.0, 1.0)

        # Buffers
        self.sleep_level = random.uniform(0.5, 1.0)  # Sleep level from 0(exhausted) to 1(fully rested)  
        self.work_life_balance = random.uniform(0.0, 1.0)  # Work-life balance from 0(bad) to 1(good)
        self.pto_left = 0
        self.fatigue = 0.0 


    def step(self):
        # determine day index for scenarios
        day = (self.model.current_step // self.model.work_hours) % 7
        # scenario: four-day week
        if self.model.scenario == 'four_day_week' and day >= 4:
            self.stress = max(0.0, self.stress - self.resilience*2)
            return
        # PTO
        if self.pto_left > 0:
            self.stress = max(0.0, self.stress - self.resilience*2)
            self.pto_left -= 1
            return
        # scheduled break at half workday
        if self.model.current_step % self.model.work_hours == self.model.work_hours//2:
            self.stress = max(0.0, self.stress - self.resilience*0.5)
        # accumulate stress
        self.stress += len(self.task_queue)*(1-self.resilience)
        # venting interact
        if self.sociability > 0.5:
            peers = [a for a in self.model.schedule.agents if isinstance(a, EmployeeAgent) and a != self]
            if peers:
                buddy = random.choice(peers)
                relief = buddy.sociability * 0.1
                self.stress = max(0.0, self.stress - relief)
                buddy.stress = max(0.0, buddy.stress - relief)
        # recovery from sleep
        self.stress = max(0.0, self.stress - self.sleep_level * 0.1)
        # update productivity
        self.productivity = max(0.0, 1 - self.stress / 10)
        self.task_queue.clear()
