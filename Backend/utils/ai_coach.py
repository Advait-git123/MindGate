from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from models.mood import MoodEntry
from models.exercise import BrainExerciseSubmission
from utils.llm import call_local_llm  # assumes you have this helper already

def get_recent_mood_and_exercises(user_id: str, db: Session):
    week_ago = datetime.utcnow() - timedelta(days=7)

    moods = db.query(MoodEntry).filter(
        MoodEntry.user_id == user_id,
        MoodEntry.timestamp >= week_ago
    ).order_by(MoodEntry.timestamp.desc()).all()

    exercises = db.query(BrainExerciseSubmission).filter(
        BrainExerciseSubmission.user_id == user_id,
        BrainExerciseSubmission.timestamp >= week_ago
    ).order_by(BrainExerciseSubmission.timestamp.desc()).all()

    return moods, exercises

def generate_ai_coach_response(user_id: str, db: Session):
    moods, exercises = get_recent_mood_and_exercises(user_id, db)

    mood_text = "\n".join([f"- [{m.timestamp.date()}] {m.mood}: {m.note}" for m in moods])
    exercise_text = "\n".join([f"- [{e.timestamp.date()}] {e.exercise_type}: {e.response}" for e in exercises])

    prompt = f"""
<|system|>
You are MindMate, a compassionate mental fitness coach. Reflect on the user's mood history and recent cognitive activity.
<|user|>
Mood Journal (last 7 days):
{mood_text or 'No entries'}

Brain Exercises (last 7 days):
{exercise_text or 'No activity'}

Please share a warm, thoughtful, and motivating reflection that helps the user stay grounded and continue progressing.
<|assistant|>
"""

    return call_local_llm(prompt)
