import pandas as pd
import random

random.seed(42)

rows = []

for i in range(1000):

    age = random.randint(18, 85)

    gender = random.choice(["Male", "Female"])

    chronic = random.choice(["Yes", "No"])

    medicines = random.randint(1, 6)

    doses = random.randint(1, 4)

    treatment = random.randint(5, 90)

    missed = random.randint(0, 10)

    reminder = random.choice(["Yes", "No"])

    score = 100

    # Age
    if age > 65:
        score -= 8

    # Medicines
    score -= medicines * 4

    # Doses
    score -= doses * 6

    # Treatment duration
    if treatment > 30:
        score -= 10

    # Previous missed doses
    score -= missed * 7

    # Reminder helps
    if reminder == "Yes":
        score += 18

    # Chronic disease slightly lowers adherence
    if chronic == "Yes":
        score -= 5

    score += random.randint(-8, 8)

    adherence = 1 if score >= 55 else 0

    rows.append([
        i + 1,
        age,
        gender,
        chronic,
        medicines,
        doses,
        treatment,
        missed,
        reminder,
        adherence
    ])

columns = [
    "patient_id",
    "age",
    "gender",
    "chronic_disease",
    "medicines_count",
    "doses_per_day",
    "treatment_days",
    "previous_missed_doses",
    "reminder_used",
    "adherence"
]

df = pd.DataFrame(rows, columns=columns)

df.to_csv("../dataset/medicine_dataset.csv", index=False)

print(df.head())
print(df["adherence"].value_counts())