from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

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