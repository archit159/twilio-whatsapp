from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import os,json


app = Flask(__name__)

with open(os.path.dirname(__file__) + './config.json') as cfg_file:
    Config = json.load(cfg_file)

client = Client(Config['twilio']['account_sid'], Config['twilio']['auth_token'])

@app.route("/test", methods=['GET', 'POST'])
def test():
    message = client.messages.create(
                              body='Hello there!',
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+918004104849'
                          )
    return("Return Status: True\n Message Body:{0}".format(message.body))

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=9999)
