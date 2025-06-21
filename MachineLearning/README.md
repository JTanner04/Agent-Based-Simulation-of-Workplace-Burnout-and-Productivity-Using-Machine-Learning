# 🔍 Machine Learning: Burnout Prediction

This folder contains all files related to the machine learning pipeline for predicting employee burnout based on simulation data.

## 📁 Contents

- `ml_pipeline.ipynb` – Jupyter notebook for EDA, feature engineering, model training, and evaluation
- `ml_pipeline.py` – Script version of the notebook for future integration
- `simulation_output.json` – Synthetic simulation data (agent stress, workload, etc.)
- `training_data.csv` – Flattened training dataset generated from the JSON
- `README.md` – You're here!

---

## 🧠 Objective

Train a classification model that predicts whether an employee agent will enter **burnout** based on:
- Workload
- Stress level
- Tasks completed
- (Future features: coping strategy, rolling stress avg, etc.)

The label `burned_out = 1` is derived from the agent’s simulation `state`.

---

## ⚙️ Features Used (Sprint 1)

| Feature | Type | Description |
|--------|------|-------------|
| `workload` | float | Hours of work assigned |
| `stress_level` | float | Agent's current stress |
| `tasks_completed` | int | Tasks completed that day |

---

## 🤖 Model

- **Type:** Logistic Regression (baseline)
- **Next:** Random Forest / Gradient Boosting
- **Evaluation:** Accuracy, Confusion Matrix, Visual Analysis

---

## 📊 Results (Sprint 1)

Example metrics (on synthetic data):
- Accuracy: ~XX%
- True positives: X
- False negatives: X

(Replace with your own numbers after evaluation)

---

## 🛠️ How to Run

1. Open `ml_pipeline.ipynb` in Jupyter
2. Run all cells to:
   - Load simulation data
   - Create training dataset
   - Train classifier
   - Evaluate predictions

Optional: Run `ml_pipeline.py` for non-interactive version

---

## 🔜 Future Improvements

- Add coping strategies as categorical features
- Engineer time-based features (rolling averages)
- Train a reinforcement learning model for optimal manager strategies
- Integrate model output into Streamlit dashboard

---

## 👨‍💻 Author

Created by [Jeremiah Tanner](https://github.com/JTanner04)


