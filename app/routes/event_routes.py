from fastapi import APIRouter, HTTPException

from app.schemas.response import EventResponse
from app.schemas.visitor import VisitorInput
from app.services.ai_generator import generate_email_draft
from app.services.matcher import find_best_session
from app.services.mcp_service import send_draft_via_mcp
from app.services.prompt_builder import build_prompt

router = APIRouter()


@router.get("/health")
def health_check():
	return {"status": "ok"}


@router.post("/submit", response_model=EventResponse)
def submit_form(data: VisitorInput):
	matched_session = find_best_session(data.professional_focus)

	if not matched_session:
		raise HTTPException(status_code=404, detail="No matching session found")

	prompt = build_prompt(data.name, data.professional_focus, matched_session)
	draft_email = generate_email_draft(prompt)

	send_draft_via_mcp(data.email, draft_email)

	return EventResponse(
		status="success",
		matched_session_id=matched_session.get("id", ""),
		matched_session_title=matched_session.get("title", ""),
		matched_session_time=matched_session.get("time", ""),
		draft_email=draft_email,
	)