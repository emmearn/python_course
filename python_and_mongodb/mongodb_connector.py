from pymongo import MongoClient
import pymongo


class MongodbConnector:
    def __init__(self):
        # connection to mongodb
        client = MongoClient('localhost', 27017)

        # create or access a db with name
        db = client.testdb

        # create or access to a collection
        self.persons_coll = db.persons

        self.persons_coll.create_index([("name", pymongo.ASCENDING)])
        self.persons_coll.create_index([("surname", pymongo.ASCENDING)])
        self.persons_coll.create_index([("computer", pymongo.ASCENDING)])

    def insert(self, c):
        self.persons_coll.insert_one(c)

    def find_one(self):
        return self.persons_coll.find_one()

    def find(self, q):
        return self.persons_coll.find(q)

    def update(self, q, u):
        self.persons_coll.update_one(q, u)
