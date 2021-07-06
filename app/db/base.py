from pymongo import MongoClient


client = MongoClient("db", 27017)
db = client["PollDatabase"]
poll_collection = db['poll']



