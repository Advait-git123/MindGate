# mindmate/main.py

from fastapi import FastAPI,Request
from routers import mood, thought, anchor, brain
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from routers import reminder,brain_gym,resurface,ai_coach,notify,user_device,tokens


app = FastAPI(
    title="MindMate API",
    description="Mental fitness, journaling, and brain gym backend",
    version="1.0.0"
)

@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": "Internal server error", "detail": str(exc)},
    )

# CORS setup to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
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


@app.get("/")
def root():
    return {"message": "Welcome to MindMate API!"}

@app.get("/ping")
def ping():
    return {"message": "pong"}
