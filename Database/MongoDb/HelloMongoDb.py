import datetime
from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client['test']

collection = db['test']

post = {"author": "Lansi",
        "text": "This Is The First Document!",
        "tags": ["mongodb", "python", "pymongo", "linux", "pizza"],
        "date": datetime.datetime.utcnow()}

collection.insert_one(post)
