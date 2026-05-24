# 🏠 Task 6 — House Price Prediction
**DevelopersHub Corporation | AI/ML Engineering Internship**

---

## 📌 Objective
Predict house prices based on property features such as median income, number of rooms, house age, and geographic location using regression models.

---

## 📦 Dataset
**California Housing Dataset**
- 20,640 samples, 8 features
- Source: Built into `sklearn.datasets` — no download needed
- Target variable: **Median House Value** (in $100,000s)

| Feature | Description |
|---------|-------------|
| MedInc | Median income in block group |
| HouseAge | Median house age |
| AveRooms | Average number of rooms |
| AveBedrms | Average number of bedrooms |
| Population | Block group population |
| AveOccup | Average house occupancy |
| Latitude | Block group latitude |
| Longitude | Block group longitude |

---

## 🤖 Models Applied
- **Linear Regression** — baseline model with feature scaling
- **Gradient Boosting Regressor** — advanced tree-based model (200 estimators, lr=0.1)

---

## ⚙️ What Was Done

1. Loaded and inspected the dataset (shape, info, describe, missing values)
2. Exploratory Data Analysis — histograms, scatter plots, correlation heatmap, box plots
3. Split data: 80% train / 20% test
4. Feature scaling using `StandardScaler` (for Linear Regression)
5. Trained both models and generated predictions
6. Evaluated with MAE, RMSE, and R²
7. Visualized actual vs predicted prices (scatter + line plots)
8. Plotted residuals and feature importance

---

## 📊 Key Results

| Metric | Linear Regression | Gradient Boosting |
|--------|:-----------------:|:-----------------:|
| MAE | ~0.53 (~$53k avg error) | ~0.37 (~$37k avg error) |
| RMSE | ~0.73 | ~0.52 |
| R² | ~60% variance explained | ~81% variance explained |

✅ **Gradient Boosting outperformed Linear Regression by ~30% across all metrics.**

---

## 🔑 Key Insights

1. **MedInc (Median Income)** is the strongest predictor of house price
2. **Location (Latitude/Longitude)** plays a significant role
3. **AveOccup** (average occupants) has a mild negative effect on price
4. Gradient Boosting captures non-linear relationships that Linear Regression misses

---

## 🚀 How to Run

1. Open `Task6_House_Price_Prediction.ipynb` in **Google Colab**
2. Run all cells in order — no GPU required
3. No API keys or downloads needed

### Dependencies
```
scikit-learn
pandas
numpy
matplotlib
seaborn
```
> All pre-installed in Google Colab.

---

## 📂 File
```
Task6_House_Price_Prediction.ipynb
```
