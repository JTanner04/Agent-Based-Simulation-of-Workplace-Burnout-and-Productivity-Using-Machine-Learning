````markdown
# Backend README

This README covers only the backend components of the Workplace Simulation project.

## Overview

The backend handles simulation logic, data collection, and optional persistence to PostgreSQL. It consists of:

- **main.py**: Defines and runs the WorkplaceModel.
- **scheduler.py**: CLI entry point for configurable runs.
- **Agent definitions**: EmployeeAgent and ManagerAgent in the `simulation/agents/` package.
- **Data persistence**: Exports to CSV/JSON and writes to a PostgreSQL `metrics` table.

## Requirements

- Python 3.8+
- PostgreSQL server
- Python packages:
  - mesa
  - psycopg2-binary

## Installation

1. Clone the repo and navigate to the project root:
   ```bash
   git clone https://github.com/yourusername/workplace-simulation.git
   cd workplace-simulation
````

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate    # macOS/Linux
   venv\\Scripts\\activate   # Windows
   ```
3. Install backend dependencies:

   ```bash
   pip install mesa psycopg2-binary
   ```

## Configuration

### PostgreSQL Setup

1. Create database and user:

   ```sql
   CREATE DATABASE workplace_sim;
   CREATE USER sim_user WITH PASSWORD 'strong_password';
   GRANT ALL PRIVILEGES ON DATABASE workplace_sim TO sim_user;
   ```
2. Set the connection URL in your environment:

   ```bash
   export DATABASE_URL=\"postgresql://sim_user:strong_password@localhost:5432/workplace_sim\"
   ```

## Usage

### Running via scheduler

* **Default run (50 steps, DB enabled)**

  ```bash
  python scheduler.py
  ```
* **Custom steps**

  ```bash
  python scheduler.py --steps 100
  ```
* **Disable DB writes**

  ```bash
  python scheduler.py --no-db
  ```

### Direct invocation

```bash
python main.py
```

After execution:

* Check `exports/metrics.csv` and `exports/metrics.json` for collected data.
* If DB writes are enabled, query the `metrics` table:

  ```sql
  SELECT * FROM metrics ORDER BY run_id, step;
  ```

This README exclusively documents the backend setup and usage.

```
```
