from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/repo1", methods=["GET"])
def say_hello():
    print(" Welcome from Repo1")
    return " Welcome from Repo1!"


if __name__ == "__main__":
    # Please do not set debug=True in production
    app.run(host="0.0.0.0", port=4080, debug=True)
