from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from utils.database import get_db
from utils.ai_coach import generate_ai_coach_response

router = APIRouter()

@router.get("/ai-coach/{user_id}")
def get_ai_coach_insight(user_id: str, db: Session = Depends(get_db)):
    response = generate_ai_coach_response(user_id, db)
    return {"coach_response": response}
