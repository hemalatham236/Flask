from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Varenya!</p>"

@app.route("/ping", methods=['GET'])
def ping():
    return "<p>Hey man! why are pinging me</p>"

@app.route("/jjjjjj", methods = ["GET"])
def jjjjjj():
    return "<p>Hey man! i'm hear"