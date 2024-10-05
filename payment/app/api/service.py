import httpx
from fastapi import HTTPException
from app.config import ORDER_SERVICE_URL

async def get_order(order_id: int):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{ORDER_SERVICE_URL}/{order_id}")
            response.raise_for_status()  # Raise exception for non-2xx status codes
            return response.json()
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            raise HTTPException(status_code=404, detail=f"Order with ID {order_id} not found.")
        else:
            raise HTTPException(status_code=500, detail="Internal server error")
    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail=f"Error connecting to order service: {str(e)}")


