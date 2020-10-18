from __future__ import absolute_import, unicode_literals

from celery import shared_task, task
from django.contrib.auth import settings
import datetime
import time

from twilio.rest import Client
from .models import Messages
# from .tw import sent_wa

# app = Celery('tasks', backend='amqp', broker='amqp://guest@localhost//')

# celery = Celery('whatsapp_auto', broker='amqp://guest@localhost//')

@task
def sent_wa(*args):
    account_sid = 'AC1bdbb7deb6e2d46d96a86e2e6a8e43e0'
    auth_token = 'd675c6f0749d2f9be91b5f9ace1acbab'
    client = Client(account_sid, auth_token)
    # print(client)
    for qs in Messages.objects.filter(profil__user=args):
        if qs.timestamp and qs.timestamp == datetime.datetime.today:
            pesan = qs.pesan
            message = client.messages.create(
                from_='whatsapp:+14155238886',
                body=pesan,
                to='whatsapp:+6282277507924'
            )

            print(message.sid, message.uri)
        
        # return message