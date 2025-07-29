from datetime import timedelta, datetime

def get_reminder_dates(created_at: datetime):
    intervals = [2, 7, 14, 30]
    return [created_at + timedelta(days=i) for i in intervals]
