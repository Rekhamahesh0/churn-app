import streamlit as st
import numpy as np
import pickle

# Load model and scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.title("📊 Customer Churn Prediction")

st.write("Enter customer details below:")

# Input fields
tenure = st.number_input("Tenure", 0, 100)
monthly_charges = st.number_input("Monthly Charges", 0.0, 200.0)
total_charges = st.number_input("Total Charges", 0.0, 10000.0)

gender = st.selectbox("Gender", ["Male", "Female"])
partner = st.selectbox("Partner", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["Yes", "No"])
phone_service = st.selectbox("Phone Service", ["Yes", "No"])
internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

# Convert to numeric (same as training)
gender = 1 if gender == "Male" else 0
partner = 1 if partner == "Yes" else 0
dependents = 1 if dependents == "Yes" else 0
phone_service = 1 if phone_service == "Yes" else 0

internet_map = {"DSL": 0, "Fiber optic": 1, "No": 2}
internet_service = internet_map[internet_service]

# Feature array (IMPORTANT: order must match training)
features = np.array([[gender, partner, dependents, tenure,
                      phone_service, internet_service,
                      monthly_charges, total_charges]])

# Scale input
features = scaler.transform(features)

# Prediction
if st.button("Predict"):
    prediction = model.predict(features)

    if prediction[0] == 1:
        st.error("❌ Customer will CHURN")
    else:
        st.success("✅ Customer will STAY")