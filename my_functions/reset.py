import pandas as pd

def reset(id: bool, all: bool):
    if id == True:

        df = pd.read_csv("expenses.csv")

        for idx, row in df.iterrows():
            df.at[idx, "ID"] = idx

        df.to_csv("expenses.csv", index=False)
    
    if all == True:
        df = pd.read_csv("expenses.csv")

        df = df.head(0)

        df.to_csv("expenses.csv", index=False)