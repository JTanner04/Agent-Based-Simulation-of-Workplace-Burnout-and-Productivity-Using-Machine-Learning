"""
employee.py

Defines the employee agent, which tracks stress & productivity.
"""

#TODO: Integrate human features like resilience, coping mechanisms, and social support.
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
        """Apply stress based on task, adjust productivity accordingly, and then clears tasks"""

        # PTO Handling
        if self.pto_left > 0:
            self.stress = max(0.0, self.stress - self.resilience * 2)
            self.pto_left -= 1
            return  # Skip stress and productivity adjustment if on PTO
        
        # Scheduled Breaks (Every 8-step cycle)
        if self.model.current_step % 8 == 4:
            self.stress = max(0.0, self.stress - self.resilience * 0.5)
        
        # Workload Stress Handling
        workload = len(self.task_queue)
        self.stress += workload * (1 - self.resilience)  # Stress increases with workload and resilience factor

        # Ventening: pair with random sociable employee
        peers = [agent for agent in self.model.schedule.agents if isinstance(agent, EmployeeAgent) and agent.unique_id != self.unique_id]
        if peers and self.sociability > 0.5:
            peer = random.choice(peers)
            relief = min(self.stress, peer.sociability * 0.1)
            self.stress = max(0.0, self.stress - relief)
            peer.stress = max(0.0, peer.stress - relief)
        
        # Mentorship: pair with a random employee for advice (10 steps)
        if self.model.current_step % 10 == 0 and peers:
            mentors = [agent for agent in peers if agent.stress < self.stress and agent.unique_id != self.unique_id]
            if mentors:
                mentor = min(mentors, key=lambda x: x.stress)
                self.stress = max(0.0, self.stress - mentor.resilience)
                mentor.productivity = min(1.0, mentor.productivity + 0.05)  # Mentor's productivity increases slightly
        
        # Increase fatigue
        self.fatigue += workload * (1 - self.work_life_balance)

        # Sleep recovery (24 steps)
        if self.model.current_step % 24 >= 18:
            self.sleep_level = min(1.0, self.sleep_level + 0.2)  # Sleep level recovers at night
            self.fatigue = max(0.0, self.fatigue - 0.5)  # Fatigue decreases slightly at night

        # Stress reduction from sleep
        self.stress = max(0.0, self.stress - self.sleep_level * 0.1)

        # Productivity adjustment based on stress and fatigue
        self.productivity = max(0.0, 1.0 - self.stress / 10.0) #should it be 1 - self.stress, or just self.stress / 10.0?
        self.task_queue.clear()
