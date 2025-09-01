import argparse
import csv
import datetime

def add(name:str, amount:float):
    with open("expenses.csv",newline="",mode="r") as file:
        reader = list(csv.reader(file))
        if len(reader) > 1:
            new_id = 1 + int(reader[-1][0])
        else:
            new_id = 0

    with open("expenses.csv",newline="",mode="a") as file:        
        new_row = [new_id, datetime.date.today(), name, amount]
        writer = csv.writer(file)
        writer.writerow(new_row)