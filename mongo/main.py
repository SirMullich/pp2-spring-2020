'''
    Courtesy of w3 schools
    https://www.w3schools.com/python/python_mongodb_getstarted.asp
'''


import pymongo


def create():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    mydict = {"name": "John", "address": "Highway 37"} # entry

    res = mycol.insert_one(mydict)

    print(myclient.list_database_names())
    print(mydb.list_collection_names())
    print(res.inserted_id)


def create_multiple():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    mylist = [
        {"name": "Amy", "address": "Apple st 652"},
        {"name": "Hannah", "address": "Mountain 21"},
        {"name": "Michael", "address": "Valley 345"},
        {"name": "Sandy", "address": "Ocean blvd 2"},
        {"name": "Betty", "address": "Green Grass 1"},
        {"name": "Richard", "address": "Sky st 331"},
        {"name": "Susan", "address": "One way 98"},
        {"name": "Vicky", "address": "Yellow Garden 2"},
        {"name": "Ben", "address": "Park Lane 38"},
        {"name": "William", "address": "Central st 954"},
        {"name": "Chuck", "address": "Main Road 989"},
        {"name": "Viola", "address": "Sideway 1633"}
    ]

    res = mycol.insert_many(mylist)

    print(myclient.list_database_names())
    print(mydb.list_collection_names())
    print(res.inserted_ids)


def create_multiple_with_ids():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    mylist = [
        {"_id": 1, "name": "John", "address": "Highway 37"},
        {"_id": 2, "name": "Peter", "address": "Lowstreet 27"},
        {"_id": 3, "name": "Amy", "address": "Apple st 652"},
        {"_id": 4, "name": "Hannah", "address": "Mountain 21"},
        {"_id": 5, "name": "Michael", "address": "Valley 345"},
        {"_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
        {"_id": 7, "name": "Betty", "address": "Green Grass 1"},
        {"_id": 8, "name": "Richard", "address": "Sky st 331"},
        {"_id": 9, "name": "Susan", "address": "One way 98"},
        {"_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
        {"_id": 11, "name": "Ben", "address": "Park Lane 38"},
        {"_id": 12, "name": "William", "address": "Central st 954"},
        {"_id": 13, "name": "Chuck", "address": "Main Road 989"},
        {"_id": 14, "name": "Viola", "address": "Sideway 1633"}
    ]

    res = mycol.insert_many(mylist)
    print(res.inserted_ids)


def find_one():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    res = mycol.find_one()
    print(res)


def find_many():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    for entry in mycol.find():
        print(entry)

def find_some_fields():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    for entry in mycol.find({}, {"_id": 0, "name": 1, "address": 1}):
        print(entry)

def find_some_fields_zero():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    for entry in mycol.find({}, {"address": 0}):
        print(entry)


def query1():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    for entry in mycol.find({"address": "Park Lane 38"}):
        print(entry)

def query2():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    for entry in mycol.find({"address": {"$gt": "S"}}):
        print(entry)

def query3():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    for entry in mycol.find({"address": {"$regex": "^S"}}):
        print(entry)

def sort():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    for entry in mycol.find().sort("name"):
        print(entry)

def sort_descending():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    for entry in mycol.find().sort("name", -1):
        print(entry)


def delete_one():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    mycol.delete_one({"address": "Mountain 21"})

def delete_many():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    res = mycol.delete_many({ "address": {"$regex": "^S"} })

    print(res.deleted_count, " documents deleted")

def delete_all():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    res = mycol.delete_many({})

    print(res.deleted_count, " documents deleted")

def drop_collection():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]
    mycol.drop()

def list_collections():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    print(mydb.list_collection_names())


def update_one():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    mycol.update_one({ "address": "Valley 345" }, { "$set": { "address": "Canyon 123" } })

    for doc in mycol.find():
        print(doc)

def update_many():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    res = mycol.update_many({ "address": { "$regex": "^S" } }, { "$set": { "name": "Minnie" } })

    print(res.modified_count, " documents updated.")


def limit():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    for doc in mycol.find().limit(5):
        print(doc)

if __name__ == '__main__':
    # x = 100
    # y = 100 * 10
    #
    # print(y)
    #
    # name = input()
    # store name in file data.csv
    # Risks:
    # 1 - Hard Drive (SSD) gets destroyed
    # cannot directly search in data.csv
    # print("Hi " + name)


    # create()
    # create_multiple()
    # create_multiple_with_ids()
    # find_one()
    # find_many()
    # find_some_fields()
    # find_some_fields_zero()
    # query1()
    # query2()
    # query3()
    # sort()
    # sort_descending()
    # delete_one()
    # delete_many()
    # delete_all()
    # drop_collection()
    # list_collections()
    # update_one()
    # update_many()
    limit()