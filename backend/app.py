from flask import Flask, jsonify
import os
import socket
import redis

REDIS_HOST = os.getenv("REDIS_HOST", "redis-master")

r = redis.Redis(
    host=REDIS_HOST,
    port=6379,
    decode_responses=True,
    socket_connect_timeout=2,
    socket_timeout=2
)

app = Flask(__name__)

@app.route("/")
def home():
    try:
        count = r.incr("counter")
        return jsonify({"counter": count})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    })

@app.route("/health")
def health():
    try:
        r.ping()
        return "OK", 200
    except:
        return "Redis not reachable", 500
        
@app.route("/db")
def db():
    db_host = os.getenv("DB_HOST", "not-set")
    return jsonify({
        "db_host": db_host,
        "status": "simulated connection"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
