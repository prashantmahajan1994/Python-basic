import pymongo
client = pymongo.MongoClient("mongodb+srv://pmahajan:tpP9wL7cDTCoFNCe@cluster0.0gfbg.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

a={
    "name" : "prashant",
    "email.id" : "m.prashantmahajan@gmail.com",
    "password" : "India@2022"
}
db1=client["mongotest"]
coll=db1['test']
coll.insert_one(a)
print("hyhyu")

a=200
print(id(a))

