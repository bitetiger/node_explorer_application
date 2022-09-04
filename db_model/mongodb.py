import pymongo
import os
from dotenv import load_dotenv
import pymongo

host = os.environ.get("ip_address")
MONGO_CONN = pymongo.MongoClient('mongodb://%s' % (host))

def conn_mongodb():
        MONGO_CONN = pymongo.MongoClient('mongodb://%s' % (host))
