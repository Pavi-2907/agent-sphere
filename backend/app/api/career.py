from fastapi import APIRouter
from backend.app.models.career import CareerRequest

router = APIRouter()


@router.post("/career")
def career(request: CareerRequest):
    return {
        "question_received": request.question
    }