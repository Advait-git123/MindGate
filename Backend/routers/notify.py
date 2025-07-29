from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from utils.database import get_db
from models.anchor import Anchor
from utils.scheduler import is_due
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

class NotifyRequest(BaseModel):
    user_id: str
    method: str = "mock"  # options: "mock", "email", "push"

@router.post("/notify")
def mock_notify(req: NotifyRequest, db: Session = Depends(get_db)):
    anchors = db.query(Anchor).filter(Anchor.user_id == req.user_id).all()
    due = [a for a in anchors if is_due(a.timestamp)]
    count = len(due)
    # In real use: integrate Firebase or email logic here
    return {
        "user": req.user_id,
        "method": req.method,
        "reminder_count": count,
        "timestamp": datetime.utcnow().isoformat()
    }
