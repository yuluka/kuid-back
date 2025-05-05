from typing import Optional
from pydantic import BaseModel

class ChatBase(BaseModel):
    query: str
    messages: list[dict[str, str]]

    class Config:
        from_attributes = True

class ChatIn(ChatBase):
    pass

class ChatOut(ChatBase):
    answer: str

    class Config:
        from_attributes = True