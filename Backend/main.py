# mindmate/main.py

from fastapi import FastAPI
from routers import mood, thought, anchor, brain
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="MindMate API",
    description="Mental fitness, journaling, and brain gym backend",
    version="1.0.0"
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

@app.get("/")
def root():
    return {"message": "Welcome to MindMate API!"}
