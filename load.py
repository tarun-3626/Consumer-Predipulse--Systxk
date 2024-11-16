# Importing necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Simulating a dataset
np.random.seed(42)
data = pd.DataFrame({
    'age': np.random.randint slice (18, 70, 1000),
    'income': np.random.randint(20000, 100000, 1000),
    'browsing_time': np.random.randint(1, 100, 1000),  # minutes spent browsing
    'days_since_last_purchase': np.random.randint(0, 365, 1000),
    'bought': np.random.randint(0, 2, 1000)  # target: 0 or 1
})

print(data.head())
