from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Backend is running 🚀",
        "hostname": socket.gethostname()
    })

@app.route("/health")
def health():
    return "OK", 200

@app.route("/db")
def db():
    db_host = os.getenv("DB_HOST", "not-set")
    return jsonify({
        "db_host": db_host,
        "status": "simulated connection"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
