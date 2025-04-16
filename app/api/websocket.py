from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends

from app.dependencies.auth import validate_token
from app.services.chat_service import ChatService
from app.dependencies.services import get_chat_service


router = APIRouter()

@router.websocket("/ws/{room_id}")
async def websocket_endpoint(
    websocket: WebSocket,
    room_id: int,
    chat_service: ChatService = Depends(get_chat_service),
):
    token = websocket.headers.get("sec-websocket-protocol")
    if not token:
        await websocket.close(code=1008, reason="Missing authentication token.")
        return

    try:
        user_payload = await validate_token(token)
    except Exception as e:
        await websocket.close(code=1008, reason=str(e))
        return

    await websocket.accept(subprotocol=token)

    await chat_service.connect(room_id, websocket)

    try:
        while True:
            data = await websocket.receive_json()
            await chat_service.handle_incoming_message(room_id, user_payload, data)
    except WebSocketDisconnect:
        await chat_service.disconnect(room_id, websocket)