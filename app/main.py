from pathlib import Path

from fastapi import FastAPI
from app.models import VisitorInput
from app.services.agenda_parser import parse_agenda_file
from app.services.matcher import DEFAULT_SESSIONS, find_best_session

app = FastAPI(
    title="Event Assistant API",
    description="API for matching visitor interests with agenda sessions",
    version="1.0.0",
)

AGENDA_FILE = Path(__file__).resolve().parent.parent / "agenda.txt"


@app.get("/")
def home():
    return {"message": "Event Assistant API is running"}


@app.post("/match")
def match_session(data: VisitorInput):
    sessions = parse_agenda_file(str(AGENDA_FILE))
    matched_session, matched_score = find_best_session(data.professional_focus, sessions or DEFAULT_SESSIONS)

    return {
        "name": data.name,
        "email": data.email,
        "professional_focus": data.professional_focus,
        "matched_session": matched_session,
        "score": matched_score,
    }