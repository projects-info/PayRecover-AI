import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="PayRecover AI", layout="wide")

st.title("💰 PayRecover AI Dashboard")

df = pd.read_csv("data/recovery_predictions.csv")

# ---------------- KPIs ----------------

total = len(df)
failed = len(df[df["status"] == "FAILED"])
success = len(df[df["status"] == "SUCCESS"])
recoverable = len(df[df["recoverable"] == 1])

risk = df[df["status"] == "FAILED"]["amount"].sum()
recoverable_amount = df[df["recoverable"] == 1]["amount"].sum()

c1, c2, c3 = st.columns(3)
c4, c5, c6 = st.columns(3)

c1.metric("Total Payments", total)
c2.metric("Successful", success)
c3.metric("Failed", failed)
c4.metric("Recoverable", recoverable)
c5.metric("Revenue At Risk", f"₹{risk:,.0f}")
c6.metric("Recoverable Revenue", f"₹{recoverable_amount:,.0f}")

st.divider()

left, right = st.columns(2)

with left:

    fig = px.pie(
        df,
        names="payment_method",
        title="Payment Methods"
    )

    st.plotly_chart(fig, use_container_width=True)

with right:

    failures = (
        df[df["status"] == "FAILED"]
        .groupby("failure_reason")
        .size()
        .reset_index(name="count")
    )

    fig = px.bar(
        failures,
        x="failure_reason",
        y="count",
        title="Failure Reasons"
    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()

fig = px.histogram(
    df,
    x="recovery_score",
    color="priority",
    nbins=20,
    title="Recovery Score Distribution"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

st.subheader("🤖 AI Recommendations")

cols = [
    "payment_id",
    "amount",
    "failure_reason",
    "recovery_score",
    "priority",
    "recommended_action",
    "confidence",
    "expected_recovery"
]

st.dataframe(
    df[cols].sort_values(
        "recovery_score",
        ascending=False
    ),
    use_container_width=True
)

st.success("PayRecover AI Dashboard Running Successfully 🚀")