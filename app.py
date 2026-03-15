import streamlit as st
import joblib

st.title("Heart Disease Prediction App")
st.write("Priyam Bhattacharya")
st.markdown("---")

pipeline = joblib.load('pipeline.pkl')
col_names = joblib.load('col_names.pkl')

# ui creation

age = st.number_input(
    "Age",
    max_value=80
)

weight = st.number_input(
    "Weight",
    max_value=100
)
height = st.number_input(
    "Height in cm",
    min_value=150,
    max_value=190
)

bmi = st.number_input(
    "BMI",
    min_value=18,
    max_value=40
)

smoking = st.selectbox(
    "Smoking",
    ['Never', 'Current', 'Formal']
)

alcohol = st.selectbox(
    "Alcohol",
    ['None', 'Low', 'Moderate', 'High']
)

pa = st.selectbox(
    "Physical Activity",
    ['Sedentary', 'Active', 'Moderate']
)
diet = st.selectbox(
    "Diet",
    ['Healthy', 'Average', 'Unhealthy']
)

sl = st.selectbox(
    "Stress Level",
    ['Low', 'Medium', 'High']
)

hypertension = st.selectbox(
    "Hypertension",
    ["Yes", 'No']
)

diabetes = st.selectbox(
    "Diabetes",
    ["Yes", 'No']
)

hyperlipidemia = st.selectbox(
    "Hyperlipidemia",
    ["Yes", 'No']
)


fh = st.selectbox(
    "Family History",
    ["Yes", 'No']
)

pha = st.selectbox(
    "Previous Heart Attack",
    ["Yes", 'No']
)

sbp = st.number_input(
    "Systolic BP",
    min_value=100,
    max_value=180
)

dbp = st.number_input(
    "Dyastolic BP",
    min_value=60,
    max_value=120
)

hr = st.number_input(
    "Heart Rate",
    min_value=60,
    max_value=110
)

bs = st.number_input(
    "Bolld Sugar",
    min_value=70,
    max_value=180
)

cholesterol = st.number_input(
    "Cholesterol",
    min_value=140,
    max_value=310
)
