import os
from twilio.rest import Client

account_sid = os.environ['TWILLIO_ACCOUNT_SID']
auth_token = os.environ['TWILLIO_AUTH_TOKEN']
my_number = os.environ['MY_NUMBER']


client = Client(account_sid, auth_token)

client.message.create(body='Just a test',
                      from_='whatsapp:+14155238886',
                      to='whatsapp:{}'.format(my_number))
