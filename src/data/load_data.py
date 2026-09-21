import pandas as pd

from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "raw" / "customer_data.csv"


def load_customer_data():
    df = pd.read_csv(DATA_PATH)

    print("Dataset loaded successfully!")
    print("Shape:", df.shape)
    print("\nFirst 5 rows:")
    print(df.head())

    return df


if __name__ == "__main__":
    load_customer_data()