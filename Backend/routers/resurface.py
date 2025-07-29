from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from utils.database import get_db
from utils.resurface import get_resurfaced_entries

router = APIRouter()

@router.get("/resurface/{user_id}")
def resurface_entries(user_id: str, db: Session = Depends(get_db)):
    resurfaced = get_resurfaced_entries(user_id, db)
    return {"resurfaced_entries": resurfaced}
