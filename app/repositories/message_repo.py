from sqlalchemy.ext.asyncio import AsyncSession

from app.models.message import MessageOrm
from app.repositories.base_repo import BaseRepository


class MessageRepository(BaseRepository[MessageOrm]):
    def __init__(self, session: AsyncSession):
        super().__init__(MessageOrm, session)
