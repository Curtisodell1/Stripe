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


#Notes:
    #By using flask,JSON,and response we are allowing for our server to receive data from an event
    #we can trigger a practice event in a real world this would likely be from some sort of renewal, or purchase, or maybe a transaction dispute. 
    # https://www.youtube.com/watch?v=QK31ioLTqGU&list=PLy1nL-pvL2M55YVn0mGoQ5r-39A1-ZypO&index=5
    # test using the stripe cli https://stripe.com/docs/stripe-cli

    #To run you just need to make sure you've downloaded flask, run a server on port=4242
    #Then run 'StripeTest % stripe listen --forward-to=localhost:4242/webhook' after loging into the stripe server
    #Once you send an event through you'll be notified by the post request and then receive the information executed from your hook.


