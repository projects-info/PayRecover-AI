from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.models.base import Base

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)

    merchant_id = Column(Integer, ForeignKey("merchants.id"))
    customer_id = Column(Integer, ForeignKey("customers.id"))

    amount = Column(Float)

    payment_method = Column(String)

    bank = Column(String)

    payment_status = Column(String)

    failure_reason = Column(String)