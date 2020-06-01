from twilio.rest import Client
import os

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
to_num = os.environ.get("TO_NUM")
messaging_service_sid = os.environ.get("MESS_SERV_SID")

client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body="Join Earth's mightiest heroes. Like Kevin Bacon.",
         messaging_service_sid=messaging_service_sid,
         to=to_num
     )

print(message.sid)