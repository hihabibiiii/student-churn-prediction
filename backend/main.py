from fastapi import FastAPI, HTTPException
import pickle
import pandas as pd

app = FastAPI(title="Student Churn Prediction API 🚀")

# -----------------------------
# Load Model + Encoders
# -----------------------------
try:
    with open("../model/model.pkl", "rb") as f:
        model = pickle.load(f)

    with open("../model/encoders.pkl", "rb") as f:
        encoders = pickle.load(f)

except Exception as e:
    raise RuntimeError(f"Error loading model: {e}")

# -----------------------------
# Home Route
# -----------------------------
@app.get("/")
def home():
    return {
        "message": "Student Churn Prediction API Running 🚀",
        "status": "OK"
    }

# -----------------------------
# Health Check
# -----------------------------
@app.get("/health")
def health():
    return {"status": "healthy"}

# -----------------------------
# Prediction Route
# -----------------------------
@app.post("/predict")
def predict(data: dict):
    try:
        df = pd.DataFrame([data])

        # encoding
        for col, encoder in encoders.items():
            if col in df.columns:
                df[col] = encoder.transform(df[col])

        # probability
        prob = model.predict_proba(df)[0][1]

        # threshold
        prediction = 1 if prob > 0.40 else 0

        # 🔥 Risk level logic
        if prob < 0.30:
            risk = "Low"
        elif prob < 0.60:
            risk = "Medium"
        else:
            risk = "High"

        return {
            "prediction": prediction,
            "result": "Dropout" if prediction == 1 else "Not Dropout",
            "confidence": round(float(prob), 3),
            "risk_level": risk
        }

    except Exception as e:
        return {"error": str(e)}