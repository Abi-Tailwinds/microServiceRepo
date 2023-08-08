from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/repo2", methods=["GET"])
def say_hello():
    print(" Welcome from Repo2")
    return " Welcome from Repo2!"


if __name__ == "__main__":
    # Please do not set debug=True in production
    app.run(host="0.0.0.0", port=5080, debug=True)
