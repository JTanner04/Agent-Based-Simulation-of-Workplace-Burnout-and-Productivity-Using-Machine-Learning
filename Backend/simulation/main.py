"""
main.py

houses the main functions of the WorkplaceModel, calculations and (optionally) postgreSQL db

"""

import os
import psycopg2
from datetime import datetime
from mesa import Model
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector

from agents.employee import EmployeeAgent
from agents.manager import ManagerAgent

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/workplace_sim")

class WorkplaceModel(Model):
    """Agent-based model of workplace stress and productivity.

    Employees gain stress based on the tasks set by the manager and 
    productivity reduces as a result. THe results are collected and then 
    can be sent to PostgreSQL database.

    """
    def __init__(self, num_employees=10) -> None:
        """Create a new Model
        
        Args:
            num_employees (int): Number of EmployeeAgent instances to intialize
        """
        super().__init__()
        self.num_employees = num_employees
        self.schedule = RandomActivation(self)
        self.current_step = 0
        # Add a manager
        manager = ManagerAgent(0, self)
        self.schedule.add(manager)

        # Create Employees
        for i in range(1, num_employees + 1):
            employee = EmployeeAgent(i, self)
            self.schedule.add(employee)


        self.datacollector = DataCollector(
            model_reporters={
                "Avg_Stress": lambda m: m.compute_avg_stress(),
                "Avg_Productivity": lambda m: m.compute_avg_productivity(),
            }
        )

    def compute_avg_stress(self) -> float:
        """Computes the average stress across all employees

        Returns:
            float: Mean stress level, or 0.0 if no stress data available
        """
        stresses = [agent.stress for agent in self.schedule.agents if hasattr(agent, 'stress')]
        return sum(stresses) / len(stresses) if stresses else 0.0

    def compute_avg_productivity(self) -> float:
        """Computes the average productivity across all employees

        Returns:
            float: Mean productivity level, or 0.0 if no productivity data available
        """
        products = [agent.productivity for agent in self.schedule.agents if hasattr(agent, 'productivity')]
        return sum(products) / len(products) if products else 0.0

    def step(self) -> None:
        """Advance by one step, collect data and then activating agents"""
        self.datacollector.collect(self)
        self.schedule.step()
        self.current_step += 1

    def run_model(self, n_steps=50, to_db=True) -> None:
        """Runs the simulation for a fixed number of steps and exports results

        Args:
            n_steps (int): Number of simulation steps to execute.
            to_db (bool): If True, send the collected data into PostgreSQL

        """

        # Run the steps
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


        if to_db:
            records = df.reset_index().rename(columns={"index": "step"}).to_dict("records")
            run_id = datetime.utcnow()
            conn = psycopg2.connect(DATABASE_URL)
            cur = conn.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS metrics (
                    run_id TIMESTAMP,
                    step INTEGER,
                    Avg_Stress REAL,
                    Avg_Productivity REAL
                )
            """)
            insert_query = "INSERT INTO metrics (run_id, step, Avg_Stress, Avg_Productivity) VALUES (%s, %s, %s, %s)"
            data_to_insert = [(run_id, rec["step"], rec["Avg_Stress"], rec["Avg_Productivity"]) for rec in records]
            cur.executemany(insert_query, data_to_insert)
            conn.commit()
            cur.close()
            conn.close()

if __name__ == "__main__":
    model = WorkplaceModel()
    model.run_model()
    print("Simulation completed.")
