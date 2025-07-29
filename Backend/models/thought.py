from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database import Base

class ThoughtEntry(Base):
    __tablename__ = "thought_entries"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.uid"))
    thought = Column(String)
    sentiment = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="thoughts")