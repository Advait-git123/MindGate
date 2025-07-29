from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.thought import Thought
from utils.database import get_db
from utils.sentiment import get_sentiment


router = APIRouter()

@router.post("/thought")
def log_thought(user_id: str, text: str, db: Session = Depends(get_db)):
    sentiment = get_sentiment(text)
    entry = Thought(user_id=user_id, text=text, sentiment=sentiment)
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return {
        "message": "Thought logged",
        "text": entry.text,
        "sentiment": entry.sentiment,
        "timestamp": entry.timestamp,
    }

@router.get("/thought/{user_id}")
def get_thoughts(user_id: str, db: Session = Depends(get_db)):
    return db.query(Thought).filter(Thought.user_id == user_id).order_by(Thought.timestamp.desc()).all()
