from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from utils.database import get_db
from utils.notify import get_due_thoughts
from utils.firebase_messaging import send_fcm
from models.user import User

router = APIRouter()

@router.get("/notify")
def notify_all(db: Session = Depends(get_db)):
    due_by_user = get_due_thoughts(db)
    sent = []

    for uid, thoughts in due_by_user.items():
        user = db.query(User).filter(User.id == uid).first()
        if not user or not user.fcm_token:
            continue

        body = f"You have {len(thoughts)} anchors to reflect on today"
        result = send_fcm(user.fcm_token, "MindMate Reminder", body)
        sent.append({"user": uid, "result": result})

    return {"sent_notifications": sent}
