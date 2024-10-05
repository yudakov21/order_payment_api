from pydantic import BaseModel
from datetime import datetime

class OrderCreate(BaseModel):
    order_id: int
    user_id: int
    name: str
    quantity: int
    price: float
    created_at: datetime

