#python package to send text messages: twilio, not available in python standard library. Has to be downloaded externally.
#example: validatio texts from gmail/other websites, texting without having phone number etc.
#created a twilio account

#from twilio.rest import Client - the original code calls the class Client fro the rest folder of __init__.py
#we replace this with the following line
from twilio import rest #inside code twilio, ther's another folder called rest, we call that forlder.

# Your Account SID from twilio.com/console
account_sid = "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
# Your Auth Token from twilio.com/console
auth_token  = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

#client = Client(account_sid, auth_token)  - access the class acc to old code
client = rest.Client(account_sid, auth_token)

message = client.messages.create(
    to="+1480xxxxxxx",  #replace with your phone number
    from_="+1240xxxxxxx", #replace with your twilio number
    body="Hello from Python!")

print(message.sid)
