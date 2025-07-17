import argparse
from main import WorkplaceModel

parser = argparse.ArgumentParser(description='Run WorkplaceModel simulation')
parser.add_argument('--steps', type=int, default=50, help='Number of simulation steps')
parser.add_argument('--team-size', type=int, default=10, help='Number of employee agents')
parser.add_argument('--work-hours', type=int, default=8, help='Hours per workday (in steps)')
parser.add_argument('--scenario', type=str, choices=['four_day_week','micromanagement'], help='Policy scenario to apply')
parser.add_argument('--batch-runs', type=int, default=1, help='Number of batch runs to aggregate')
parser.add_argument('--no-db', action='store_true', help='Disable database writes')
args = parser.parse_args()

if __name__ == '__main__':
    # batch runs
    dfs = []
    for i in range(args.batch_runs):
        model = WorkplaceModel(
            num_employees=args.team_size,
            work_hours=args.work_hours,
            scenario=args.scenario
        )
        df = model.run_model(n_steps=args.steps, to_db=not args.no_db)
        df['run'] = i+1
        dfs.append(df)
    if args.batch_runs > 1:
        import pandas as pd
        agg = pd.concat(dfs).groupby('step').mean().reset_index()
        agg.to_csv('exports/aggregated_metrics.csv', index=False)
        agg.to_json('exports/aggregated_metrics.json', orient='records')
        print(f'Batch runs completed: {args.batch_runs}. Aggregated results saved.')
    else:
        print(f'Simulation completed for {args.steps} steps.')