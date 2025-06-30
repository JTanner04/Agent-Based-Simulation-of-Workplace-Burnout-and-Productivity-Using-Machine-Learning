"""
employee.py

Defines the employee agent, which tracks stress & productivity.
"""

#TODO: Integrate human features like resilience, coping mechanisms, and social support.

from mesa import Agent

class EmployeeAgent(Agent):
    """An employee who changes productivity based on amount of stress"""


    def __init__(self, unique_id, model):
        """Initializes stress, productivity, and task queue."""
        super().__init__(unique_id, model)
        self.stress = 0.0
        self.productivity = 1.0
        self.task_queue = []

    def step(self):
        """Apply stress based on task, adjust productivity accordingly, and then clears tasks"""

        # Stress increases based on their number of tasks
        self.stress += len(self.task_queue)

        # Productivity declines as stress increases, but it never goes below 0
        self.productivity = max(0.0, 1.0 - self.stress / 10.0)
        self.task_queue.clear()
