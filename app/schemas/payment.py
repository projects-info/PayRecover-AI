from pydantic import BaseModel
from typing import Optional

class PaymentCreate(BaseModel):
    merchant_id: int
    customer_id: int
    amount: float
    payment_method: str
    bank: str
    payment_status: str
    failure_reason: Optional[str] = None


class PaymentResponse(PaymentCreate):
    id: int

    class Config:
        from_attributes = True