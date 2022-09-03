from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import pymongo
import os
from dotenv import load_dotenv

ip_address=os.environ.get("ip_address")
connection = pymongo.MongoClient()
connection = pymongo.MongoClient('mongodb://%s' % (ip_address))
# connection = pymongo.MongoClient('mongodb://%s:%s@%s' % (username, password, ip_address))
blog_session_db = connection.blog_session_db
blog_ab = blog_session_db.blog_ab

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return render_template('index.html')

@app.route("/cardano")
def cardano():
    return render_template('cardano.html')


@app.route("/solana")
def cardano():
    return render_template('solana.html')


@app.route("/avalanche")
def cardano():
    return render_template('avalanche.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)