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
df.head()

# In[3]:


features = ["workload", "stress_level", "tasks_completed"]
x = df[features]
y = df["burned_out"]


# In[4]:


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)


# In[5]:


model = LogisticRegression()
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
