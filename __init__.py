from flask import Flask, jsonify, request, render_template, session
from flask_cors import CORS
import os
from dotenv import load_dotenv
import control.mgmt

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    webpage_name = control.mgmt.ExplorerSession.get_explorer_page() 
    control.mgmt.ExplorerSession.save_session_info(session['client_ip'], 'anonymous', webpage_name)
    # print(control.mgmt.ExplorerSession.get_explorer_page())
    return render_template('explorer_A.html')

@app.route("/cardano")
def cardano():
    return render_template('cardano.html')


@app.route("/solana")
def solana():
    return render_template('solana.html')


@app.route("/avalanche")
def avalanche():
    return render_template('avalanche.html')

@app.before_request
def app_before_request():
    if 'client_id' not in session:
        session['client_id'] = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)