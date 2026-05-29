from pathlib import Path

from fastapi import FastAPI, HTTPException
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
    try:
        sessions = parse_agenda_file(str(AGENDA_FILE))
        matched_session, matched_score = find_best_session(
            data.professional_focus,
            sessions or DEFAULT_SESSIONS,
        )

        if not matched_session:
            raise HTTPException(status_code=404, detail="No matching session found")

        return {
            "name": data.name,
            "email": data.email,
            "professional_focus": data.professional_focus,
            "matched_session": matched_session,
            "score": matched_score,
        }
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="agenda.txt file not found")