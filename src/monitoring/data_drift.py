import pandas as pd
from pathlib import Path

BASE_PATH = Path(__file__).resolve().parents[2]

DATA_PATH = BASE_PATH / "data" / "processed" / "segmentation_data.csv"


def check_data():
    df = pd.read_csv(DATA_PATH)

    print("InsightHub Data Monitoring")
    print("--------------------------")

    print("Rows:", df.shape[0])
    print("Columns:", df.shape[1])

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nFeature Statistics:")
    print(df.describe())


if __name__ == "__main__":
    check_data()