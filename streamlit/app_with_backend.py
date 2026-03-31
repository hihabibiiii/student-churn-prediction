import streamlit as st
import requests

st.set_page_config(page_title="Student Churn Prediction", layout="centered")

st.title("🎓 Student Dropout Prediction System")
st.markdown("### Enter Student Details")

# Input Fields
age = st.number_input("Age", 18, 30, 21)
gender = st.selectbox("Gender", ["Male", "Female"])
income = st.number_input("Family Income", 0, 100000, 25000)
internet = st.selectbox("Internet Access", ["Yes", "No"])
study = st.slider("Study Hours per Day", 0, 10, 3)
attendance = st.slider("Attendance Rate (%)", 0, 100, 75)
delay = st.slider("Assignment Delay Days", 0, 10, 2)
travel = st.slider("Travel Time (minutes)", 0, 120, 30)
job = st.selectbox("Part Time Job", ["Yes", "No"])
scholarship = st.selectbox("Scholarship", ["Yes", "No"])
stress = st.slider("Stress Index", 0, 10, 5)
gpa = st.number_input("GPA", 0.0, 2.0, 1.2)
sem_gpa = st.number_input("Semester GPA", 0.0, 2.0, 1.1)
cgpa = st.number_input("CGPA", 0.0, 2.0, 1.1)
semester = st.selectbox("Semester", ["Year 1", "Year 2", "Year 3", "Year 4"])
dept = st.selectbox("Department", ["Engineering", "Arts", "Business", "CS"])
parent = st.selectbox("Parental Education", ["High School", "Bachelor", "Master"])

# Button
if st.button("🔍 Predict"):

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

    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=data)
        result = response.json()

        st.subheader("📊 Result")

        # Risk color
        if result["risk_level"] == "Low":
            st.success(f"🟢 Low Risk\n\nConfidence: {result['confidence']}")
        elif result["risk_level"] == "Medium":
            st.warning(f"🟡 Medium Risk\n\nConfidence: {result['confidence']}")
        else:
            st.error(f"🔴 High Risk\n\nConfidence: {result['confidence']}")

        st.write(f"Prediction: {result['result']}")

    except Exception as e:
        st.error("Backend not running ❌")