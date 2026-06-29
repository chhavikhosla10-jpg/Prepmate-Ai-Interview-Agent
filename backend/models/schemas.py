from pydantic import BaseModel, Field

class InterviewRequest(BaseModel):
    resume_text: str = Field(..., min_length=10)
    target_role: str = Field(..., min_length=2)

class InterviewResponse(BaseModel):
    result: str
    source: str
    note: str | None = None
