import pymongo
from pymongo import MongoClient

# connection to mongodb
client = MongoClient('localhost', 27017)

# create a db with name
db = client.testdb

# create a collection
persons_coll = db.persons

persons_coll.create_index([("name", pymongo.ASCENDING)])
persons_coll.create_index([("surname", pymongo.ASCENDING)])
persons_coll.create_index([("computer", pymongo.ASCENDING)])

# create a document
p1 = {"name": "Mario", "surname": "Rossi", "eta": 30,
      "computer": ["asus", "apple"]}

# insert document into db
persons_coll.insert_one(p1)

# create a document
p2 = {"name": "Giuseppe", "surname": "Verdi", "eta": 45,
      "computer": ["apple"]}

# insert document into db
persons_coll.insert_one(p2)
