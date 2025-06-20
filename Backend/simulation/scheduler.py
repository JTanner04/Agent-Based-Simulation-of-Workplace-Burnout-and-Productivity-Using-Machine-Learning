import argparse
from simulation.main import WorkplaceModel


def parse_args():
    parser = argparse.ArgumentParser(description="Run WorkplaceModel simulation")
    parser.add_argument("--steps", type=int, default=50, help="Number of steps to run")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    model = WorkplaceModel()
    model.run_model(n_steps=args.steps)
    print(f"Simulation completed for {args.steps} steps.")