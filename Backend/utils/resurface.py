from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from models.mood import MoodEntry

def get_resurfaced_entries(user_id: str, db: Session):
    now = datetime.utcnow()
    offsets = [7, 30, 90]  # days ago
    resurfaced = []

    for days in offsets:
        target_date = now - timedelta(days=days)
        window_start = target_date - timedelta(days=1)
        window_end = target_date + timedelta(days=1)

        entry = db.query(MoodEntry).filter(
            MoodEntry.user_id == user_id,
            MoodEntry.timestamp >= window_start,
            MoodEntry.timestamp <= window_end
        ).first()

        if entry:
            resurfaced.append({
                "days_ago": days,
                "mood": entry.mood,
                "note": entry.note,
                "timestamp": entry.timestamp.isoformat()
            })

    return resurfaced
