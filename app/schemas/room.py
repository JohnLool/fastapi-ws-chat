from pydantic import BaseModel, ConfigDict


class RoomBase(BaseModel):
    user_1_id: int
    user_2_id: int


class RoomCreate(RoomBase):
    pass


class RoomOut(RoomBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
