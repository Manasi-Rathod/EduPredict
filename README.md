# 🎓 **EduPredict – AI-Driven Student Performance & Placement Prediction System**

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Framework-Flask-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/ML-Scikit--Learn-brightgreen?style=for-the-badge">
  <img src="https://img.shields.io/badge/Data-Pandas-yellow?style=for-the-badge">
  <img src="https://img.shields.io/badge/Domain-Education%20Analytics-purple?style=for-the-badge">
</p>

---

## 📘 **About the Project**

**EduPredict** is a machine learning–powered platform designed to evaluate **student performance**, **learning outcomes**, and **placement potential** using predictive analytics.
It offers an intuitive **Flask-based dashboard** where students or administrators can enter academic data and instantly receive performance insights.

This system is ideal for:
🎓 Colleges & Training Institutes
📊 Academic Counselors
🧑‍🏫 Faculty & Mentors
👨‍🎓 Students improving academic planning

---

## ✨ **Key Features**

### 🔮 **1. AI-Powered Student Performance Prediction**

* Predicts placement probability
* Identifies at-risk students
* Evaluates academic readiness
* Provides interpretability based on input features

### 📊 **2. Interactive Analytics Dashboard**

* Clean and modern UI using Flask templates
* Insightful scorecards and visualization
* Fast prediction response

### 🧠 **3. End-to-End ML Pipeline**

* Data preprocessing using scaler (`scaler.pkl`)
* ML model training (`train_model.py`)
* Exported production-ready model (`placement_model.pkl`)

### 💻 **4. Lightweight Deployment**

* Flask backend
* HTML/CSS templates (no heavy frontend frameworks)
* Simple to host on Render, AWS, Azure, or Heroku

---

## 🧩 **Technology Stack**

| Layer                | Tools Used           |
| -------------------- | -------------------- |
| **Backend**          | Flask                |
| **ML Framework**     | Scikit-Learn         |
| **Data Processing**  | Pandas, NumPy        |
| **Model Deployment** | Pickle Model + Flask |
| **Frontend**         | HTML, CSS, Bootstrap |
| **Versioning**       | Git & GitHub         |

---

## 📁 **Project Structure**

```
EduPredict/
│── static/                   # CSS, images, assets
│── templates/                # HTML frontend pages
│── app.py                    # Main Flask application
│── train_model.py            # Model training pipeline
│── placement_model.pkl       # Machine learning model
│── scaler.pkl                # Scaler for preprocessing
│── requirements.txt          # Project dependencies
│── .gitignore                # Ignored files
```

---

## 🏗️ **System Architecture**

```
            ┌─────────────────┐
            │   User Input    │
            └────────┬────────┘
                     ▼
            ┌─────────────────┐
            │   Flask App     │
            └────────┬────────┘
                     ▼
     ┌────────────────────────────────┐
     │  Preprocessing (Scaler.pkl)    │
     └─────────────┬──────────────────┘
                   ▼
        ┌───────────────────────┐
        │  ML Model (pkl file)  │
        └──────────┬────────────┘
                   ▼
             📈 Prediction Output
```

---

## 🚀 **Getting Started**

### **1️⃣ Clone the Repository**

```
git clone https://github.com/Manasi-Rathod/EduPredict.git
cd EduPredict
```

### **2️⃣ Install Dependencies**

```
pip install -r requirements.txt
```

### **3️⃣ Run the Application**

```
python app.py
```

### **4️⃣ Open in Browser**

```
http://127.0.0.1:5000
```

---

## 🔮 **Upcoming Enhancements**

* 🔵 Advanced dashboards using Plotly
* 🔵 Multiple ML models with comparison
* 🔵 Explainable AI (SHAP-based insights)
* 🔵 Student recommendation engine
* 🔵 Cloud-hosted version with authentication

---

## 👩‍💻 **Author**

**Manasi Rathod**
AI/ML Engineer | Data Science | Predictive Analytics

If this project helps you, please ⭐ the repository.
Your support motivates future improvements!

---
