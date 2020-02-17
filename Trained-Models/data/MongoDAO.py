from pymongo import MongoClient
import pandas as pd
import csv
import json

client = MongoClient('mongodb://35.154.86.182:27017/')

db = client.fyp_data
print(db)
stdRecords = db.student


def insert_csv(path):
    global stdRecords
    j = {}
    with open(path) as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        print(rows)
        j = json.loads(json.dumps(rows))

    stdRecords.insert_many(j)


def get_data_frame():
    global stdRecords
    x = stdRecords.find({})
    lst = []
    for i in x:
        lst.append(i)
    return pd.DataFrame.from_dict(lst, orient='columns')


# insert_csv('sirisaman_full.csv')
# insert_csv('southland_full.csv')
#df = get_data_frame()
#print(df)

