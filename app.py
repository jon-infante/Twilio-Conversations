import os
from flask import Flask
from twilio.rest import Client
import dotenv

dotenv.load_dotenv('.env')


app = Flask(__name__)

account_sid = os.environ.get['TWILIO_ACCOUNT_SID']
auth_token = os.environ.get['TWILIO_AUTH_TOKEN']

client = Client(account_sid, auth_token)

conversation = client.conversations \
                     .conversations \
                     .create(friendly_name='My First Conversation')

print(conversation.sid)

@app.route("/")
def hello():
  return "Hello World!"

if __name__ == "__main__":
  app.run()