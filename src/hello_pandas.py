from pathlib import Path
import pandas as pd

def hello_panda():
    df = pd.DataFrame({'num_legs': [2, 4, 8, 0],
                   'num_wings': [2, 0, 0, 0],
                   'num_specimen_seen': [10, 2, 1, 8]},
                  index=['falcon', 'dog', 'spider', 'fish'])
    
    print(df['num_legs'].sample(3, random_state=0))
    print(df['num_legs'].sample(3))
    

def hello_panda_csv():
    # Get the script's directory and build path from there
    script_dir = Path(__file__).parent
    csv_path = script_dir.parent / "data/transactions.csv"
    
    df_raw = pd.read_csv(csv_path)
    
    print('{}{}'.format("\n\n\n", "==START=="))
    print(df_raw.sample(3))
    print('{}{}'.format("\n\n\n", "===▼▼▼▼▼==="))
    
    # df=df_raw.columns # Show columns
    # df=df_raw.info()# Column description, memory usage
    
    # df=df_raw.describe()# Count, mean, median, percentile

    # df=df_raw['device'] # Column selection or column indexing
    # df=df_raw['device'].describe() # Describe selected column
    
    # with pd.option_context('display.max_rows', 1):
    #     print(df_raw) # Will print only 1 raw inside the context
        
    # print(df_raw) # Context no longer valid
    
    # Slicing operations(on column name). [start:stop:step]
    # df_raw.columns[:2]   # First 2 columns. 
    # df_raw.columns[2:5]  # Columns at index 2, 3, 4
    # df=df_raw.columns[-2:]  # Last 2 columns
    # df_raw.columns[::2]  # Every other column
    # df_raw.columns[7:2:-1] # Start at 7, going back to 2 
    
    # df=df_raw.select_dtypes("object")
    
    # Slicing operations (on data frame). [start:stop:step]
    # df=df_raw['country'] # Column selection, as a series
    # df=df_raw[['country']] # Column selection, as DF

    
    # Position-based indexing, not slicing. 
    # df = df_raw.iloc[:, [0, 3]] # Select all rows, and columns 0 and 3
    # df = df_raw.iloc[:5 ]# Select 5 rows, all columns
    # df = df_raw.iloc[:5, : ]# Select 5 rows, all columns
    # df = df_raw.iloc[2:5, :3] # Select rows 2-5, and first 3 column
    # df = df_raw.iloc[2:5, [3]] # Select rows 2-5, and 4rd column
    
    # Row index is the label for each row in a DataFrame, shown on the far left. By default, pandas uses integers (0, 1, 2, 3...) as row indices.
    
    # Label-based indexing
    # df = df_raw.loc[:,'is_fraud'] # all rows, Only is_fraud column
    # df = df_raw.loc[:, ['user_id', 'is_fraud']] # all rows, Indicated columns
    # df = df_raw.loc[1:4, ['user_id', 'is_fraud']] # Rows 1-4, Indicated columns
    
    # Boolean-based indexing
    # df = df_raw.loc[:,'is_fraud'] # all rows, Only is_fraud column
    
    # df=df_raw.loc[df_raw['is_fraud']==1] # All the rows with is_fraud=1
    # df=df_raw.loc[df_raw['is_fraud']==1, ['country', 'is_fraud']] # Rows with is_fraud=1 with country and is_fraud column
    
    df=df_raw[df_raw['is_fraud']==1].groupby('country').size() # Fraud by country
    
    # Pivot by country, show column percent
    # df=_fraud_by_country(df_raw)
    
    # Pivot by country, device, show column percent
    df=_fraud_by_country_device(df_raw)
    
    
    print(df)
    
    if isinstance(df, pd.DataFrame): 
        print("\n  ", df.columns.tolist())
    print(type(df))
    print(df_raw.columns)
    print(f"{"===▲▲▲▲===\n"}")
    
# Single underscore _method is the Python convention for "internal use" - it's not truly private but signals it shouldn't be called externally. Double underscore __method applies name mangling for stricter privacy.    
def _fraud_by_country(df_raw):
    """Private method to calculate fraud counts by country"""    
    # Show fraud by country along with column total
    fraud_by_country=df_raw[df_raw['is_fraud']==1].groupby('country').size() # Fraud by country
    fraud_by_country_pct=round(fraud_by_country*100/fraud_by_country.sum(), 2)
    
    assert fraud_by_country_pct.sum()==100, "The total percentage is not 100"
    
    df=pd.DataFrame({
        'count': fraud_by_country,
        'percent': fraud_by_country_pct.astype(str) + '%'
    })
    return df

def _fraud_by_country_device(df_raw):
    fraud_by_country_device=df_raw[df_raw['is_fraud']==1].groupby(['country', 'device']).size()

    fraud_by_country_device_pct=round(fraud_by_country_device*100/fraud_by_country_device.sum(), 2)
    
    assert fraud_by_country_device_pct.sum()==100, "The total percentage is not 100"
    
    df=pd.DataFrame({
        'count': fraud_by_country_device,
        'percent': fraud_by_country_device_pct.astype(str) + '%'
    })
    return df

if __name__=='__main__':
    # hello_panda()
    hello_panda_csv()