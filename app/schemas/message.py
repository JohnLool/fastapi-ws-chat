from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional


class MessageBase(BaseModel):
    room_id: int
    user_id: Optional[int] = None
    username: str
    content: str


class MessageCreate(MessageBase):
    pass


class MessageOut(MessageBase):
    id: int
    timestamp: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
