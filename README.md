# 🚗 Car MPG Prediction App

This project is a regression-based machine learning app that predicts the **Miles Per Gallon (MPG)** of a car using its technical specifications. The app is built using **Streamlit** for interactive input and runs a pretrained model (`auto.pkl`) in the backend.

## 🎯 Objective

To estimate a car’s fuel efficiency (MPG) based on attributes such as engine specs, weight, and model year. This can assist car manufacturers and buyers in evaluating performance.

## 🧠 Model Details

- **Model:** Pretrained regression model (e.g., RandomForestRegressor or similar)
- **Target:** `MPG` (Miles Per Gallon)
- **Input Features:**
  - Cylinders
  - Displacement
  - Horsepower
  - Weight
  - Acceleration
  - Model Year
  - Origin (1: USA, 2: Europe, 3: Asia)

## 💻 Tech Stack

- **Python**
- **Streamlit** – Web app UI
- **Joblib** – Model loading
- **NumPy, Pandas** – Data handling

## 🚀 Features

- Simple UI to input car details
- Real-time prediction of fuel efficiency
- Error handling and data validation

## 📂 Folder Structure

mpg-prediction-app/
│
├── app.py # Streamlit app code
├── auto.pkl # Trained regression model
├── requirements.txt # Dependencies
├── README.md # Project documentation

## 📊 Sample Output

User Input:
  Cylinders: 4 ,
  Horsepower: 90 ,
  Weight: 2500 ,
  Model Year: 2010 

✅ Predicted MPG: 28.56

## 📌 Disclaimer
- This application is for demonstration and educational purposes only. Actual fuel efficiency may vary based on driving conditions and other factors.
