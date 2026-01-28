from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

last_command = "none"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send_command():
    global last_command
    last_command = request.json.get("command", "none")
    return jsonify({"status": "ok"})

@app.route("/get")
def get_command():
    global last_command
    cmd = last_command
    last_command = "none"
    return jsonify({"command": cmd})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
