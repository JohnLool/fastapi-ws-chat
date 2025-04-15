from starlette.websockets import WebSocket
from typing import Dict, Any
from app.services.room_service import RoomService
from app.services.message_service import MessageService
from app.services.connection_manager import ConnectionManager
from app.schemas.message import MessageCreate, MessageOut


class ChatService:
    def __init__(
        self,
        room_service: RoomService,
        message_service: MessageService,
        connection_manager: ConnectionManager
    ):
        self.room_service = room_service
        self.message_service = message_service
        self.connection_manager = connection_manager

    async def connect(self, room_id: int, websocket: WebSocket):
        room = await self.room_service.get_room(room_id)
        if not room:
            raise Exception(f"Room {room_id} not found")
        await self.connection_manager.connect(room_id, websocket)

    def disconnect(self, room_id: int, websocket: WebSocket):
        self.connection_manager.disconnect(room_id, websocket)

    async def handle_incoming_message(self, room_id: int, user_payload: Dict[str, Any], data: Dict[str, Any]) -> MessageOut:
        message_data = MessageCreate(
            room_id=room_id,
            user_id=user_payload.get("sub"),
            username=user_payload.get("username"),
            content=data.get("content")
        )
        message = await self.message_service.create_message(message_data)
        await self.connection_manager.broadcast(room_id, message.model_dump_json())
        return message

    async def get_room_messages(self, room_id: int) -> [MessageOut]:
        return await self.message_service.get_room_messages(room_id)
