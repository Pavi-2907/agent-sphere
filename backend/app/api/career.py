from fastapi import APIRouter

from backend.app.models.career import CareerRequest
from backend.app.services.llm_service import generate_response


router = APIRouter()


@router.post("/career")
def career(request: CareerRequest):
    answer = generate_response(request.question)

    return {
        "question": request.question,
        "answer": answer
    }