import pandas as pd


class RecoveryAgent:

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def recommend(self, row):

        score = row["recovery_score"]
        reason = str(row["failure_reason"])

        if score >= 90:
            action = "Retry Immediately"
            priority = "Critical"
            confidence = "Very High"

        elif score >= 75:
            action = "Retry within 2 Hours"
            priority = "High"
            confidence = "High"

        elif score >= 60:
            action = "Notify Customer"
            priority = "Medium"
            confidence = "Medium"

        else:
            action = "Manual Review"
            priority = "Low"
            confidence = "Low"

        explanation = {
            "Network Error":
                "Temporary network issue detected. Retry is recommended.",

            "Bank Timeout":
                "The bank did not respond. A retry has a high chance of success.",

            "Insufficient Funds":
                "Customer may succeed after account balance is replenished.",

            "UPI Failure":
                "Suggest retrying using UPI or an alternate payment method.",

            "Card Expired":
                "Customer should update card information before retrying.",

            "Fraud Suspected":
                "Escalate to the fraud/risk team before taking any action.",

            "Invalid CVV":
                "Ask the customer to re-enter the correct CVV.",

            "User Cancelled":
                "No automatic action recommended."
        }

        expected_recovery = row["amount"] * (score / 100)

        return pd.Series({
            "recommended_action": action,
            "priority": priority,
            "confidence": confidence,
            "expected_recovery": round(expected_recovery, 2),
            "ai_reason": explanation.get(
                reason,
                "Manual investigation recommended."
            )
        })

    def run(self):

        ai = self.df.apply(self.recommend, axis=1)

        return pd.concat([self.df, ai], axis=1)


if __name__ == "__main__":

    df = pd.read_csv("data/payments.csv")

    from recovery_score import RecoveryScorer

    scorer = RecoveryScorer(df)

    scored = scorer.predict()

    agent = RecoveryAgent(scored)

    result = agent.run()

    print(result.head())

    result.to_csv(
        "data/recovery_predictions.csv",
        index=False
    )

    print("\nAI recommendations saved to data/recovery_predictions.csv")