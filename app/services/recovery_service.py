from collections import Counter
from sqlalchemy.orm import Session
from app.models.payment import Payment


def payment_failure_summary(db: Session):
    failed = db.query(Payment).filter(
        Payment.payment_status == "Failed"
    ).all()

    total_failed = len(failed)

    reasons = Counter(
        payment.failure_reason for payment in failed
    )

    return {
        "total_failed_payments": total_failed,
        "failure_reasons": dict(reasons)
    }
def recovery_score(payment):
    score = 0

    if payment.failure_reason == "UPI Timeout":
        score += 40

    if payment.payment_method == "UPI":
        score += 30

    if payment.amount < 5000:
        score += 30

    return min(score, 100)
def revenue_at_risk(db: Session):
    failed = db.query(Payment).filter(
        Payment.payment_status == "Failed"
    ).all()

    total = sum(payment.amount for payment in failed)

    return {
        "failed_payments": len(failed),
        "revenue_at_risk": total
    }