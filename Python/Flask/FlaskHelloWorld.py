from flask import Flask
app = Flask("HelloWorld")

@app.route("/")
def hello():
    return "Hallo Welt"

@app.route("/data")
def data():
    return "Generating data ..."


if __name__ == "__main__":
    app.run(port=(8421))