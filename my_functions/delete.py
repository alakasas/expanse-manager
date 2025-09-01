import pandas as pd

def delete(id: int):
    df = pd.read_csv("expenses.csv")

    df = df.loc[df["ID"] != id]

    df.to_csv("expenses.csv", index=False)