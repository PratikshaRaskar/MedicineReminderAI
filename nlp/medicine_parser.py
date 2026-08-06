import re

medicine_database = [
    "Paracetamol",
    "Crocin",
    "Azithromycin",
    "Amoxicillin",
    "Vitamin C",
    "Dolo 650",
    "Cetirizine",
    "Pantoprazole",
    "Metformin",
    "Aspirin",
    "Ibuprofen",
    "Omeprazole"
]

def extract_medicines(text):

    medicines = []

    for medicine in medicine_database:

        pattern = r"\b" + re.escape(medicine) + r"\b"

        if re.search(pattern, text, re.IGNORECASE):
            medicines.append(medicine)

    return medicines