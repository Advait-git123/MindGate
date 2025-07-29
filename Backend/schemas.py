from pydantic import BaseModel
from datetime import datetime

class AnchorIn(BaseModel):
    uid: str
    text: str

class AnchorOut(AnchorIn):
    id: int
    created_at: datetime

class MoodIn(BaseModel):
    uid: str
    entry: str

class ThoughtIn(BaseModel):
    uid: str
    content: str
