import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("Customer Churn Prediction")

st.write("Enter customer details:")

# Inputs
tenure = st.number_input("Tenure", 0, 100)
monthly_charges = st.number_input("Monthly Charges", 0.0, 200.0)
total_charges = st.number_input("Total Charges", 0.0, 10000.0)

gender = st.selectbox("Gender", ["Male", "Female"])
partner = st.selectbox("Partner", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["Yes", "No"])
phone_service = st.selectbox("Phone Service", ["Yes", "No"])
internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

# Convert to numbers
gender = 1 if gender == "Male" else 0
partner = 1 if partner == "Yes" else 0
dependents = 1 if dependents == "Yes" else 0
phone_service = 1 if phone_service == "Yes" else 0

internet_map = {"DSL": 0, "Fiber optic": 1, "No": 2}
internet_service = internet_map[internet_service]

# Feature array
# Create full feature vector (20 features as model expects)
features = np.zeros((1, 20))

# Fill only known values (positions matter)
features[0][0] = gender
features[0][1] = partner
features[0][2] = dependents
features[0][3] = tenure
features[0][4] = phone_service
features[0][5] = internet_service
features[0][6] = monthly_charges
features[0][7] = total_charges

# Prediction
if st.button("Predict"):
    prediction = model.predict(features)

    if prediction[0] == 1:
        st.error("Customer will CHURN ❌")
    else:
        st.success("Customer will STAY ✅")
