# 🧠 Agent-Based Simulation of Workplace Burnout & Productivity

## 📌 Project Title  
**Agent-Based Simulation of Workplace Burnout and Productivity Using Machine Learning**

## 🚦 Project Status  
-  **Sprint 1:** Core Simulation MVP – *Complete*  
-  **Sprint 2:** Behavioral Complexity + UI MVP – *Complete*
-  **Sprint 3:** ML Model + Scenario Tuning – *Complete*
-  **Sprint 4:** Final Polish & Deployment – *Complete*

---

## 📘 Project Overview

This project simulates a dynamic workplace using agent-based modeling. Employee agents have distinct workloads, personalities, stress thresholds, and coping strategies. The goal is to evaluate how changes in team structure, workload distribution, and mental health interventions impact productivity, morale, and burnout over time.

---

## 🧠 Tech Stack

| Layer                  | Technologies |
|------------------------|--------------|
| Simulation Engine      | Python, [Mesa](https://mesa.readthedocs.io/en/stable/) |
| Frontend Dashboard     | Streamlit, Plotly, Matplotlib |
| Machine Learning       | scikit-learn, PyTorch, Stable-Baselines3 |
| Database               | PostgreSQL (via psycopg2), CSV/JSON |
| API (Optional)         | FastAPI |
| Deployment             | Docker, Heroku, Hugging Face Spaces, AWS EC2 |
| CI/CD                  | GitHub Actions |
| Bonus Tools            | LangChain, OpenAI, PDFKit, Bokeh |

---

## 🚀 Deployment Recommendations

- **MVP:** Use Heroku or Hugging Face Spaces for quick deployment
- **Scale:** Containerize with Docker, deploy to AWS EC2, use PostgreSQL RDS
- **CI/CD:** Automate builds and deployments via GitHub Actions

---

## 👥 Team Roles

### 🧠 Simulation & Backend Lead — *Cornell*
- Develop Mesa simulation engine
- Implement agent logic (stress → burnout), recovery, and task management
- Export and persist data to CSV/JSON + PostgreSQL
- (Optional) Create REST endpoints using FastAPI

**Deliverables:**
- `simulation/` logic  
- Exported data sets  
- PostgreSQL schema + script  
- Unit tests

---

### 📊 ML & Data Analyst — *Jeremiah*
- Conduct EDA on simulation outputs
- Train burnout prediction models (Logistic Regression, Random Forest, etc.)
- (Optional) Implement RL manager agent via Stable-Baselines3
- Create data preprocessing pipelines + visual insights

**Deliverables:**
- `machine_learning/` directory  
- `ml_pipeline.ipynb` + `.py` script  
- Model artifacts + metrics  
- Risk prediction visualizations

---

### 🖥️ Frontend & DevOps Engineer — *Kzaiah*
- Build Streamlit dashboard with HR controls, visual metrics, and scenario toggles
- Implement PostgreSQL save/load functionality
- Containerize with Docker, deploy via Heroku/Hugging Face
- Configure GitHub Actions for CI/CD

**Deliverables:**
- `streamlit_app.py` + components  
- `Dockerfile`, deployment configs  
- Live dashboard + user instructions

---

## 🗓️ Sprint Plan (June 19 – August 8, 2025)

| Sprint | Dates             | Focus                         | Key Goals |
|--------|-------------------|-------------------------------|-----------|
| 🏁 Sprint 1 | Jun 19 – Jun 30 | Core Simulation MVP            | Agent logic, data export, DB storage |
| 🔄 Sprint 2 | Jul 1 – Jul 12  | Behavioral Complexity + UI     | Coping logic, personalities, UI toggle controls |
| 🧠 Sprint 3 | Jul 13 – Jul 24 | ML + Scenario Tuning             | Train classifier, (optional) RL agent, scenario testing |
| 🚀 Sprint 4 | Jul 25 – Aug 8  | Final Polish & Deployment      | Testing, Docker, deployment, polish, reporting |

---

### ✅ Sprint Highlights

#### Sprint 1: Core Simulation MVP
- Mesa agent logic (stress, burnout)
- Export to JSON/CSV
- PostgreSQL schema + storage
- Basic Streamlit scaffold
- ML: Burnout label design, first EDA

#### Sprint 2: Behavioral Complexity + UI MVP
- Add recovery mechanics, agent personalities, coping strategies
- Interactive dashboard toggles for HR policies
- Save/load PostgreSQL runs
- First ML classifier + daily burnout risk visualizations

#### Sprint 3: ML + Scenario Tuning
- Finalized Random Forest burnout classifier with engineered features
- Exported daily stress snapshots and burnout risk probabilities
- Visualized model predictions (feature importance, burnout risk curves, agent-level risk histograms)
- Integrated ML pipeline with live simulation outputs for future dashboard embedding
- Prepared data for scenario tuning (e.g., 4-day week vs full-time)

### Sprint 4: Final Polish & Deployment
- Integrated final burnout model into Streamlit dashboard  
- Visualized predictions in real time with risk scores and curves  
- Saved trained model (`burnout_model.pkl`) for app embedding  
- Exported daily prediction results for scenario comparison  
- Prepared for production deployment and final reporting  

---

## 📦 Final Deliverables (Due August 8, 2025)

- ✅ **Streamlit dashboard** (deployed)
- ✅ **Complete GitHub repo** with docs and architecture
- ✅ **ML notebook + trained model**
- ✅ **PDF summary report** (charts, findings, insights)

---

## 👨‍💻 Author Credits
- **Simulation:** Cornell Stewart
- **Machine Learning:** Jeremiah Tanner  
- **Frontend & DevOps:** Kzaiah Hall

---

