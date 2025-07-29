from utils.brain_utils import get_brain_exercises, get_cognitive_test_results
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(prefix="/brain", tags=["Brain Gym"])

router.get("/brain-gym")
def brain_gym():
    return {"exercises": get_brain_exercises()}

router.get("/cognitive-test")
def cognitive_test():
    return {"results": get_cognitive_test_results()}
