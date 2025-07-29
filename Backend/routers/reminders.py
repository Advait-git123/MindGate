from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.anchor import Anchor
from utils.database import get_db
from utils.scheduler import is_due  # the one we just wrote

router = APIRouter()

@router.get("/reminders/{user_id}")
def get_reminders(user_id: str, db: Session = Depends(get_db)):
    anchors = db.query(Anchor).filter(Anchor.user_id == user_id).all()
    due_anchors = [a for a in anchors if is_due(a.timestamp)]  # or a.timestamp, a.stage if you added stage
    return {
        "reminders_due": len(due_anchors),
        "anchors": [
            {
                "id": a.id,
                "text": a.text,
                "timestamp": a.timestamp,
                "emotion": a.emotion,
                "type": a.type,
            }
            for a in due_anchors
        ]
    }
