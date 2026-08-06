import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("../dataset/medicine_adherence_dataset.csv")

print("Original Dataset:")
print(df.head())

# Create LabelEncoder
encoder = LabelEncoder()

# Encode categorical columns
df["gender"] = encoder.fit_transform(df["gender"])
# Female = 0, Male = 1

df["chronic_disease"] = encoder.fit_transform(df["chronic_disease"])
# No = 0, Yes = 1

df["reminder_used"] = encoder.fit_transform(df["reminder_used"])
# No = 0, Yes = 1

df["adherence"] = encoder.fit_transform(df["adherence"])
# High = 0, Low = 1 (or vice versa depending on LabelEncoder)

print("\nEncoded Dataset:")
print(df.head())

# Save encoded dataset
df.to_csv("../dataset/medicine_encoded.csv", index=False)

print("\nDataset saved as dataset/medicine_encoded.csv")