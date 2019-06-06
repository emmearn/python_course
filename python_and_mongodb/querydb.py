from python_and_mongodb.mongodb_connector import MongodbConnector


mongodb = MongodbConnector()

p = mongodb.find_one()
print(p)

print("***")
ps = mongodb.find({"computer": "apple"})
for person in ps:
    print(person)
