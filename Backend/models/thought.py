from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from utils.database import Base

class Thought(Base):
    __tablename__ = "thoughts"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, nullable=False)
    text = Column(String, nullable=False)
    sentiment = Column(String, default="neutral")
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
