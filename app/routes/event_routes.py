from pathlib import Path

from fastapi import APIRouter

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
		return EventResponse(
			status="failed",
			matched_session=None,
			draft_email="No matching session found",
		)

	prompt = build_prompt(data.name, data.professional_focus, matched_session)
	draft_email = generate_email_draft(prompt)

	send_draft_via_mcp(data.email, draft_email)

	return EventResponse(
		status="success",
		matched_session=matched_session,
		draft_email=draft_email,
	)