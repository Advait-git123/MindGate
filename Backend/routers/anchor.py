from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.anchor import Anchor
from schemas import AnchorIn, AnchorOut

router = APIRouter(prefix="/anchor")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=AnchorOut)
def create_anchor(anchor: AnchorIn, db: Session = Depends(get_db)):
    db_anchor = Anchor(**anchor.dict())
    db.add(db_anchor)
    db.commit()
    db.refresh(db_anchor)
    return db_anchor

@router.get("/{uid}", response_model=list[AnchorOut])
def get_anchors(uid: str, db: Session = Depends(get_db)):
    return db.query(Anchor).filter(Anchor.uid == uid).all()
