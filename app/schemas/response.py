from pydantic import BaseModel

class EventResponse(BaseModel):
    status: str
    matched_session: str
    draft_email: str


class DraftResponse(BaseModel):
    message: str
    draft_email: str