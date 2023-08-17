from datetime import datetime, timedelta

def get_hour_array():
    now = datetime.now()
    current_hour = now.hour
    hour_array = []
    
    for i in range(0, 8):
        if i == 0:
            hour = current_hour - 1.5
        else:
            hour = current_hour - (i * 3)
        
        if hour < 0:
            hour += 24
        
        if hour >= 12:
            if hour > 12:
                hour -= 12
            hour_array.append(f"{int(hour)}:30 PM")
        else:
            if hour == 0:
                hour = 12
            hour_array.append(f"{int(hour)}:30 AM")
    
    return hour_array

def get_last_7_days():
    days = []
    for i in range(0, 7):
        day = datetime.now() - timedelta(days=i)
        days.append(day.strftime('%A')[:3])
    return days


