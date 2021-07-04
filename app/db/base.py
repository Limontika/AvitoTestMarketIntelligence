from pymongo import MongoClient


client = MongoClient()
db = client["PollDatabase"]
poll_collection = db['poll']



