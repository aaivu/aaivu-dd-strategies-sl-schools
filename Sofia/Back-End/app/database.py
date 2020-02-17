import pprint
from mongoengine import connect
from pymongo import MongoClient
import pandas as pd
import csv
import json


def init():
    connect('fyp_data_new', host='178.128.26.214', port=27017)
    
client = MongoClient('mongodb://178.128.26.214:27017')

db = client.fyp_data_new
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


x = get_data_frame()
    

