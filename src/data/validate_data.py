import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "raw" / "customer_data.csv"


def validate_data():
    df = pd.read_csv(DATA_PATH)

    print("DATA VALIDATION")
    print("----------------")
    print("Rows and Columns:", df.shape)
    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:", df.duplicated().sum())

    print("\nData Types:")
    print(df.dtypes)

    print("\nValidation completed!")


if __name__ == "__main__":
    validate_data()