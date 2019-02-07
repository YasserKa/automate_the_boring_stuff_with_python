import requests
from twilio.rest import Client


account_sid = 'ACxxxxxxxxxxxxxxxxx'
auth_token = 'xxxxxxxxxxxxxxxxxxxxxx'
client = Client(account_sid, auth_token)

raining = True
if (raining):
    message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+96181750315',
                     to='+96181750315'
                 )
