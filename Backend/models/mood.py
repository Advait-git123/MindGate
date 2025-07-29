from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from utils.database import Base

class MoodEntry(Base):
    __tablename__ = "mood_entries"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    mood = Column(String)
    note = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
