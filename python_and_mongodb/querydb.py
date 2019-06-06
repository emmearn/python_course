from python_and_mongodb.mongodb_connector import MongodbConnector


mongodb = MongodbConnector()

p = mongodb.find_one()
print(p)

print("***")
ps = mongodb.find({"computer": "apple"})
for person in ps:
    print(person)

print("***")
res = mongodb.update({"name": "Giuseppe"}, {"$set": {"eta": 50}})

print("***")
ps2 = mongodb.find({"name": "Giuseppe"})
for person in ps2:
    print(person)
