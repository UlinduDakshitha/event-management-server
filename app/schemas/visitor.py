from pydantic import BaseModel, EmailStr

class VisitorInput(BaseModel):
    name: str
    email: EmailStr
    professional_focus: str