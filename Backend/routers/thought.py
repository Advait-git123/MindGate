from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, models
from ..database import get_db
from ..utils.sentiment import analyze_sentiment

router = APIRouter(prefix="/thought", tags=["Thought Diary"])

@router.post("/")
def log_thought(entry: schemas.ThoughtEntryCreate, db: Session = Depends(get_db)):
    sentiment = analyze_sentiment(entry.thought)
    db_entry = models.ThoughtEntry(user_id=entry.user_id, thought=entry.thought, sentiment=sentiment)
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry

@router.get("/{user_id}")
def get_thoughts(user_id: str, db: Session = Depends(get_db)):
    return db.query(models.ThoughtEntry).filter(models.ThoughtEntry.user_id == user_id).all()