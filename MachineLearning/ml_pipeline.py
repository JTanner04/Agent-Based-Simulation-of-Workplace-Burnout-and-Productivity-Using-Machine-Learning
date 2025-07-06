# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
import numpy as np


# In[2]:


df = pd.read_csv("training_data.csv")

# Create engineered features before selecting them
df['rolling_stress_3d'] = df.groupby('agent_id')['stress_level'].transform(lambda x: x.rolling(3, min_periods=1).mean())
df['stress_delta'] = df.groupby('agent_id')['stress_level'].diff().fillna(0)
df['task_efficiency'] = df['tasks_completed'] / df['workload']
df.head()

# In[3]:

#Export daily snapshots of agent stress and productivity
daily_snapshots = df[['agent_id', 'day', 'workload', 'stress_level', 'tasks_completed', 'workload', 'rolling_stress_3d', 'stress_delta', 'task_efficiency']]

#Save to CSV
daily_snapshots.to_csv("daily_snapshots.csv", index=False)

features = ["workload", "stress_level", "tasks_completed", 'rolling_stress_3d', 'stress_delta', 'task_efficiency']
x = df[features]
y = df["burned_out"]


# In[4]:


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)


# In[5]:

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(random_state=42)
model.fit(x_train, y_train)
y_pred = model.predict(x_test)


# In[6]:


print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))


# In[7]:


sns.boxplot(x="burned_out", y="stress_level", data=df)
plt.title("Stress Level vs Burnout")
plt.show()


# In[8]:
y_pred = model.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()

print(f"Accuracy: {accuracy * 100:.2f}%")
print(f"True Positives: {tp}")
print(f"False Negatives: {fn}")
# In[9]:
# Rolling average stress over past 3 days per agent
df['rolling_stress_3d'] = df.groupby('agent_id')['stress_level'].transform(lambda x: x.rolling(3, min_periods=1).mean())

# Change in stress since previous day
df['stress_delta'] = df.groupby('agent_id')['stress_level'].diff().fillna(0)

#Task Efficiency (task per workload hour)
df['task_efficiency'] = df['tasks_completed'] / df['workload']
# In[10]:
# Visualize Feature Importance
importances = model.feature_importances_
feature_names = x.columns
sns.barplot(x=importances, y=feature_names)
plt.title("Feature Importance (Random Forest)")
plt.show()
# In[11]:
#Visualize Burnout Risk Over Time
burnout_risk = model.predict_proba(x_test)[:, 1]

risk_df = x_test.copy()
risk_df['burnout_risk'] = burnout_risk
risk_df['actual'] = y_test.values

sns.histplot(risk_df['burnout_risk'], bins=20)
plt.title("Distribution of Burnout Risk Scores")
plt.xlabel("Predicted Burnout Risk")
plt.ylabel("Count")
plt.show()
# In[12]:
#Burnout Risk Curve
if "day" not in df.columns:
    df["day"] = df.groupby("agent_id").cumcount() + 1

# Add day info to risk_df based on original index
risk_df["agent_id"] = df.loc[risk_df.index, "agent_id"].values
risk_df["day"] = df.loc[risk_df.index, "day"].values

# Average burnout risk per day
avg_risk_by_day = risk_df.groupby("day")["burnout_risk"].mean()

# Plot it
plt.figure(figsize=(8, 4))
avg_risk_by_day.plot(kind="line", marker="o")
plt.title("Average Burnout Risk Over Time")
plt.xlabel("Day")
plt.ylabel("Average Burnout Risk")
plt.grid(True)
plt.tight_layout()
plt.show()
# In[13]
