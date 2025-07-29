import time
from datetime import datetime
from utils.database import SessionLocal
from utils.notify import get_due_thoughts
from utils.firebase_messaging import send_fcm
from models.user import User

def notify_job():
    db = SessionLocal()
    try:
        dues = get_due_thoughts(db)
        for uid, thoughts in dues.items():
            user = db.query(User).filter(User.id == uid).first()
            if not user or not user.fcm_token:
                continue
            body = f"You have {len(thoughts)} anchors to revisit."
            send_fcm(user.fcm_token, "MindMate Reminder", body)
        print(f"Run at {datetime.utcnow().isoformat()}")
    finally:
        db.close()

if __name__ == "__main__":
    while True:
        notify_job()
        time.sleep(24 * 3600)  # Sleep 1 day
