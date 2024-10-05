import httpx
from fastapi import HTTPException
from app.config import USER_SERVICE_URL

async def get_user(user_id: int):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{USER_SERVICE_URL}/{user_id}")
            response.raise_for_status()  # Бросает исключение для не 2xx кодов статуса
            return response.json()
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            raise HTTPException(status_code=404, detail=f"User с ID {user_id} не найден.")
        else:
            raise HTTPException(status_code=500, detail="Внутренняя ошибка сервера.")
    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail=f"Ошибка соединения с микросервисом user: {str(e)}")
