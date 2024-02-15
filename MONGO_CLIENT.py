import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["test"]
mycol = mydb["Device_Locations"]

def query_locations(org, id):
    query = { "org": org, "name": id }
    result = mycol.find(query)
    return result