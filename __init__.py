from flask import Flask, jsonify, request, render_template, session
from flask_cors import CORS
import os
from dotenv import load_dotenv
import control.mgmt

app = Flask(__name__)
CORS(app)
app.secret_key = 'secretkey'

@app.route('/')
def home():
    control.mgmt.ExplorerSession.save_session_info(session['ip'], 'home')
    return render_template('index.html')

@app.before_request
def app_before_request():
         session['ip'] = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
         print(session['ip'], '이게 아이피다!!')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)