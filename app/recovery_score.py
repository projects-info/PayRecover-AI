import pandas as pd

class RecoveryScorer:

    def __init__(self, df):
        self.df = df.copy()

    def calculate_score(self, row):

        score = 50

        if row["recoverable"] == 1:
            score += 30

        if row["amount"] > 10000:
            score += 10

        if row["retry_count"] == 0:
            score += 10

        if row["failure_reason"] == "Network Error":
            score += 10

        if row["failure_reason"] == "Bank Timeout":
            score += 10

        if row["failure_reason"] == "Insufficient Funds":
            score += 5

        if row["failure_reason"] == "Card Expired":
            score -= 15

        if row["failure_reason"] == "Fraud Suspected":
            score -= 30

        return max(0, min(score, 100))

    def predict(self):

        self.df["recovery_score"] = self.df.apply(
            self.calculate_score,
            axis=1
        )

        self.df["priority"] = self.df["recovery_score"].apply(
            lambda x:
            "Critical" if x >= 90 else
            "High" if x >= 75 else
            "Medium" if x >= 50 else
            "Low"
        )

        return self.df