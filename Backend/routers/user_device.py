from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.user import User
from utils.database import get_db
from pydantic import BaseModel

router = APIRouter()

class TokenPayload(BaseModel):
    user_id: str
    fcm_token: str

@router.post("/store_token")
def store_token(body: TokenPayload, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == body.user_id).first()
    if not user:
        raise HTTPException(404, "User not found")
    user.fcm_token = body.fcm_token
    db.commit()
    return {"status": "token stored"}
