import streamlit as st
import pandas as pd
import joblib  # agar aapne model save kiya hai

# Load model
model = joblib.load("code/fake_job_model.pkl")  # model.ipynb se save kiya hoga

st.title("Fake Job Detection")

# Input fields
title = st.text_input("Job Title")
description = st.text_area("Job Description")
telecommuting = st.number_input("Telecommuting", min_value=0, max_value=1, value=0)

# Predict button
if st.button("Predict"):
    # Simple example: aapko features vectorize karke model me pass karna hoga
    # X = preprocess(title, description, telecommuting)
    # pred = model.predict(X)
    st.write("Prediction: Fake / Real")
