from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Guys welcome to python!!"


if __name__ == "__main__":
    app.debug = True
    app.run(port=4040)
