import pandas as pd
from pathlib import Path

INPUT_PATH = Path(__file__).resolve().parents[2] / "data" / "processed" / "customer_data_processed.csv"
OUTPUT_PATH = Path(__file__).resolve().parents[2] / "data" / "processed" / "segmentation_data.csv"


def create_features():
    df = pd.read_csv(INPUT_PATH)

    # Features used for customer segmentation
    features = df[
        [
            "Age",
            "Annual Income (k$)",
            "Spending Score (1-100)"
        ]
    ]

    features.to_csv(OUTPUT_PATH, index=False)

    print("Feature engineering completed!")
    print("Features used:")
    print(features.columns.tolist())
    print("\nShape:", features.shape)


if __name__ == "__main__":
    create_features()