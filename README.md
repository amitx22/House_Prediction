# 🏠 House Price Prediction

A Machine Learning web application that predicts the estimated price of a house based on its features using a trained regression model.

## Live Demo : https://houseprediction-ncycth7k7pueqtnx6owhzo.streamlit.app/

## 🎯 Objective

The objective of this project is to build a simple ML-based system that takes important house features as input and predicts the estimated house price.

## 🧠 How It Works

```text
House Features
      ↓
Data Preprocessing
      ↓
Trained ML Regression Model
      ↓
Price Prediction
      ↓
Streamlit Web Interface
```

The application takes the following inputs:

* Square Footage
* Number of Bedrooms
* Number of Bathrooms
* Year Built
* Lot Size
* Garage Size
* Neighborhood Quality

The trained model is loaded using **Joblib** and used to generate the prediction.

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Streamlit

The repository's `requirements.txt` includes Pandas, NumPy, Scikit-learn, Joblib and Streamlit.

## ✨ Features

* Interactive Streamlit interface
* Multiple house feature inputs
* ML-based price prediction
* Pre-trained model loading
* Simple and user-friendly UI
* Instant prediction result

## 📂 Project Structure

```text
House_Prediction/
│
├── app.py
├── house_price_analysis.ipynb
├── train.csv
├── house_price_model.pkl
├── model_columns.pkl
└── requirements.txt
```

## ▶️ Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

The application will open in the browser.

## 💡 Key Learning

Through this project, I learned the complete workflow of a Machine Learning regression project:

```text
Dataset
   ↓
Data Analysis
   ↓
Feature Selection
   ↓
Model Training
   ↓
Model Saving
   ↓
Prediction
   ↓
Streamlit Deployment
```

## 💼 Interview Explanation

> "I developed a House Price Prediction application using Machine Learning regression. I used house-related features such as square footage, bedrooms, bathrooms, year built, lot size, garage size and neighborhood quality to predict the estimated house price. I trained the model using the dataset, saved the trained model using Joblib, and built a Streamlit interface where users can enter the house details and get a prediction."

## 👨‍💻 Author

**Amit Kumar Singh**
 
