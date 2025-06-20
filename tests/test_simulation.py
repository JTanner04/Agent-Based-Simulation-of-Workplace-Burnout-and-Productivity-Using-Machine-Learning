import pandas as pd
import pytest
from simulation.main import WorkplaceModel


def test_model_run_creates_exports(tmp_path, monkeypatch):
    # Redirect cwd to temp path
    monkeypatch.chdir(tmp_path)
    model = WorkplaceModel(num_employees=2)
    model.run_model(n_steps=2)
    csv = tmp_path / "exports" / "metrics.csv"
    json = tmp_path / "exports" / "metrics.json"
    assert csv.exists()
    assert json.exists()
    df = pd.read_csv(csv)
    assert "Avg_Stress" in df.columns
    assert len(df) == 2