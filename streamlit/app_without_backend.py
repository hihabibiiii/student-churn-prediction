import streamlit as st
import pickle
import pandas as pd

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Student Dropout Dashboard",
    page_icon="🎓",
    layout="wide"
)

# -----------------------------
# Load Model
# -----------------------------
@st.cache_resource
def load_model():
    with open("../model/model.pkl", "rb") as f:
        model = pickle.load(f)
    with open("../model/encoders.pkl", "rb") as f:
        encoders = pickle.load(f)
    return model, encoders

model, encoders = load_model()

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("📊 Navigation")
page = st.sidebar.radio("Go to", ["Prediction", "About"])

# -----------------------------
# Prediction Page
# -----------------------------
if page == "Prediction":

    st.title("🎓 Student Dropout Prediction Dashboard")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("👤 Student Info")
        age = st.number_input("Age", 18, 30, 21)
        gender = st.selectbox("Gender", ["Male", "Female"])
        income = st.number_input("Family Income", 0, 100000, 25000)
        internet = st.selectbox("Internet Access", ["Yes", "No"])
        job = st.selectbox("Part Time Job", ["Yes", "No"])
        scholarship = st.selectbox("Scholarship", ["Yes", "No"])

    with col2:
        st.subheader("📚 Academic Info")
        study = st.slider("Study Hours", 0, 10, 3)
        attendance = st.slider("Attendance (%)", 0, 100, 75)
        delay = st.slider("Assignment Delay", 0, 10, 2)
        travel = st.slider("Travel Time", 0, 120, 30)
        stress = st.slider("Stress Index", 0, 10, 5)
        gpa = st.number_input("GPA", 0.0, 2.0, 1.2)
        sem_gpa = st.number_input("Semester GPA", 0.0, 2.0, 1.1)
        cgpa = st.number_input("CGPA", 0.0, 2.0, 1.1)

    col3, col4 = st.columns(2)

    with col3:
        semester = st.selectbox("Semester", ["Year 1", "Year 2", "Year 3", "Year 4"])
        dept = st.selectbox("Department", ["Engineering", "Arts", "Business", "CS"])

    with col4:
        parent = st.selectbox("Parental Education", ["High School", "Bachelor", "Master"])

    # -----------------------------
    # Prediction Button
    # -----------------------------
    if st.button("🚀 Predict Risk"):

        # -----------------------------
        # Input Data
        # -----------------------------
        data = {
            "Age": age,
            "Gender": gender,
            "Family_Income": income,
            "Internet_Access": internet,
            "Study_Hours_per_Day": study,
            "Attendance_Rate": attendance,
            "Assignment_Delay_Days": delay,
            "Travel_Time_Minutes": travel,
            "Part_Time_Job": job,
            "Scholarship": scholarship,
            "Stress_Index": stress,
            "GPA": gpa,
            "Semester_GPA": sem_gpa,
            "CGPA": cgpa,
            "Semester": semester,
            "Department": dept,
            "Parental_Education": parent
        }

        df = pd.DataFrame([data])

        # -----------------------------
        # Encoding
        # -----------------------------
        for col, encoder in encoders.items():
            if col in df.columns:
                df[col] = encoder.transform(df[col])

        # -----------------------------
        # Feature Engineering (FIX 🔥)
        # -----------------------------
        df["performance_score"] = (df["GPA"] + df["Semester_GPA"] + df["CGPA"]) / 3
        df["engagement_score"] = (df["Attendance_Rate"]/100 + df["Study_Hours_per_Day"]/10) / 2

        # -----------------------------
        # Column Order Fix (VERY IMPORTANT)
        # -----------------------------
        df = df[model.feature_names_in_]

        # -----------------------------
        # Prediction
        # -----------------------------
        prob = model.predict_proba(df)[0][1]
        prediction = 1 if prob > 0.40 else 0

        # -----------------------------
        # Risk Level
        # -----------------------------
        if prob < 0.30:
            risk = "Low"
        elif prob < 0.60:
            risk = "Medium"
        else:
            risk = "High"

        # -----------------------------
        # Display Result
        # -----------------------------
        st.subheader("📊 Result")

        colA, colB, colC = st.columns(3)

        colA.metric("📈 Confidence", f"{round(prob*100, 2)}%")
        colB.metric("🎯 Prediction", "Dropout" if prediction else "Safe")
        colC.metric("⚠️ Risk Level", risk)

        if risk == "Low":
            st.success("🟢 Low Risk Student")
        elif risk == "Medium":
            st.warning("🟡 Medium Risk Student")
        else:
            st.error("🔴 High Risk Student")

# -----------------------------
# About Page
# -----------------------------
else:
    st.title("ℹ️ About Project")

    st.markdown("""
    ### 🎓 Student Dropout Prediction System

    This project uses Machine Learning to predict student dropout risk.

    #### 🚀 Features:
    - XGBoost Model
    - Risk Level Detection
    - Confidence Score
    - Interactive Dashboard

    #### 👨‍💻 Developer:
    Habibullah Salmani
    """)