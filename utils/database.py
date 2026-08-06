import sqlite3

DB_NAME = "medicine.db"


# -----------------------------
# Connection
# -----------------------------
def get_connection():
    return sqlite3.connect(DB_NAME)


# -----------------------------
# Create Tables
# -----------------------------
def create_table():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS medicines(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        medicine TEXT,
        prescription TEXT,
        prediction TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS reminders(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        medicine TEXT,
        reminder_time TEXT
    )
    """)

    conn.commit()
    conn.close()


# -----------------------------
# Save Medicine
# -----------------------------
def save_medicine(medicine, prescription, prediction):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO medicines
        (medicine,prescription,prediction)
        VALUES(?,?,?)
        """,
        (medicine, prescription, prediction)
    )

    conn.commit()
    conn.close()


# -----------------------------
# Save Reminder
# -----------------------------
def save_reminder(medicine, reminder_time):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO reminders
        (medicine,reminder_time)
        VALUES(?,?)
        """,
        (medicine, reminder_time)
    )

    conn.commit()
    conn.close()


# -----------------------------
# Dashboard Statistics
# -----------------------------
def get_total_medicines():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM medicines")

    total = cur.fetchone()[0]

    conn.close()

    return total


def get_high_adherence():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT COUNT(*)
        FROM medicines
        WHERE prediction='High Adherence'
    """)

    total = cur.fetchone()[0]

    conn.close()

    return total


def get_low_adherence():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT COUNT(*)
        FROM medicines
        WHERE prediction='Low Adherence'
    """)

    total = cur.fetchone()[0]

    conn.close()

    return total


def get_adherence_percentage():

    total = get_total_medicines()

    if total == 0:
        return 0

    high = get_high_adherence()

    return round((high / total) * 100, 2)


def get_recent_predictions(limit=7):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT prediction
        FROM medicines
        ORDER BY id DESC
        LIMIT ?
    """, (limit,))

    data = cur.fetchall()

    conn.close()

    data.reverse()

    chart = []

    for row in data:
        if row[0] == "High Adherence":
            chart.append(95)
        else:
            chart.append(45)

    return chart