import pandas as pd
from pathlib import Path

RAW_PATH = Path(__file__).resolve().parents[2] / "data" / "raw" / "customer_data.csv"
PROCESSED_PATH = Path(__file__).resolve().parents[2] / "data" / "processed" / "customer_data_processed.csv"


def preprocess_data():
    df = pd.read_csv(RAW_PATH)

    # Convert Gender into numerical values
    df["Gender"] = df["Gender"].map({"Male": 0, "Female": 1})

    # Remove CustomerID because it is only an identifier
    df = df.drop(columns=["CustomerID"])

    # Save processed data
    PROCESSED_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED_PATH, index=False)

    print("Preprocessing completed!")
    print("Processed shape:", df.shape)
    print("\nProcessed data:")
    print(df.head())


if __name__ == "__main__":
    preprocess_data()