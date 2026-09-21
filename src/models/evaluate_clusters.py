import pandas as pd
from pathlib import Path
from sklearn.metrics import silhouette_score

BASE_PATH = Path(__file__).resolve().parents[2]

DATA_PATH = BASE_PATH / "data" / "processed" / "customer_segments.csv"


def evaluate_clusters():
    df = pd.read_csv(DATA_PATH)

    X = df[
        [
            "Age",
            "Annual Income (k$)",
            "Spending Score (1-100)"
        ]
    ]

    labels = df["Cluster"]

    score = silhouette_score(X, labels)

    print("Cluster Evaluation")
    print("-------------------")
    print(f"Silhouette Score: {score:.4f}")


if __name__ == "__main__":
    evaluate_clusters()