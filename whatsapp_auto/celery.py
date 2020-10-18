from __future__ import absolute_import, unicode_literals

import os
from celery import Celery

# from components.models import Messages, Profile

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'whatsapp_auto.settings')

app = Celery('whatsapp_auto')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {}'.format(self.request))

if __name__ == '__main__':
    app.start()