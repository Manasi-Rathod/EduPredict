# train_model.py

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
matplotlib.use('Agg')  # Avoids GUI issues when plotting
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, roc_auc_score
import joblib

import os
os.makedirs("static", exist_ok=True)

# Load dataset
df = pd.read_csv(r"C:\Users\RATHO\Downloads\student_placement\Student_Placement.csv")
df.drop(columns=['College_ID'], inplace=True)

# Encode categorical columns
df['Internship_Experience'] = df['Internship_Experience'].map({'Yes': 1, 'No': 0})
df['Placement'] = df['Placement'].map({'Yes': 1, 'No': 0})

# EDA: Save plots
sns.countplot(x='Placement', data=df)
plt.title("Placement Distribution")
plt.savefig("static/placement_distribution.png")
plt.clf()

# Correlation heatmap
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.savefig("static/correlation_heatmap.png")
plt.clf()

# Features and Target
X = df.drop("Placement", axis=1)
y = df["Placement"]

# Split & scale
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train Model
model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled, y_train)

# Evaluation
y_pred = model.predict(X_test_scaled)
print("Classification Report:\n", classification_report(y_test, y_pred))

# Save model and scaler
joblib.dump(model, 'placement_model.pkl')
joblib.dump(scaler, 'scaler.pkl')
print("✅ Model and scaler saved successfully!")
