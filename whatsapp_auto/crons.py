from django_cron import CronJobBase, Schedule
from twilio.rest import Client


from django.contrib.auth import settings

from components.models import Messages, Profile

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'whatsapp_auto.my_cron_job'

    def do(self):
        account_sid = settings.ACCOUNT_SID
        auth_token = settings.AUTH_TOKEN
        client = Client(account_sid, auth_token)
        
        # for qs in Messages.objects.filter(profil__user__username='MU150710'):

        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body='Testing 2',
            to='whatsapp:+6282277507924'
        )

        print(message.sid)
        # return message