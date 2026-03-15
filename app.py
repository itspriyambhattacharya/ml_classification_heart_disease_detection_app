import streamlit as st
import joblib
import pandas as pd

st.title("Heart Disease Prediction App")
st.write("Priyam Bhattacharya")
st.markdown("---")


@st.cache_resource
def load_model():
    pipeline = joblib.load('pipeline.pkl')
    col_names = joblib.load('col_names.pkl')
    return pipeline, col_names


pipeline, col_names = load_model()
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
    ['Never', 'Current', 'Former']
)

gender = st.selectbox(
    "Gender",
    ['Male', 'Female']
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
    "Diastolic BP",
    min_value=60,
    max_value=120
)

hr = st.number_input(
    "Heart Rate",
    min_value=60,
    max_value=110
)

bs = st.number_input(
    "Blood Sugar",
    min_value=70,
    max_value=180
)

cholesterol = st.number_input(
    "Cholesterol",
    min_value=140,
    max_value=310
)

if st.button("Predict"):
    with st.spinner("Predicting"):
        hypertension = 1 if hypertension.lower() == 'yes' else 0
        diabetes = 1 if diabetes.lower() == 'yes' else 0
        hyperlipidemia = 1 if hyperlipidemia.lower() == 'yes' else 0
        fh = 1 if fh.lower() == 'yes' else 0
        pha = 1 if pha.lower() == 'yes' else 0
        ns = pd.DataFrame({
            'age': [age],
            'gender': [gender],
            'weight': [weight], 'height': [height], 'bmi': [bmi],
            'smoking': [smoking],
            'physical_activity': [pa],
            'diet': [diet],
            'stress_level': [sl],
            'hypertension': [hypertension],
            'diabetes': [diabetes],
            'hyperlipidemia': [hyperlipidemia],
            'family_history': [fh],
            'previous_heart_attack': [pha],
            'systolic_bp': [sbp],
            'diastolic_bp': [dbp],
            'heart_rate': [hr],
            'blood_sugar_fasting': [bs],
            'cholesterol_total': [cholesterol]
        },
            index=[0]
        )
        ns = ns[col_names]
        st.write(ns)
        pred = pipeline.predict(ns)
        # pred_proba = pipeline.predict_proba(ns)
        # st.write(pred_proba[0])
        if pred[0] == 1:
            st.error("High Rish of Heart Attack")
        elif pred[0] == 0:
            st.success("Low Risk of Heart Attack")

st.markdown("---")
st.caption(
    "This application is for educational purposes only and should not be used for medical diagnosis."
)
st.markdown("---")
