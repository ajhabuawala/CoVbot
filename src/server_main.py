from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

help_messages = ['help', 'help me',  'what can you do', 'what can you do ?']

@app.route("/sms", methods=['POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None).lower()

    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message
    if body in help_messages:
        send_help_message(resp)
    elif body == 'bye':
        resp.message("Goodbye")

    return str(resp)


def send_help_message(resp):
    return resp.message('''Í can do the following:
                        1) Tell me something nice right now 
                        2) Tell me a joke
                        3) Suggest a quarantine activity 
                        4) Suggest a quarantine workout''')
if __name__ == "__main__":
    app.run(debug=True)
