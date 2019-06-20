from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hallo Welt"

@app.route("/data")
def data():
    return "Generating data ..."


if __name__ == "__main__":
    app.run()