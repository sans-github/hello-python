from pathlib import Path
import os

import pandas as pd


def hello_panda():
    df_raw = _load_csv_data()
    df = df_raw

    # Column operations
    df = df_raw.columns  # Show columns
    df = df_raw.info()  # Column description, memory usage
    df = df_raw.describe()  # Count, mean, median, percentile

    # Slicing operations on column. [start:stop:step]
    df = df_raw.columns[:2]  # First 2 columns.
    df = df_raw.columns[2:5]  # Columns at index 2, 3, 4
    df = df = df_raw.columns[-2:]  # Last 2 columns
    df = df_raw.columns[::2]  # Every other column
    df = df_raw.columns[7:2:-1]  # Start at 7, going back to 2

    # All rows all columns
    df = df_raw
    df = df_raw.iloc[:, :]
    df = df_raw.loc[:, :]

    # All rows selected columns
    df = df_raw["country"]  # As a series
    df = df_raw[["country"]]  # As a DF
    df = df_raw[["country", "device"]]  # Returns a DF
    df = df_raw.loc[:, ["country"]]
    df = df_raw.loc[:, ["country", "device"]]
    df = df_raw.iloc[:, 2:6]
    df = df_raw.iloc[:, [2, 3, 6]]

    # Selected rows all columns
    df = df_raw[:2]  # 0, 1
    df = df_raw[2:5]  # 2, 3, 4
    df = df_raw[2:5:2]  # 2, 4
    df = df_raw.loc[df_raw["is_fraud"] == 1]
    df = df_raw.loc[::2, :]
    df = df_raw.iloc[::2, :]

    # Selected rows selected columns
    df = df_raw.loc[df_raw["is_fraud"] == 1, ["country", "device"]]
    df = df_raw.loc[1:4, ["country", "is_fraud"]]
    df = df_raw.iloc[::3, [4, 5]]

    # pivot: fraud by country
    df_count = (
        df_raw.loc[df_raw["is_fraud"] == 1, ["country", "device"]]
        .groupby(["country"])
        .size()
        .sort_values(ascending=False)
    )
    df_percent = round(df_count * 100 / df_count.sum(), 2).astype(str) + "%"

    df = pd.DataFrame({"count": df_count, "percent": df_percent})

    # pivot: fraud by country, device
    df_count = (
        df_raw.loc[df_raw["is_fraud"] == 1, ["country", "device"]]
        .groupby(["country", "device"])
        .size()
        .sort_values(ascending=False)
    )
    df_percent = round(df_count * 100 / df_count.sum(), 2).astype(str) + "%"

    df = pd.DataFrame({"count": df_count, "percent": df_percent})

    print(df)

    if isinstance(df, pd.DataFrame):
        print(f"type={type(df)}, size={df.shape}")
    elif isinstance(df, pd.Series):
        print(f"type={type(df)}, size={len(df)}")
    else:
        print(f"type={type(df)}")


def _load_csv_data():
    script_dir = Path(__file__).parent
    csv_path = script_dir.parent / "data/transactions.csv"

    return pd.read_csv(csv_path)


if __name__ == "__main__":
    os.system("clear")
    hello_panda()
