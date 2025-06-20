# Agent-Based Simulation of Workplace Burnout

## Setup

```
pip install -r requirements.txt
```

## Run Simulation

```
python -m simulation.main  # defaults to 10 employees, 50 steps
```
or with custom steps:

```
python -m simulation.scheduler --steps 100
```

Outputs will be in `exports/metrics.csv` and `exports/metrics.json`.

## Testing

```
pytest
```
