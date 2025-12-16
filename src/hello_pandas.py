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
    
    df = pd.read_csv(csv_path)
    
    # print(df.columns)
    # print(df.info())
    # print(df.describe())
    
    # print(df['device'].describe())
    # print(df['country'].describe())
    
    # with pd.option_context('display.max_rows', 1):
    #     print(df)
        
    # print(df)
    
    # print(df.columns)
    # print(df.columns[:2])
    # print(df[df.columns[:2]])
    # print(df[df.columns[~2:]])
    
    # print(df.select_dtypes("object"))
    
    print(df['country'])
    print(df[['country']])

    
if __name__=='__main__':
    # hello_panda()
    hello_panda_csv()