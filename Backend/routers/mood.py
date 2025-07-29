from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.mood import Mood
from utils.database import get_db

router = APIRouter()

@router.post("/mood")
def log_mood(user_id: str, mood: str, db: Session = Depends(get_db)):
    entry = Mood(user_id=user_id, mood=mood)
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return {"message": "Mood logged", "mood": entry.mood, "timestamp": entry.timestamp}

@router.get("/mood/{user_id}")
def get_mood_history(user_id: str, db: Session = Depends(get_db)):
    return db.query(Mood).filter(Mood.user_id == user_id).order_by(Mood.timestamp.desc()).all()
