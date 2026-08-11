from pydantic import BaseModel


class CareerRequest(BaseModel):
    question: str