#created a twilio account
#installed the external module in python, and used the same

from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC71bc20dc5ba851ca493905396dada85d"
# Your Auth Token from twilio.com/console
auth_token  = "902ebe20e3121d85e6c03c7a129a2adc"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+14808233655",  #replace with your phone number
    from_="+12408835505", #replace with your twilio number
    body="Hello from Python!")

print(message.sid)
