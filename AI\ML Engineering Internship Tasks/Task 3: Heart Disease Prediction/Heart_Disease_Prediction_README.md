# 🫀 Heart Disease Prediction System

## 📌 Project Overview
This project is a machine learning-based system that predicts whether a person is at risk of heart disease using clinical and medical attributes. It uses the UCI Heart Disease dataset and applies classification algorithms to generate predictions along with model interpretability.

---

## 📊 Dataset
- Source: Heart Disease UCI Dataset (Kaggle)
- Records: 1025 samples
- Features: Medical attributes such as chest pain type, ECG results, blood pressure indicators, thalassemia, etc.
- Target: Presence or absence of heart disease (binary classification)

---

## ⚙️ Project Workflow

### 1. Data Preprocessing
- Handled categorical variables using one-hot encoding (pd.get_dummies)
- Converted all features into numeric format
- Ensured dataset was fully ML-compatible

### 2. Exploratory Data Analysis (EDA)
- Analyzed target distribution
- Studied feature relationships using correlation heatmap
- Identified patterns affecting heart disease risk

### 3. Feature Engineering
- Separated features (X) and target (y)
- Applied train-test split (stratified sampling)
- Scaled features for Logistic Regression using StandardScaler

### 4. Model Training
Two models were trained:
- Logistic Regression (baseline linear model)
- Decision Tree Classifier (interpretable non-linear model)

### 5. Model Evaluation
Performance was evaluated using:
- Accuracy Score
- Confusion Matrix
- ROC Curve & AUC Score

### 6. Feature Importance
- Logistic Regression coefficients used for interpretability
- Decision Tree feature importance used to identify key medical indicators

---

## 📈 Results
- Models successfully predict heart disease risk
- Logistic Regression provides probabilistic interpretation
- Decision Tree provides rule-based insights
- Key medical features identified influencing prediction

---

## 🧠 Key Skills Demonstrated
- Binary Classification
- Data Preprocessing & Encoding
- Exploratory Data Analysis (EDA)
- Model Training (Logistic Regression, Decision Tree)
- Model Evaluation (Accuracy, ROC-AUC, Confusion Matrix)
- Feature Importance Analysis

---

## 🚀 Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn

---

## 📌 Future Improvements
- Hyperparameter tuning
- Deployment using Streamlit or FastAPI
- Adding real-time patient input interface
- Improving accuracy with ensemble models

---

## 👨‍💻 Author
Machine Learning Project – Heart Disease Prediction System
