from sqlalchemy.ext.asyncio import AsyncSession

from app.models import RoomOrm
from app.repositories.base_repo import BaseRepository


class RoomRepository(BaseRepository[RoomOrm]):
    def __init__(self, session: AsyncSession):
        super().__init__(RoomOrm, session)
