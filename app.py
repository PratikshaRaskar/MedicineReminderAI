from flask import Flask, render_template, request, redirect, url_for
import os

from config import *

# -----------------------------
# Database
# -----------------------------
from utils.database import (
    create_table,
    save_medicine,
    save_reminder,
    get_total_medicines,
    get_high_adherence,
    get_low_adherence,
    get_adherence_percentage,
    get_recent_predictions
)

# -----------------------------
# OCR
# -----------------------------
from ocr.extract_medicine import extract_text

# -----------------------------
# NLP
# -----------------------------
from nlp.medicine_parser import extract_medicines

# -----------------------------
# ML Model
# -----------------------------
from models.adherence_model import predict_adherence

# -----------------------------
# Voice Reminder
# -----------------------------
from reminder.voice import speak_reminder

# -----------------------------
# Flask App
# -----------------------------
app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.secret_key = SECRET_KEY

create_table()

# ==========================================================
# HOME
# ==========================================================

@app.route("/")
def home():
    return render_template("index.html")


# ==========================================================
# DASHBOARD
# ==========================================================

@app.route("/dashboard")
def dashboard():

    total = get_total_medicines()

    high = get_high_adherence()

    low = get_low_adherence()

    adherence = get_adherence_percentage()

    chart_data = get_recent_predictions()

    return render_template(
        "dashboard.html",
        total=total,
        high=high,
        low=low,
        adherence=adherence,
        chart_data=chart_data
    )


# ==========================================================
# Upload Page
# ==========================================================

@app.route("/upload")
def upload():
    return render_template("upload.html")


# ==========================================================
# Predict
# ==========================================================

@app.route("/predict", methods=["POST"])
def predict():

    if "image" not in request.files:
        return redirect(url_for("upload"))

    file = request.files["image"]

    if file.filename == "":
        return redirect(url_for("upload"))

    image_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(image_path)

    # -------------------------------------
    # OCR
    # -------------------------------------

    text = extract_text(image_path)

    print("OCR TEXT:")
    print(text)

    medicines = extract_medicines(text)

    print("Medicines:", medicines)

    medicines_count = len(medicines)

    # -------------------------------------
    # Patient Information
    # -------------------------------------

    age = int(request.form["age"])

    gender = request.form["gender"]

    chronic = request.form["chronic_disease"]

    doses = int(request.form["doses_per_day"])

    treatment_days = int(request.form["treatment_days"])

    missed = int(request.form["previous_missed_doses"])

    reminder_used = request.form["reminder_used"]

    reminder_time = request.form["reminder_time"]

    # -------------------------------------
    # ML Prediction
    # -------------------------------------

    prediction, probability = predict_adherence(
        age=age,
        gender=gender,
        chronic_disease=chronic,
        medicines_count=medicines_count,
        doses_per_day=doses,
        treatment_days=treatment_days,
        previous_missed_doses=missed,
        reminder_used=reminder_used
    )

    # -------------------------------------
    # Save Medicines
    # -------------------------------------

    for medicine in medicines:

        save_medicine(
            medicine,
            text,
            prediction
        )

        save_reminder(
            medicine,
            reminder_time
        )

    # -------------------------------------
    # Voice
    # -------------------------------------

    if medicines:

        speak_reminder(
            f"Please remember to take {medicines[0]}"
        )

    # -------------------------------------
    # Result
    # -------------------------------------

    return render_template(

        "result.html",

        image=file.filename,

        medicines=medicines,

        text=text,

        prediction=prediction,

        probability=probability,

        reminder_time=reminder_time,

        age=age,

        gender=gender,

        chronic=chronic,

        doses=doses,

        treatment_days=treatment_days,

        missed=missed

    )


# ==========================================================
# Reminder Page
# ==========================================================

@app.route("/reminder")
def reminder():
    return render_template("reminder.html")


# ==========================================================
# Success Page
# ==========================================================

@app.route("/success")
def success():
    return render_template("success.html")


# ==========================================================
# Run
# ==========================================================

if __name__ == "__main__":
    app.run(debug=True)