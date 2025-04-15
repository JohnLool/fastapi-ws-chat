from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from app.models import MessageOrm
from app.repositories.message_repo import MessageRepository
from app.schemas.message import MessageOut, MessageCreate
from app.services.base_service import BaseService


class MessageService(BaseService[MessageRepository]):
    def __init__(self, db: AsyncSession):
        super().__init__(MessageRepository(db), MessageOut)

    async def create_message(self, data: MessageCreate) -> Optional[MessageOut]:
        return await super().create(data)

    async def get_room_messages(self, room_id: int) -> list[MessageOut]:
        filters = [MessageOrm.room_id == room_id]
        return await super().get_all(*filters)