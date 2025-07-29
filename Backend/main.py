# backend/main.py

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from apscheduler.schedulers.background import BackgroundScheduler

from routers import (
    mood, thought, anchor, brain, reminder, resurface,
    ai_coach, notify, user_device, tokens
)

from utils.firebase import send_push_notification
from utils.notify import get_due_thoughts
from utils.database import engine, SessionLocal
from models import token  # Ensure this exists and is correct
from utils.database import Base

# FastAPI App Metadata
app = FastAPI(
    title="MindMate API",
    description="Mental fitness, journaling, and brain gym backend",
    version="1.0.0"
)

# CORS setup to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this in production!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global exception handler
@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": "Internal server error", "detail": str(exc)},
    )

# Register all routers
app.include_router(mood.router)
app.include_router(thought.router)
app.include_router(anchor.router)
app.include_router(brain.router)
app.include_router(reminder.router)
app.include_router(resurface.router)
app.include_router(ai_coach.router)
app.include_router(notify.router)
app.include_router(user_device.router)
app.include_router(tokens.router)

# Ensure DB tables are created
Base.metadata.create_all(bind=engine)

# Scheduler Job
def notify_users():
    print("[Scheduler] Checking for users to notify...")
    db = SessionLocal()
    try:
        tokens = get_due_thoughts(db)
        for token in tokens:
            send_push_notification(
                token,
                title="🧠 Mental Boost Reminder",
                body="Don't forget to reflect today! Add a thought in MindMate."
            )
    finally:
        db.close()

# Start scheduler at 9 AM every day
scheduler = BackgroundScheduler()
scheduler.add_job(notify_users, "cron", hour=9, minute=0)
scheduler.start()

# Healthcheck endpoints
@app.get("/")
def root():
    return {"message": "Welcome to MindMate API!"}

@app.get("/ping")
def ping():
    return {"message": "pong"}
