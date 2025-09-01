import pandas as pd

def list_csv():

    df = pd.read_csv("expenses.csv")
    print(df.to_string(index=False))

