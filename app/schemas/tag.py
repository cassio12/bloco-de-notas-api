from pydantic import BaseModel

class TagBase(BaseModel):
    name: str

class TagCreate(TagBase):
    pass

class TagUpdate(BaseModel):
    name: str | None = None


class TagResponse(TagBase):
    id: int

    class Config:
        orm_mode = True