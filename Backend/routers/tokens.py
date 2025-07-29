# backend/routes/token.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from utils.database import get_db
from models.tokens import Token

router = APIRouter()

@router.post("/register_token/")
def register_token(user_id: str, token: str, db: Session = Depends(get_db)):
    existing = db.query(Token).filter(Token.user_id == user_id).first()
    if existing:
        existing.token = token
    else:
        entry = Token(user_id=user_id, token=token)
        db.add(entry)
    db.commit()
    return {"message": "Token registered"}
