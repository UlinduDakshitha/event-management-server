from fastapi import FastAPI
from app.models import VisitorInput
from app.services.matcher import find_best_session

app = FastAPI(
    title="Event Assistant API",
    description="API for matching visitor interests with agenda sessions",
    version="1.0.0",
)


@app.get("/")
def home():
    return {"message": "Event Assistant API is running"}


@app.post("/submit")
def submit_form(data: VisitorInput):
    matched_session = find_best_session(data.professional_focus)

    return {
        "message": "Form received successfully",
        "name": data.name,
        "email": data.email,
        "professional_focus": data.professional_focus,
        "matched_session": matched_session,
    }