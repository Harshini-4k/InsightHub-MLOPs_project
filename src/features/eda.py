import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "processed" / "customer_data_processed.csv"


def perform_eda():
    df = pd.read_csv(DATA_PATH)

    print("EDA")
    print("---")
    print("\nStatistical Summary:")
    print(df.describe())

    # Distribution of Annual Income
    plt.figure(figsize=(8, 5))
    plt.hist(df["Annual Income (k$)"], bins=10)
    plt.title("Annual Income Distribution")
    plt.xlabel("Annual Income (k$)")
    plt.ylabel("Number of Customers")
    plt.show()

    # Distribution of Spending Score
    plt.figure(figsize=(8, 5))
    plt.hist(df["Spending Score (1-100)"], bins=10)
    plt.title("Spending Score Distribution")
    plt.xlabel("Spending Score")
    plt.ylabel("Number of Customers")
    plt.show()


if __name__ == "__main__":
    perform_eda()