import json
import datetime

def get_available_slots(calendar_data):
    today = datetime.date.today()
    return [slot for slot in calendar_data if slot["date"] >= str(today)]

def sync_with_calendar(user_input):
    # Dummy calendar data for demonstration
    calendar_data = [
        {"date": "2025-08-01", "time": "10:00", "status": "available"},
        {"date": "2025-08-02", "time": "14:00", "status": "booked"},
        {"date": "2025-08-03", "time": "11:00", "status": "available"},
    ]
    available_slots = get_available_slots(calendar_data)
    return {"user": user_input, "available_slots": available_slots}

if __name__ == "__main__":
    user_input = {"name": "John Doe", "email": "john@example.com"}
    result = sync_with_calendar(user_input)
    print(json.dumps(result, indent=4))
