from pathlib import Path

import pandas as pd


def create_df():
    df = pd.DataFrame(
        {
            "num_legs": [2, 4, 8, 0],
            "num_wings": [2, 0, 0, 0],
            "num_specimen_seen": [10, 2, 1, 8],
        },
        index=["falcon", "dog", "spider", "fish"],
    )

    print(df["num_legs"].sample(3, random_state=0))
    print(df["num_legs"].sample(3))

    nums=[1, 2, 3, 4]
    char=['A', 'B', 'C', 'D']

    df = pd.DataFrame(
        {
            "nums": nums, 
            "char" : char
        }
    )

    print(df)

    


def hello_panda_csv():
    df_raw = _load_csv_data()

    print("{}{}".format("\n\n\n", "==START=="))
    print(df_raw.sample(3))
    print("{}{}".format("\n\n\n", "===▼▼▼▼▼==="))

    # Column operations
    # df=df_raw.columns # Show columns
    # df=df_raw.info()# Column description, memory usage

    # Slicing operations on column. [start:stop:step]
    # df=df_raw.columns[:2]   # First 2 columns.
    # df=df_raw.columns[2:5]  # Columns at index 2, 3, 4
    # df=df=df_raw.columns[-2:]  # Last 2 columns
    # df=df_raw.columns[::2]  # Every other column
    # df=df_raw.columns[7:2:-1] # Start at 7, going back to 2

    # df=df_raw.describe()# Count, mean, median, percentile

    # Column selection
    # df=df_raw['device'] # As series
    # df=df_raw[['device']] # As DF
    # df=df_raw[['device', 'country']] # Multiple columns, as DF

    # Rows selection. [start:stop:step]
    # df=df_raw[:2]   # First 2 rows.
    # df=df_raw[2:5]  # Rows 2, 3, 4
    # df=df_raw.select_dtypes("object")

    # Position-based indexing, not slicing.
    # df = df_raw.iloc[:, [0, 3]] # Select all rows, and columns 0 and 3
    # df = df_raw.iloc[:5 ]# Select 5 rows, all columns
    # df = df_raw.iloc[:5, : ]# Select 5 rows, all columns
    # df = df_raw.iloc[2:5, :3] # Select rows 2-5, and first 3 column
    # df = df_raw.iloc[2:5, [3]] # Select rows 2-5, and 4rd column

    # Note: Row index is the label for each row in a DataFrame, shown on the far left. By default, pandas uses integers (0, 1, 2, 3...) as row indices.

    # Label-based indexing
    # df = df_raw.loc[:,'is_fraud'] # all rows, Only is_fraud column
    # df = df_raw.loc[:, ['user_id', 'is_fraud']] # all rows, Indicated columns
    # df = df_raw.loc[1:4, ['user_id', 'is_fraud']] # Rows 1-4, Indicated columns

    # Boolean-based indexing
    # df = df_raw.loc[:,'is_fraud'] # all rows, Only is_fraud column

    # df=df_raw.loc[df_raw['is_fraud']==1] # All the rows with is_fraud=1
    # df=df_raw.loc[df_raw['is_fraud']==1, ['country', 'is_fraud']] # Rows with is_fraud=1 with country and is_fraud column

    # df=df_raw[df_raw['is_fraud']==1].groupby('country').size() # Fraud by country

    # with pd.option_context('display.max_rows', 1):
    #     print(df_raw) # Will print only 1 raw inside the context
    # print(df_raw) # Context no longer valid

    df = df_raw

    print(df)

    if isinstance(df, pd.DataFrame):
        print("\n  ", df.columns.tolist())
    print(type(df))
    print(df_raw.columns)
    print(f"{'===▲▲▲▲===\n'}")


def _load_csv_data():
    script_dir = Path(__file__).parent
    csv_path = script_dir.parent / "data/transactions.csv"

    return pd.read_csv(csv_path)


# Single underscore _method is the Python convention for "internal use" - it's not truly private but signals it shouldn't be called externally. Double underscore __method applies name mangling for stricter privacy.
def _fraud_by_country(df_raw):
    """Private method to calculate fraud counts by country"""
    # Show fraud by country along with column total
    fraud_by_country = (
        df_raw[df_raw["is_fraud"] == 1].groupby("country").size()
    )  # Fraud by country
    fraud_by_country_pct = round(fraud_by_country * 100 / fraud_by_country.sum(), 2)

    assert fraud_by_country_pct.sum() == 100, "The total percentage is not 100"

    df = pd.DataFrame(
        {"count": fraud_by_country, "percent": fraud_by_country_pct.astype(str) + "%"}
    )
    return df


def _fraud_by_country_device(df_raw):
    fraud_by_country_device = (
        df_raw[df_raw["is_fraud"] == 1].groupby(["country", "device"]).size()
    )

    fraud_by_country_device_pct = round(
        fraud_by_country_device * 100 / fraud_by_country_device.sum(), 2
    )

    assert round(fraud_by_country_device_pct.sum()) == 100, print(
        "The total percentage is not 100. {}".format(fraud_by_country_device_pct.sum())
    )

    df = pd.DataFrame(
        {
            "count": fraud_by_country_device,
            "percent": fraud_by_country_device_pct.astype(str) + "%",
        }
    )
    return df


def _fraud_by_user(df_raw):
    fraud_by_user = df_raw[df_raw["is_fraud"] == 1].groupby(["user_id"]).size()

    fraud_by_user_pct = round(fraud_by_user * 100 / fraud_by_user.sum(), 2)

    assert round(fraud_by_user_pct.sum()) == 100, print(
        "The total percentage is not 100. {}".format(fraud_by_user_pct.sum())
    )

    df = (
        pd.DataFrame({"count": fraud_by_user, "percent": fraud_by_user_pct})
        .sort_values("percent", ascending=False)
        .head(10)
    )

    df["percent"] = df["percent"].astype(str) + "%"
    return df


def _fraud_by_country_user():
    df_raw = _load_csv_data()

    fraud_country_user_count = (
        df_raw.loc[df_raw["is_fraud"] == 1, ["country", "user_id"]]
        .groupby(["country", "user_id"])
        .size()
        .sort_values(ascending=False)
    )

    fraud_country_user_percent = (
        fraud_country_user_count * 100 / fraud_country_user_count.sum()
    )

    df = pd.DataFrame(
        {"count": fraud_country_user_count, "percent": fraud_country_user_percent}
    )

    # Display everything. Not just a subset
    with pd.option_context("display.max_rows", None, "display.max_columns", None):
        print(df)


if __name__ == "__main__":
    # create_df()
    hello_panda_csv()
    # _fraud_by_country_user()
    # df=_fraud_by_country(df_raw)
    # df=_fraud_by_country_device(df_raw)
    # df = _fraud_by_user(df_raw)
    pass
