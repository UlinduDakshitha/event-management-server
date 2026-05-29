from pathlib import Path

from fastapi import APIRouter, HTTPException

from app.schemas.response import EventResponse
from app.schemas.visitor import VisitorInput
from app.services.agenda_parser import parse_agenda_file
from app.services.ai_generator import generate_email_draft
from app.services.matcher import find_best_session
from app.services.mcp_service import send_draft_via_mcp
from app.services.prompt_builder import build_prompt

router = APIRouter()

AGENDA_FILE = Path(__file__).resolve().parents[2] / "agenda.txt"


@router.get("/health")
def health_check():
	return {"status": "ok"}


@router.post("/submit", response_model=EventResponse)
def submit_form(data: VisitorInput):
	sessions = parse_agenda_file(str(AGENDA_FILE))
	matched_session, _ = find_best_session(data.professional_focus, sessions)

	if not matched_session:
		raise HTTPException(status_code=404, detail="No matching session found")

	session_summary = (
		f"{matched_session.get('title', 'N/A')} | "
		f"Time: {matched_session.get('time', 'N/A')} | "
		f"Speaker: {matched_session.get('speaker', 'N/A')}"
	)

	prompt = build_prompt(data.name, data.professional_focus, session_summary)
	draft_email = generate_email_draft(prompt)

	send_draft_via_mcp(data.email, draft_email)

	return EventResponse(
		status="success",
		matched_session=session_summary,
		draft_email=draft_email,
	)