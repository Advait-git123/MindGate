from fastapi import APIRouter
import random

router = APIRouter(prefix="/brain", tags=["Brain Gym"])

questions = [
    {"q": "What is 15 + 27?", "a": "42"},
    {"q": "Reverse the word 'developer'", "a": "repoleved"},
    {"q": "Name a fruit that starts with 'B'", "a": "Banana"},
    {"q": "What comes next: 2, 4, 6, ?", "a": "8"},
    {"q": "Spell 'conscious' backwards", "a": "suoicsnoc"}
]

@router.get("/")
def get_brain_gym_question():
    return random.choice(questions)