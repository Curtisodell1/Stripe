import stripe
import json
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    print(request.data)
    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(port=4242)