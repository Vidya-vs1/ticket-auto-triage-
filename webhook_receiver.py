from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return "Webhook Receiver is Running ✅", 200

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Received webhook data:")
    print(data)
    return jsonify({"status": "success", "data": data}), 200

if __name__ == "__main__":
    app.run(port=5001)
