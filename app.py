import streamlit as st
import pickle

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

st.title("🌍 Global Natural Disasters – Disaster Group Prediction")
st.write("This app predicts whether a disaster is **Natural** or **Technological**, based on input values.")

# Input fields
deaths = st.number_input("Total Deaths", min_value=0, step=1)
affected = st.number_input("Total Affected", min_value=0, step=1)
damages = st.number_input("Total Damages (000 US$)", min_value=0, step=1)

# Predict button
if st.button("Predict"):
    prediction = model.predict([[deaths, affected, damages]])
    st.success(f"Predicted Disaster Group: {prediction[0]}")
