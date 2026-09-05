import pandas as pd


class Analytics:

    def __init__(self, df):
        self.df = df.copy()

    def total_payments(self):
        return len(self.df)

    def failed_payments(self):
        return len(self.df[self.df["status"] == "FAILED"])

    def successful_payments(self):
        return len(self.df[self.df["status"] == "SUCCESS"])

    def total_revenue(self):
        return float(self.df["amount"].sum())

    def failed_revenue(self):
        return float(
            self.df[self.df["status"] == "FAILED"]["amount"].sum()
        )

    def recoverable_revenue(self):
        return float(
            self.df[
                (self.df["status"] == "FAILED") &
                (self.df["recoverable"] == 1)
            ]["amount"].sum()
        )

    def recovery_rate(self):
        failed = self.failed_payments()

        if failed == 0:
            return 0

        recoverable = len(
            self.df[
                (self.df["status"] == "FAILED") &
                (self.df["recoverable"] == 1)
            ]
        )

        return round((recoverable / failed) * 100, 2)

    def payment_method_distribution(self):
        return (
            self.df["payment_method"]
            .value_counts()
            .reset_index(name="count")
            .rename(columns={"index": "payment_method"})
        )

    def failure_reason_distribution(self):
        return (
            self.df[self.df["status"] == "FAILED"]["failure_reason"]
            .value_counts()
            .reset_index(name="count")
            .rename(columns={"index": "failure_reason"})
        )

    def priority_distribution(self):
        if "priority" not in self.df.columns:
            return pd.DataFrame()

        return (
            self.df["priority"]
            .value_counts()
            .reset_index(name="count")
            .rename(columns={"index": "priority"})
        )

    def top_recovery_opportunities(self):

        if "expected_recovery" not in self.df.columns:
            return pd.DataFrame()

        return (
            self.df.sort_values(
                "expected_recovery",
                ascending=False
            )
            .head(10)
        )

    def summary(self):

        return {
            "Total Payments": self.total_payments(),
            "Successful Payments": self.successful_payments(),
            "Failed Payments": self.failed_payments(),
            "Total Revenue": self.total_revenue(),
            "Revenue At Risk": self.failed_revenue(),
            "Recoverable Revenue": self.recoverable_revenue(),
            "Recovery Rate (%)": self.recovery_rate(),
        }


if __name__ == "__main__":

    df = pd.read_csv("data/recovery_predictions.csv")

    analytics = Analytics(df)

    print(analytics.summary())