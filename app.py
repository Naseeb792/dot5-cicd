from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

@app.route('/feature-y')
def featurey():
    return 'feature-y'

if __name__ == "__main__":
    app.run()
