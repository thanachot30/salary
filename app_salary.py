


import streamlit as st
import pickle
import numpy as np

# Load the saved model
with open("linear_regression_model.pkl", "rb") as file:
    model = pickle.load(file)

# Streamlit app
st.title("Salary Prediction App")
st.write("This app predicts the salary based on years of experience using a linear regression model.")

# Input from user
years_experience = st.number_input("Enter years of experience:", min_value=0.0, max_value=50.0, step=0.1)

# Prediction
if st.button("Predict Salary"):
    # Reshape input to match model's expected input shape
    salary_prediction = model.predict(np.array([[years_experience]]))[0]
    st.write(f"Predicted Salary: ${salary_prediction:,.2f}")
