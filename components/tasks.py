import datetime
from celery import shared_task, task

from twilio.rest import Client
from .models import Messages

@task
def sent_wa(*args):
    account_sid = 'AC1bdbb7deb6e2d46d96a86e2e6a8e43e0'
    auth_token = 'd675c6f0749d2f9be91b5f9ace1acbab'
    client = Client(account_sid, auth_token)
    # print(client)
    for qs in Messages.objects.filter(profil__user=args):
        b = datetime.date.today()
        if qs.timestamp and qs.timestamp.day == b.day:
            # print(qs.timestamp.day and qs.timestamp == datetime.date(day).today()
            pecan = qs.pesan
            message = client.messages.create(
                from_='whatsapp:+14155238886',
                body=pecan,
                to='whatsapp:+6282277507924'
            )

            print(message.sid, message.uri)
            return message