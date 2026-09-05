# 💰 PayRecover AI

## AI-Powered Revenue Recovery Platform

PayRecover AI is an intelligent payment recovery system that detects failed payments, predicts recoverability, estimates revenue at risk, and recommends AI-driven recovery actions.

---

## Features

- AI Recovery Scoring
- Failed Payment Analysis
- Revenue at Risk Estimation
- Intelligent Recovery Recommendations
- FastAPI REST API
- Streamlit Dashboard
- SQLite Database
- Synthetic Payment Dataset (10,000+ records)

---

## Architecture

Payments Dataset
        │
        ▼
Revenue Engine
        │
        ▼
Recovery Score
        │
        ▼
AI Recovery Agent
        │
        ▼
Analytics
        │
        ▼
Streamlit Dashboard

---

## Tech Stack

- Python
- FastAPI
- Streamlit
- Pandas
- Plotly
- SQLite

---

## Run

Generate AI predictions

python app/recovery_agent.py

Run Dashboard

python -m streamlit run dashboard/dashboard.py

Run API

python -m uvicorn app.main:app --reload

---

## Dashboard

- Payment Analytics
- Revenue at Risk
- Recovery Score Distribution
- AI Recommendations
- Payment Method Analysis
- Failure Reason Analysis

---

## Future Improvements

- Gemini/OpenAI Integration
- Razorpay API Integration
- Automated Retry Engine
- Email & SMS Recovery
- ML-based Recovery Prediction