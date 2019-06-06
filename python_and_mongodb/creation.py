from python_and_mongodb.mongodb_connector import MongodbConnector

mongodb = MongodbConnector()

# create a document
p1 = {"name": "Mario", "surname": "Rossi", "eta": 30,
      "computer": ["asus", "apple"]}

# insert document into db
mongodb.insert(p1)

# create a document
p2 = {"name": "Giuseppe", "surname": "Verdi", "eta": 45,
      "computer": ["apple"]}

# insert document into db
mongodb.insert(p2)
