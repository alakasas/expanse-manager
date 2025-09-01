import pandas as pd

def update(id: int, name:str | None, amount:float | None):
    df = pd.read_csv("expenses.csv")
    row_idx = df.loc[df["ID"] == id].index[0]

    if name is not None:
        df.at[row_idx, "Name"] = name

    if amount is not None:
        df.at[row_idx, "Amount"] = amount

    df.to_csv("expenses.csv", index=False)
