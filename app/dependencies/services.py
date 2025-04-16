from typing import Annotated

from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_session
from app.services.chat_service import ChatService
from app.services.connection_manager import connection_manager, ConnectionManager
from app.services.message_service import MessageService
from app.services.room_service import RoomService


async def get_connection_manager() -> ConnectionManager:
    return connection_manager

async def get_room_service(
    db: Annotated[AsyncSession, Depends(get_session)],
) -> RoomService:
    return RoomService(db)

async def get_message_service(
        db: Annotated[AsyncSession, Depends(get_session)],
) -> MessageService:
    return MessageService(db)

async def get_chat_service(
        room_service: Annotated[RoomService, Depends(get_room_service)],
        message_service: Annotated[MessageService, Depends(get_message_service)],
        conn_manager: Annotated[ConnectionManager, Depends(get_connection_manager)],
) -> ChatService:
    return ChatService(room_service, message_service, conn_manager)