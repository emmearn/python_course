from python_and_mongodb.mongodb_connector import MongodbConnector


mongodb = MongodbConnector()

p = mongodb.find_one()
print(p)

print("***")
ps = mongodb.find({"computer": "apple"})
for person in ps:
    print(person)

res = mongodb.update({"name": "Giuseppe"}, {"$set": {"eta": 50}})

print("***")
p2 = mongodb.find_with({"name": "Giuseppe"})
print(p2)

print("***")
p3 = mongodb.find_with({"name": {"$gt": "Giuseppe"}})
print(p3)
