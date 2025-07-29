from datetime import datetime, timedelta

SPACED_REPETITION_INTERVALS = [2, 7, 14, 30]  # days

def get_reminder_dates(created_at: datetime):
    return [created_at + timedelta(days=days) for days in SPACED_REPETITION_INTERVALS]

def is_due(timestamp: datetime, current_time: datetime = None) -> bool:
    if current_time is None:
        current_time = datetime.utcnow()
    # Check if now >= any reminder date (within 1 day window)
    for days in SPACED_REPETITION_INTERVALS:
        reminder_date = timestamp + timedelta(days=days)
        if reminder_date <= current_time <= (reminder_date + timedelta(days=1)):
            return True
    return False
