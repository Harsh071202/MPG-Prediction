import streamlit as st
import pandas as pd
import joblib  # or use pickle if you prefer
import numpy as np

# Load the trained model
model = joblib.load("auto.pkl")  # Ensure this file is in the same directory

# Streamlit UI
st.title("Car MPG Prediction App 🚗")
st.write("Enter car details to predict the MPG")

# User Inputs
cylinders = st.number_input("Cylinders", min_value=3, max_value=12, step=1)
displacement = st.number_input("Displacement", min_value=50.0, max_value=500.0, step=0.1)
horsepower = st.number_input("Horsepower", min_value=40.0, max_value=500.0, step=0.1)
weight = st.number_input("Weight", min_value=1000.0, max_value=6000.0, step=1.0)
acceleration = st.number_input("Acceleration", min_value=5.0, max_value=30.0, step=0.1)
model_year = st.number_input("Model Year", min_value=1900, max_value=2025, step=1)
origin = st.selectbox("Origin", [1, 2, 3])  # Assume 1=USA, 2=Europe, 3=Asia

# Predict Button
if st.button("Predict MPG"):
    input_data = np.array([[cylinders, displacement, horsepower, weight, acceleration, model_year, origin]])
    prediction = model.predict(input_data)
    st.success(f"Predicted MPG: {prediction[0]:.2f}")

