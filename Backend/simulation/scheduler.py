### File: scheduler.py

import argparse
from main import WorkplaceModel


def parse_args():
    parser = argparse.ArgumentParser(description="Run WorkplaceModel simulation")
    parser.add_argument("--steps", type=int, default=50, help="Number of steps to run")
    parser.add_argument("--no-db", action="store_true", help="Disable database insertion")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    model = WorkplaceModel()
    model.run_model(n_steps=args.steps, to_db=not args.no_db)
    print(f"Simulation completed for {args.steps} steps.")
