"""
app.py
------
A simple Flask application for the IELTS Speaking Test platform.

Features:
- Route `/` returns a welcome message.
- Route `/welcome` accepts a 'name' query parameter and returns a personalized JSON message.

Usage:
    FLASK_APP=app.py flask run
    # or simply
    python app.py
"""

from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    """
    Root route.
    Returns a simple greeting.
    """
    return "Hello, Test Taker!", 200

@app.route("/welcome", methods=["GET"])
def welcome():
    """
    Welcome route.
    Accepts a 'name' query parameter and returns a personalized JSON message.
    Handles missing or empty name gracefully.
    """
    name = request.args.get('name', default=None, type=str)
    if name is None:
        # Missing 'name' parameter
        return make_response(jsonify({"error": "Missing 'name' query parameter."}), 400)
    if not name.strip():
        # Empty name
        return make_response(jsonify({"error": "Name cannot be empty."}), 400)
    clean_name = name.strip()
    message = f"Welcome to the IELTS Speaking Test, {clean_name}!"
    return jsonify({"message": message})

if __name__ == "__main__":
    # For direct execution
    app.run(debug=True)