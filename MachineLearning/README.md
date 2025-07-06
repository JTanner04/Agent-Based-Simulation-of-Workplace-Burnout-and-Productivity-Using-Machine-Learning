# 🔍 Machine Learning: Burnout Prediction

This folder contains all files related to the machine learning pipeline for predicting employee burnout based on simulation data.

---

## 📁 Contents

- `ml_pipeline.py` – Script version of the notebook for backend integration  
- `ml_pipeline.ipynb` – Exploratory notebook with visuals, metrics, and analysis  
- `simulation_output.json` – Synthetic simulation data (agent stress, workload, etc.)  
- `training_data.csv` – Flattened training dataset generated from the simulation  
- `daily_snapshots.csv` – Daily agent-level stress, workload, and productivity metrics  
- `README.md` – You’re here!

---

## 🧠 Objective

Train a classification model to predict whether an employee agent will enter burnout based on:

- Workload  
- Stress level  
- Tasks completed  
- Engineered behavioral features  
  - Rolling average stress  
  - Change in stress  
  - Task efficiency  

The label `burned_out = 1` is derived from the agent’s simulation state.

---

## 🚀 Progress by Sprint

### ✅ **Sprint 1**
- Trained baseline **Logistic Regression**
- Exported simulation data to structured CSV
- Conducted basic EDA

### ✅ **Sprint 2**
- Switched to **Random Forest Classifier** for improved prediction
- Engineered time-based features:
  - `rolling_stress_3d`: 3-day rolling stress average  
  - `stress_delta`: change in stress level from prior day  
  - `task_efficiency`: tasks completed per workload hour
- Exported **daily agent-level snapshots** to `daily_snapshots.csv`
- Visualized:
  - Feature importance  
  - Burnout risk distribution  
  - Burnout risk curve over time

---

## 🤖 Model

| Model                  | Status       |
|------------------------|--------------|
| Logistic Regression    | ✅ Baseline   |
| Random Forest Classifier | ✅ Current   |
| Reinforcement Learning | 🔜 Planned    |

---

## 📊 Results (Sprint 2)

Example metrics on synthetic data:

- **Accuracy:** 100.00%  
- **True Positives:** 9  
- **False Negatives:** 0  

Burnout risk predictions are now available daily for each agent and visualized as both a histogram and time series trend.

---

## 🛠️ How to Run

### 🧪 Notebook:
1. Open `ml_pipeline.ipynb` in Jupyter Lab or VS Code  
2. Run all cells to:
   - Load simulation data  
   - Engineer features  
   - Train and evaluate model  
   - Visualize insights  

### ⚙️ Script:
```bash
python ml_pipeline.py
