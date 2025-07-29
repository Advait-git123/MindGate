from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from utils.database import Base

class Exercise(Base):
    __tablename__ = "exercises"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    question = Column(String)
    completed = Column(Boolean, default=False)
    date = Column(DateTime(timezone=True), server_default=func.now())
