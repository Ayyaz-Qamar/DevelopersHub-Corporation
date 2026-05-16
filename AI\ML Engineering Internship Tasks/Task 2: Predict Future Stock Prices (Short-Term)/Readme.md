📈 Task 2: Predict Future Stock Prices (Short-Term)
🎯 Objective

The goal of this project is to predict the next day's closing price of a stock using historical stock market data. A regression-based machine learning model is trained on features derived from stock price movement.

📊 Dataset
Source: Yahoo Finance
Library: yfinance
Stock Example: Apple (AAPL), Tesla (TSLA), or any selected stock

The dataset contains:

Open price
High price
Low price
Close price
Volume
⚙️ Features Used

The model uses the following input features:

Open
High
Low
Volume

🎯 Target variable:

Next day Close price (shifted by 1 day)
🧠 Machine Learning Models Used

Two regression models are used for prediction:

Linear Regression (baseline model)
Random Forest Regressor (improved performance option)
📌 Workflow
1. Stock Selection

A stock is selected (e.g., AAPL or TSLA).

2. Data Collection

Historical stock data is fetched using the yfinance API.

3. Data Preprocessing
Selecting required features
Creating target variable (next-day Close price)
Handling missing values
4. Model Training
Dataset is split into training and testing sets
Regression model is trained on historical data
5. Prediction

The trained model predicts future closing prices on test data.

6. Visualization

Actual vs predicted closing prices are plotted for comparison.

📊 Visualization Output

The project generates a graph showing:

Actual Closing Prices 📉
Predicted Closing Prices 📈

This helps evaluate how closely the model follows real market trends.

🛠️ Technologies Used
Python 🐍
yfinance (Yahoo Finance API)
Pandas
NumPy
Scikit-learn
Matplotlib