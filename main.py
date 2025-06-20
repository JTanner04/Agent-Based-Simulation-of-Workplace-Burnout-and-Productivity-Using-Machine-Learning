from mesa import Model
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector
import os
from pymongo import MongoClient
from datetime import datetime

from simulation.agents.employee import EmployeeAgent
from simulation.agents.manager import ManagerAgent

# MongoDB setup
MONGO_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)
db = client["workplace_sim"]
metrics_col = db["metrics"]

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

    def run_model(self, n_steps=50, to_mongo=True):
        """Run the model for n_steps, export CSV/JSON, and optionally push to MongoDB."""
        for _ in range(n_steps):
            self.step()

        # Export to files
        df = self.datacollector.get_model_vars_dataframe()
        output_dir = os.path.join(os.getcwd(), "exports")
        os.makedirs(output_dir, exist_ok=True)
        csv_path = os.path.join(output_dir, "metrics.csv")
        json_path = os.path.join(output_dir, "metrics.json")
        df.to_csv(csv_path)
        df.to_json(json_path)
        print(f"Saved CSV to {csv_path} and JSON to {json_path}")

        # Insert into MongoDB
        if to_mongo:
            records = df.reset_index().rename(columns={"index": "step"}).to_dict("records")
            run_id = datetime.utcnow().isoformat()
            for rec in records:
                rec["run_id"] = run_id
            metrics_col.insert_many(records)
            print(f"Inserted {len(records)} records into MongoDB collection 'metrics'")


if __name__ == "__main__":
    # Run a default simulation
    model = WorkplaceModel()
    model.run_model()
    print("Simulation completed.")
