from urllib.request import urlopen
from flask import Flask
from flask import request

from flask import Flask
from flask_ngrok import run_with_ngrok
app = Flask(__name__)


@app.route("/")
def hello():
    return "hello world"


if __name__ == '__main__':
    app.run()