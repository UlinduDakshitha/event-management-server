from pydantic import BaseModel

class EventResponse(BaseModel):
    status: str
    matched_session_id: str
    matched_session_title: str
    matched_session_time: str
    draft_email: str


class DraftResponse(BaseModel):
    message: str
    draft_email: str