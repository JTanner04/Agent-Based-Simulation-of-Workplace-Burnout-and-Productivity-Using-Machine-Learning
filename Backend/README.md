# Agent-Based Simulation of Workplace Burnout

## Setup

```bash
pip install -r requirements.txt
```

## MongoDB Integration

Make sure you have a MongoDB instance (local or Atlas), then:

```bash
export MONGODB_URI="mongodb+srv://<user>:<password>@cluster.mongodb.net"
```

Metrics will be inserted into the `workplace_sim.metrics` collection.

## Run Simulation

Default (CSV/JSON + Mongo):

```bash
python -m simulation.main
```

Custom steps or disable Mongo:

```bash
python -m simulation.scheduler --steps 100        # with Mongo
python -m simulation.scheduler --steps 100 --no-mongo  # no Mongo insert
```

## Testing

```bash
pytest
```

