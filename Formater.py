from datetime import datetime

def today():
    return str(datetime.now().strftime("%Y-%m-%d"))