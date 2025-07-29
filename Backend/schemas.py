from pydantic import BaseModel
from datetime import datetime

class AnchorIn(BaseModel):
    user_id: str
    text: str

class AnchorOut(AnchorIn):
    id: int
    created_at: datetime

class MoodIn(BaseModel):
    user_id: str
    entry: str

class ThoughtIn(BaseModel):
    user_id: str
    content: str

class MoodEntryCreate(BaseModel):
    user_id: str
    mood: str
    note: str = None

class ThoughtEntryCreate(BaseModel):
    user_id: str
    thought: str
