import random
from faker import Faker
import pandas as pd
from datetime import datetime, timedelta

fake = Faker()

random.seed(42)

NUM_RECORDS = 10000

payment_methods = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Net Banking",
    "Wallet"
]

subscription_types = [
    "Monthly",
    "Quarterly",
    "Annual"
]

failure_reasons = [
    "Insufficient Funds",
    "Card Expired",
    "Bank Timeout",
    "Network Error",
    "Fraud Suspected",
    "User Cancelled",
    "Invalid CVV",
    "UPI Failure"
]

bank_responses = [
    "Approved",
    "Declined",
    "Timeout",
    "Processing Error",
    "Blocked"
]

rows = []

start_date = datetime.now() - timedelta(days=180)

for i in range(1, NUM_RECORDS + 1):

    status = random.choices(
        ["SUCCESS", "FAILED"],
        weights=[75, 25]
    )[0]

    amount = random.randint(99, 25000)

    retry_count = random.randint(0, 3)

    payment_date = start_date + timedelta(
        minutes=random.randint(0, 250000)
    )

    if status == "SUCCESS":
        failure_reason = ""
        recoverable = 0
        bank_response = "Approved"
    else:
        failure_reason = random.choice(failure_reasons)

        recoverable = 1 if failure_reason in [
            "Insufficient Funds",
            "Network Error",
            "Bank Timeout",
            "UPI Failure"
        ] else 0

        bank_response = random.choice(bank_responses)

    rows.append({
        "payment_id": f"PAY{i:06}",
        "customer_id": f"CUST{random.randint(1000,9999)}",
        "amount": amount,
        "payment_method": random.choice(payment_methods),
        "subscription_type": random.choice(subscription_types),
        "status": status,
        "failure_reason": failure_reason,
        "retry_count": retry_count,
        "bank_response": bank_response,
        "recoverable": recoverable,
        "payment_date": payment_date
    })

df = pd.DataFrame(rows)

df.to_csv("data/payments.csv", index=False)

print("Dataset created successfully!")
print(df.head())
print()
print("Total Records:", len(df))