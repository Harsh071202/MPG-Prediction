import streamlit as st
import pandas as pd
import joblib  # or use pickle if you prefer
import numpy as np
import os

# Load the trained model
model_path = "auto.pkl"
if os.path.exists(model_path):
    model = joblib.load(model_path)
else:
    st.error("Model file 'auto.pkl' not found. Please check the file location.")
    st.stop()

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
    try:
        input_data = np.array([[cylinders, displacement, horsepower, weight, acceleration, model_year, origin]])
        input_data = input_data.reshape(1, -1)  # Ensure proper shape for model
        prediction = model.predict(input_data)
        
        if prediction is not None and len(prediction) > 0:
            st.success(f"Predicted MPG: {float(prediction[0]):.2f}")
        else:
            st.error("Prediction failed. Model did not return a valid output.")
    except Exception as e:
        st.error(f"An error occurred during prediction: {str(e)}")

