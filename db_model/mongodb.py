import pymongo
import os
from dotenv import load_dotenv
import pymongo

host = os.environ.get("ip_address")
username = os.environ.get("username")
password = os.environ.get("password")

def conn_mongodb():
        MONGO_CONN = pymongo.MongoClient('mongodb://%s:%s@%s' % (username, password, host))
        explorer_db_col = MONGO_CONN.explorer_session_db.explorer_collection
        return explorer_db_col
