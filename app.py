import os
from flask import Flask, request, redirect, render_template
import dotenv
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

dotenv.load_dotenv('.env')

app = Flask(__name__)

@app.route('/')
def index():
    click = 'click'
    """Return Homepage"""
    return render_template('home.html', click=click)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message
    if body == '1':
        resp.message("Confirmed")
    else:
        resp.message("Please type a valid response.")

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True, port=os.environ.get('PORT', 5000))
