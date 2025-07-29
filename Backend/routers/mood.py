from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, models
from ..database import get_db

router = APIRouter(prefix="/mood", tags=["Mood Journal"])

@router.post("/")
def log_mood(entry: schemas.MoodEntryCreate, db: Session = Depends(get_db)):
    mood = models.MoodEntry(**entry.dict())
    db.add(mood)
    db.commit()
    db.refresh(mood)
    return mood

@router.get("/{user_id}")
def get_mood_entries(user_id: str, db: Session = Depends(get_db)):
    return db.query(models.MoodEntry).filter(models.MoodEntry.user_id == user_id).all()