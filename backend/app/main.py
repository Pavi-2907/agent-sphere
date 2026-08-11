from fastapi import FastAPI
from backend.app.api.career import router as career_router

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Welcome to AgentSphere"}


app.include_router(career_router)