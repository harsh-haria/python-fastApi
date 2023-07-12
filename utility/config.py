from pymongo import MongoClient
from keys.db import MONGODB_URI

conn = MongoClient(MONGODB_URI)
try:
    # Send a ping to confirm a successful connection
    conn.admin.command('ping')
    print("Connected!")
except Exception as e:
    print(e)