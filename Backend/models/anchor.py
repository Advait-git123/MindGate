from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from database import Base

class Anchor(Base):
    __tablename__ = "anchors"
    id = Column(Integer, primary_key=True, index=True)
    uid = Column(String, ForeignKey("users.uid"))
    text = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
