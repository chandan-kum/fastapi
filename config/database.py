from pymongo import MongoClient

client = MongoClient("mongodb+srv://chandan:chandan123@cluster0.w7p4dt6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.pcm

collection_name = db["users"]



