import os
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATASET = os.path.join(BASE_DIR, "dataset", "medicine_encoded.csv")

MODEL = os.path.join(BASE_DIR, "models", "adherence_model.pkl")

df = pd.read_csv(DATASET)

X = df.drop(columns=["patient_id", "adherence"])
y = df["adherence"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=200,
    max_depth=8,
    random_state=42
)

model.fit(X_train, y_train)

pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, pred))

joblib.dump(model, MODEL)

print("Model saved successfully.")