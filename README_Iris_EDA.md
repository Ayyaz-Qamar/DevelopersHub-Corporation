# 📊 Task 1: Exploratory Data Analysis (Iris Dataset)

## 📌 Overview
This project is part of an AI/ML Engineering Internship task.  
The objective is to perform **Exploratory Data Analysis (EDA)** on the Iris dataset to understand data structure, statistics, and feature relationships using Python.

## 📂 Dataset
The dataset used is the **Iris Dataset**, which contains measurements of three different species of Iris flowers.

### Features:
- Sepal Length
- Sepal Width
- Petal Length
- Petal Width
- Species (Target Class)

## 🎯 Objectives
- Load and inspect dataset
- Understand data structure and statistics
- Detect missing values
- Visualize relationships between features
- Identify patterns and outliers

## 🛠️ Tools & Libraries
- Python
- Pandas
- Matplotlib
- Seaborn

## 📥 Installation
pip install pandas matplotlib seaborn

## 🚀 Steps Performed

### Load Dataset
iris = pd.read_csv("/content/iris.csv")

### Data Inspection
iris.head()
iris.shape
iris.columns

### Dataset Information
iris.info()

### Statistical Summary
iris.describe()

### Missing Values Check
iris.isnull().sum()

## 📊 Data Visualization

Scatter Plot:
sns.scatterplot(data=iris, x="sepal_length", y="petal_length", hue="species")

Histograms:
iris.hist(figsize=(10,8))

Box Plot:
sns.boxplot(data=iris)

Pair Plot (Optional):
sns.pairplot(iris, hue="species")

## 📈 Key Insights
- 150 samples, 5 columns
- No missing values
- Petal features are highly informative for classification
- Species are clearly separable

## 🧠 Skills Learned
- Data loading with Pandas
- EDA workflow
- Statistical analysis
- Visualization with Seaborn & Matplotlib

## 📌 Conclusion
EDA is a critical first step in any ML pipeline. It improves understanding of data and helps guide model building decisions.
