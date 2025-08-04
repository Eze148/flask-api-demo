from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"message": "Hello, world! This is running on the cloud 🚀"})


# New endpoint: /about (GET)
@app.route("/about")
def about():
    return jsonify({"about": "This is a sample Flask API with multiple endpoints."})


# New endpoint: /echo (POST)
from flask import request


@app.route("/echo", methods=["POST"])
def echo():
    data = request.get_json()
    return jsonify({"you_sent": data}), 201


# New endpoint: /add (POST)
@app.route("/add", methods=["POST"])
def add():
    data = request.get_json()
    a = data.get("a")
    b = data.get("b")
    if a is None or b is None:
        return jsonify({"error": "Missing a or b"}), 400
    try:
        result = float(a) + float(b)
    except Exception:
        return jsonify({"error": "a and b must be numbers"}), 400
    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True)
