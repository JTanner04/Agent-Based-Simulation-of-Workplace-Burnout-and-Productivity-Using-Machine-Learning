from mesa import Agent

class EmployeeAgent(Agent):
    """
    Employee agent that accumulates stress based on task load
    and has productivity that decreases with stress.
    """
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.stress = 0.0
        self.productivity = 1.0
        self.task_queue = []

    def step(self):
        # Stress increases by number of tasks
        self.stress += len(self.task_queue)
        # Productivity decreases as stress increases
        self.productivity = max(0.0, 1.0 - self.stress / 10.0)
        # Clear task queue for next step
        self.task_queue.clear()
