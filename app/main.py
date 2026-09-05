from fastapi import FastAPI
import pandas as pd

app = FastAPI(
    title="PayRecover AI",
    version="1.0"
)

@app.get("/")
def home():
    return {
        "message": "PayRecover AI API Running 🚀"
    }

@app.get("/summary")
def summary():

    df = pd.read_csv("data/recovery_predictions.csv")

    return {
        "total_payments": len(df),
        "failed_payments": len(df[df["status"]=="FAILED"]),
        "recoverable": len(df[df["recoverable"]==1]),
        "revenue_at_risk": float(df[df["status"]=="FAILED"]["amount"].sum()),
        "recoverable_revenue": float(df[df["recoverable"]==1]["amount"].sum())
    }