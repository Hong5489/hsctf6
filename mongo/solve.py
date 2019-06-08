from pymongo import MongoClient
client = MongoClient('mongodb://admin:keithkeithkeith@keith-logger-mongodb.web.chal.hsctf.com', 27017)
cursor = client['database']['collection'].find({})
for document in cursor:
	print document