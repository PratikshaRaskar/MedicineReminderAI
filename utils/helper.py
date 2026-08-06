from datetime import datetime

def current_time():

    return datetime.now().strftime("%H:%M")

def current_date():

    return datetime.now().strftime("%d-%m-%Y")