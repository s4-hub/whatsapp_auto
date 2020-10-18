from flask import Flask
from flask_apscheduler import APScheduler
from twilio.rest import Client

import datetime

from .models import Messages

app = Flask(__name__)
scheduler = APScheduler()

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
            # return message


    # if __name__ == '__main__':
            scheduler.add_job(id='task1', func=sent_wa, trigger='interval', replace_existing=True ,seconds=5)
            scheduler.start()
    # app.run(host = 'localhost', port=8080)