from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.payment import PaymentCreate, PaymentResponse
from app.services.payment_service import (
    create_payment,
    get_payments,
    get_payment,
    delete_payment,
)

router = APIRouter(prefix="/payments", tags=["Payments"])


@router.post("/", response_model=PaymentResponse)
def add_payment(payment: PaymentCreate, db: Session = Depends(get_db)):
    return create_payment(db, payment)


@router.get("/", response_model=list[PaymentResponse])
def read_payments(db: Session = Depends(get_db)):
    return get_payments(db)


@router.get("/{payment_id}", response_model=PaymentResponse)
def read_payment(payment_id: int, db: Session = Depends(get_db)):
    payment = get_payment(db, payment_id)

    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")

    return payment


@router.delete("/{payment_id}")
def remove_payment(payment_id: int, db: Session = Depends(get_db)):
    payment = delete_payment(db, payment_id)

    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")

    return {"message": "Payment deleted successfully"}