from pydantic import BaseModel
from datetime import datetime


class PaymentRequest(BaseModel):
    id: int
    order_id: int
    payment_type: str
    status: str
    created_at: datetime
    security_code: str = None
    email_address: str = None