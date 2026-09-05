from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.payment import Payment
from app.services.recovery_service import (
    payment_failure_summary,
    recovery_score,
    revenue_at_risk,
)

router = APIRouter(
    prefix="/analytics",
    tags=["Revenue Intelligence"]
)


@router.get("/failures")
def get_failure_summary(db: Session = Depends(get_db)):
    return payment_failure_summary(db)


@router.get("/revenue")
def get_revenue_at_risk(db: Session = Depends(get_db)):
    return revenue_at_risk(db)


@router.get("/recovery-score/{payment_id}")
def get_recovery_score(payment_id: int, db: Session = Depends(get_db)):
    payment = db.query(Payment).filter(Payment.id == payment_id).first()

    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")

    return {
        "payment_id": payment.id,
        "recovery_score": recovery_score(payment)
    }