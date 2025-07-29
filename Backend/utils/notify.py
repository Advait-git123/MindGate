# backend/utils/notify.py
from sqlalchemy.orm import Session
from models.thought import Thought
from models.token import Token
from utils.database import get_db
from datetime import datetime, timedelta

def get_due_thoughts(db: Session):
    """
    Returns list of user tokens who haven't logged a thought in the last 24 hours.
    """
    cutoff_time = datetime.utcnow() - timedelta(days=1)

    recent_thoughts = (
        db.query(Thought.user_id)
        .filter(Thought.timestamp >= cutoff_time)
        .distinct()
        .all()
    )
    recent_user_ids = {user_id for (user_id,) in recent_thoughts}

    all_tokens = db.query(Token).all()

    due_users = [
        token.token for token in all_tokens if token.user_id not in recent_user_ids
    ]

    return due_users
