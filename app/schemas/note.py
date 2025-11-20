from pydantic import BaseModel
from typing import List, Optional
from app.schemas.tag import TagResponse

class NoteBase(BaseModel):
    title: str
    content: Optional[str] = None

class NoteCreate(NoteBase):
    tags: Optional[List[int]] = []

class NoteUpdate(NoteBase):
    title: Optional[str] = None
    content: Optional[str] = None
    tags: Optional[List[int]] = None

class NoteResponse(NoteBase):
    id: int
    tags: List['TagResponse'] = []

    class Config:
        orm_mode = True


