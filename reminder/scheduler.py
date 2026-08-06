import schedule
import time

from utils.database import get_connection
from reminder.voice import speak_reminder


def check_reminders():
    conn = get_connection()
    cur = conn.cursor()

    current_time = time.strftime("%H:%M")

    cur.execute("""
        SELECT medicine
        FROM reminders
        WHERE reminder_time=?
    """, (current_time,))

    medicines = cur.fetchall()

    for medicine in medicines:
        message = f"It is time to take {medicine[0]}"
        print(message)
        speak_reminder(message)

    conn.close()


schedule.every(1).minutes.do(check_reminders)

print("Reminder Scheduler Started...")

while True:
    schedule.run_pending()
    time.sleep(1)
    