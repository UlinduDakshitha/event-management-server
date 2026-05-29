from fastapi import FastAPI
from app.models import VisitorInput

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
    return {
        "message": "Form received successfully",
        "name": data.name,
        "email": data.email,
        "professional_focus": data.professional_focus,
    }