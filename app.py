from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/feature-z")
def featurez():
    return "feature-z"

if __name__ == "__main__":
    app.run()
