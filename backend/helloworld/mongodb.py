from pymongo import MongoClient
client = MongoClient("mongodb+srv://XXXXXX:XXXXXXX@cluster0-swsn8.mongodb.net/test?retryWrites=true&w=majority")

#Makes a db inside the cluster
db = client.cheese

#Makes a collection called customers
mycol = db["customers"]

mydict = { "name": "Bob", "address": "Highway 37" }

#inserts the document into the customers collection
x = mycol.insert_one(mydict)

print("Hello world")
print(x.inserted_id)
