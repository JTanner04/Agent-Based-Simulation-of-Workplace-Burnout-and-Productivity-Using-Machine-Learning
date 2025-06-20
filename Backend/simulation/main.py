from mesa import Model
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector
import os

from simulation.agents.employee import EmployeeAgent
from simulation.agents.manager import ManagerAgent


class WorkplaceModel(Model):
    """A workplace model with employees and a manager."""
    def __init__(self, num_employees=10):
        super().__init__()
        self.num_employees = num_employees
        self.schedule = RandomActivation(self)

        # Instantiate manager
        manager = ManagerAgent(0, self)
        self.schedule.add(manager)

        # Instantiate employee agents
        for i in range(1, num_employees + 1):
            employee = EmployeeAgent(i, self)
            self.schedule.add(employee)

        # Set up data collector
        self.datacollector = DataCollector(
            model_reporters={
                "Avg_Stress": lambda m: m.compute_avg_stress(),
                "Avg_Productivity": lambda m: m.compute_avg_productivity(),
            }
        )

    def compute_avg_stress(self):
        stresses = [agent.stress for agent in self.schedule.agents if hasattr(agent, 'stress')]
        return sum(stresses) / len(stresses) if stresses else 0

    def compute_avg_productivity(self):
        products = [agent.productivity for agent in self.schedule.agents if hasattr(agent, 'productivity')]
        return sum(products) / len(products) if products else 0

    def step(self):
        """Advance the model by one step."""
        self.datacollector.collect(self)
        self.schedule.step()

    def run_model(self, n_steps=50):
        """Run the model for n_steps, then export metrics to CSV/JSON."""
        for _ in range(n_steps):
            self.step()

        # Export collected data
        df = self.datacollector.get_model_vars_dataframe()
        output_dir = os.path.join(os.getcwd(), "exports")
        os.makedirs(output_dir, exist_ok=True)
        df.to_csv(os.path.join(output_dir, "metrics.csv"))
        df.to_json(os.path.join(output_dir, "metrics.json"))


if __name__ == "__main__":
    # Run a default simulation
    model = WorkplaceModel()
    model.run_model()
    print("Simulation completed. Metrics saved to exports/metrics.csv and exports/metrics.json")
