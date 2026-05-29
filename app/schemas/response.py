from pydantic import BaseModel

class DraftResponse(BaseModel):
    message: str
    draft_email: str