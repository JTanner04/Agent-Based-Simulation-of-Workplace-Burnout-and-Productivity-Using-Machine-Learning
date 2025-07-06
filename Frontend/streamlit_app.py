import os
import streamlit as st
import pandas as pd
import psycopg2
import plotly.express as px
import matplotlib.pyplot as plt

# --- Configuration ---
st.set_page_config(
    page_title="Workplace Burnout Simulation Dashboard",
    layout="wide"
)

# --- Sidebar Controls ---
st.sidebar.header("Simulation Controls")
steps = st.sidebar.number_input("Steps to run", min_value=1, max_value=1000, value=50)
num_agents = st.sidebar.number_input("Number of employees", min_value=1, max_value=100, value=10)
run_db = st.sidebar.checkbox("Persist to PostgreSQL", value=True)
run_button = st.sidebar.button("Run Simulation")

# Connection string (read from env if not provided)
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://user:password@localhost:5432/workplace_sim"
)

# --- Functions ---
@st.cache_data(show_spinner=False)
def load_csv():
    path = os.path.join("exports", "metrics.csv")
    if os.path.exists(path):
        return pd.read_csv(path)
    return pd.DataFrame()

@st.cache_data(show_spinner=False)
def load_db():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        query = "SELECT * FROM metrics ORDER BY run_id, step"
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    except Exception:
        return pd.DataFrame()

# --- Run Simulation ---
if run_button:
    with st.spinner("Running simulation..."):
        from subprocess import run
        cmd = [
            "python", "scheduler.py",
            "--steps", str(steps)
        ]
        if not run_db:
            cmd.append("--no-db")
        run(cmd)
    st.success("Simulation completed.")

# --- Data Loading ---
st.header("Simulation Metrics")

# Choose data source
source = st.radio("Data source", ("CSV", "PostgreSQL"))
if source == "CSV":
    df = load_csv()
else:
    df = load_db()

if df.empty:
    st.warning("No data available. Run the simulation first.")
    st.stop()

# --- Time-Series Plots ---
col1, col2 = st.columns(2)
with col1:
    st.subheader("Average Stress over Time")
    # Plotly line chart
    fig1 = px.line(df, x="step", y="Avg_Stress", title="Avg Stress vs Step")
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("Average Productivity over Time")
    # Matplotlib line chart
    fig2, ax2 = plt.subplots()
    ax2.plot(df["step"], df["Avg_Productivity"], marker='o')
    ax2.set_xlabel("Step")
    ax2.set_ylabel("Avg Productivity")
    ax2.set_title("Avg Productivity vs Step")
    st.pyplot(fig2)

# --- Download Data ---
st.markdown("---")
st.subheader("Export Data")
if st.download_button(
    label="Download CSV",
    data=df.to_csv(index=False).encode('utf-8'),
    file_name="metrics.csv",
    mime="text/csv"
):
    st.info("CSV downloaded!")
