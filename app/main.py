from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.models import VisitorInput
from app.services.agenda_parser import parse_agenda_file
from app.services.ai_generator import generate_email_draft
from app.services.matcher import DEFAULT_SESSIONS, find_best_session
from app.services.mcp import send_draft_via_mcp
from app.services.prompt_builder import build_invitation_prompt

app = FastAPI(
    title="Event Assistant API",
    description="API for matching visitor interests with agenda sessions",
    version="1.0.0",
)

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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

        invitation_prompt = build_invitation_prompt(
            visitor_name=data.name,
            professional_focus=data.professional_focus,
            matched_session=matched_session,
        )
        send_draft_via_mcp(data.email, invitation_prompt)

        return {
            "name": data.name,
            "email": data.email,
            "professional_focus": data.professional_focus,
            "matched_session": matched_session,
            "score": matched_score,
            "invitation_prompt": invitation_prompt,
            "draft_sent": True,
        }
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="agenda.txt file not found")


@app.post("/generate-draft")
def generate_draft(data: VisitorInput):
    try:
        sessions = parse_agenda_file(str(AGENDA_FILE))
        best_session, score = find_best_session(
            data.professional_focus,
            sessions or DEFAULT_SESSIONS,
        )

        if not best_session:
            raise HTTPException(status_code=404, detail="No matching session found")

        prompt = build_invitation_prompt(
            visitor_name=data.name,
            professional_focus=data.professional_focus,
            matched_session=best_session,
        )
        draft_email = generate_email_draft(prompt)

        send_draft_via_mcp(data.email, draft_email)

        return {
            "message": "Draft generated successfully",
            "prompt_used": prompt,
            "matched_session": best_session,
            "draft_email": draft_email,
            "score": score,
        }
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="agenda.txt file not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))