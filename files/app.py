from flask import Flask
app = Flask(__name__)

@app.route("/")
def incoming():
    return "ALL OK"