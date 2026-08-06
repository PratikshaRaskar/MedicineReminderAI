import os
import joblib
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "adherence_model.pkl")

model = joblib.load(MODEL_PATH)

def predict_adherence(age,
                       gender,
                       chronic_disease,
                       medicines_count,
                       doses_per_day,
                       treatment_days,
                       previous_missed_doses,
                       reminder_used):

    # Encode categorical values
    gender = 1 if gender == "Male" else 0
    chronic_disease = 1 if chronic_disease == "Yes" else 0
    reminder_used = 1 if reminder_used == "Yes" else 0

    data = pd.DataFrame([{
        "age": age,
        "gender": gender,
        "chronic_disease": chronic_disease,
        "medicines_count": medicines_count,
        "doses_per_day": doses_per_day,
        "treatment_days": treatment_days,
        "previous_missed_doses": previous_missed_doses,
        "reminder_used": reminder_used
    }])

    print("\n====== INPUT TO MODEL ======")
    print(data)

    prediction = model.predict(data)[0]

    print("Prediction:", prediction)
    probability = model.predict_proba(data)[0].max() * 100

    if prediction == 0:
        status = "High Adherence"
    else:
        status = "Low Adherence"

    return status, round(probability, 2)