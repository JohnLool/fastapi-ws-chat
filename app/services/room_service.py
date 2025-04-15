from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.room_repo import RoomRepository
from app.schemas.room import RoomOut, RoomCreate
from app.services.base_service import BaseService


class RoomService(BaseService[RoomRepository]):
    def __init__(self, db: AsyncSession):
        super().__init__(RoomRepository(db), RoomOut)

    async def create_room(self, data: RoomCreate) -> Optional[RoomOut]:
        return await super().create(data)

    async def get_room(self, room_id: int) -> Optional[RoomOut]:
        return await super().get_by_id(room_id)

    async def list_rooms(self) -> list[RoomOut]:
        return await super().get_all()