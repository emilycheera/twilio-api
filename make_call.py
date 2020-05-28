import os
from twilio.rest import Client


account_sid = os.environ["ACCOUNT_SID"]
auth_token = os.environ["AUTH_TOKEN"]
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to=os.environ["TO_NUM"],
                        from_=os.environ["FROM_NUM"]
                    )

print(call.sid)
