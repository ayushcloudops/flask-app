from flask import Flask, jsonify
import os
import socket
import redis

r = redis.Redis(
    host='redis-master.default.svc.cluster.local',
    port=6379,
    decode_responses=True
)

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        r.incr("counter")
        return f"Counter: {r.get('counter')}"
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
