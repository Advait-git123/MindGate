# backend/models/token.py
from sqlalchemy import Column, String
from utils.database import Base

class Token(Base):
    __tablename__ = "tokens"

    user_id = Column(String, primary_key=True)
    token = Column(String, unique=True, nullable=False)

