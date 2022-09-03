import pymongo
import os
from dotenv import load_dotenv
import pymongo

host = os.environ("ip_address")
MONGO_CONN = pymongo.MongoClient('mongodb://%s' % (host))

def conn_mongodb():
    try:
        MONGO_CONN.admin.command('ismaster')
        blog_ab = MONGO_CONN.blog_session_db.blog_ab
    except:
        MONGO_CONN = pymongo.MongoClient('mongodb://%s' % (host))
        blog_ab = MONGO_CONN.blog_session_db.blog_ab
    return blog_ab
