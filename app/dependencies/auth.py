from fastapi import APIRouter
import httpx

AUTH_SERVICE_URL = "http://auth-backend:8000/token-validate"

router = APIRouter()


async def validate_token(token: str) -> dict:
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                AUTH_SERVICE_URL,
                headers={"Authorization": f"Bearer {token}"}
            )
        except httpx.RequestError:
            raise Exception("Failed to contact the authentication service.")

    if response.status_code != 200:
        raise Exception("Token validation failed.")

    user_payload = response.json()
    if not all(key in user_payload for key in ("sub", "user_id")):
        raise Exception("Invalid token payload format.")

    return user_payload