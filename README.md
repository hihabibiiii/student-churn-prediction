# 🎓 Student Dropout Risk Prediction System

A full-stack Machine Learning project that predicts whether a student is at risk of dropping out using real-world data.

---

## 🚀 Features

* 🔥 XGBoost ML Model (optimized with threshold tuning)
* 📊 Risk Level Prediction (Low / Medium / High)
* ⚡ FastAPI Backend (Production-ready API)
* 🎨 Streamlit UI (Interactive frontend)
* 📈 Confidence Score Output
* 🧠 Feature Engineering + Imbalance Handling

---

## 🛠️ Tech Stack

* Python
* Scikit-learn
* XGBoost
* FastAPI
* Streamlit
* Pandas / NumPy

---

## 📁 Project Structure

```
student-churn-prediction/
│
├── model/
│   ├── model.pkl
│   └── encoders.pkl
│
├── backend/
│   └── main.py
│
├── app.py
├── train_model.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/student-churn-prediction.git
cd student-churn-prediction

pip install -r requirements.txt
```

---

## ▶️ Run Backend

```bash
cd backend
uvicorn main:app --reload
```

---

## 🎨 Run Frontend (Streamlit)

```bash
streamlit run app.py
```

---

## 🌐 API Endpoint

```
POST /predict
```

### Example Input:

```json
{
  "Age": 21,
  "Gender": "Male",
  "Family_Income": 30000,
  "Internet_Access": "Yes",
  "Study_Hours_per_Day": 5,
  "Attendance_Rate": 85,
  "Assignment_Delay_Days": 1,
  "Travel_Time_Minutes": 20,
  "Part_Time_Job": "No",
  "Scholarship": "Yes",
  "Stress_Index": 4,
  "GPA": 1.5,
  "Semester_GPA": 1.4,
  "CGPA": 1.3,
  "Semester": "Year 2",
  "Department": "Engineering",
  "Parental_Education": "Bachelor"
}
```

---

## 📊 Output

```json
{
  "prediction": 0,
  "result": "Not Dropout",
  "confidence": 0.23,
  "risk_level": "Low"
}
```

---

## 🧠 Model Details

* Algorithm: XGBoost Classifier
* Imbalance Handling: scale_pos_weight
* Threshold Tuning: 0.40
* Feature Engineering:

  * Performance Score
  * Engagement Score

---

## 🎯 Use Cases

* 🎓 Colleges (Dropout prevention)
* 📚 EdTech platforms
* 🧑‍🏫 Coaching institutes

---

## 👨‍💻 Author

**Habibullah Salmani**
Data Scientist & Full Stack Developer

📧 Email: [hshabibullah@gmail.com](mailto:hshabibullah@gmail.com)
🔗 GitHub: https://github.com/hihabibiiii

---

## ⭐ If you like this project, give it a star!
