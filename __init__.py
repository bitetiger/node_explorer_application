from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return render_template('index.html')

@app.route("/hello")
def hello_flask():
    return "<h1>Hello Flash!</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)