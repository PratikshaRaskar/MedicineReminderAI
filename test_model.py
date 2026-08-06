from models.adherence_model import predict_adherence

print("------ HIGH ADHERENCE TEST ------")
print(
    predict_adherence(
        age=24,
        gender="Female",
        chronic_disease="No",
        medicines_count=1,
        doses_per_day=1,
        treatment_days=5,
        previous_missed_doses=0,
        reminder_used="Yes"
    )
)

print()

print("------ LOW ADHERENCE TEST ------")
print(
    predict_adherence(
        age=75,
        gender="Male",
        chronic_disease="Yes",
        medicines_count=6,
        doses_per_day=4,
        treatment_days=90,
        previous_missed_doses=18,
        reminder_used="No"
    )
)