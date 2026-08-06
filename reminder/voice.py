import pyttsx3

# -----------------------------
# Initialize Text-to-Speech Engine
# -----------------------------

engine = pyttsx3.init()

engine.setProperty("rate", 150)      # Speech speed
engine.setProperty("volume", 1.0)    # Volume (0.0 - 1.0)

# Select female voice if available
voices = engine.getProperty("voices")

if len(voices) > 1:
    engine.setProperty("voice", voices[1].id)


# -----------------------------
# Speak Any Text
# -----------------------------

def speak(text):
    """
    Speak any text.
    """

    try:
        engine.say(text)
        engine.runAndWait()

    except Exception as e:
        print("Voice Error:", e)


# -----------------------------
# Speak Medicine Reminder
# -----------------------------

def speak_reminder(medicine):
    """
    Speak reminder for one medicine.
    """

    message = (
        f"This is your medicine reminder. "
        f"Please take your medicine {medicine} now. "
        f"Take it with water and follow your doctor's instructions."
    )

    speak(message)


# -----------------------------
# Speak Multiple Medicines
# -----------------------------

def speak_multiple_reminders(medicines):
    """
    Speak reminder for multiple medicines.
    """

    if not medicines:
        speak("No medicines detected.")
        return

    speak("The following medicines were detected.")

    for medicine in medicines:
        speak(f"Please take {medicine}")


# -----------------------------
# General Reminder
# -----------------------------

def general_reminder():

    message = (
        "It is time to take your medicines. "
        "Please do not miss your scheduled dose. "
        "Stay healthy."
    )

    speak(message)


# -----------------------------
# Test
# -----------------------------

if __name__ == "__main__":

    print("Testing Voice Reminder...")

    speak_reminder("Paracetamol")

    print("Voice test completed.")