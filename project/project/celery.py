from __future__ import absolute_import, unicode_literals
import os
import sys
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

sys.path.append(os.path.abspath('project'))
# app = Celery('Fundoo')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
app = Celery('hello', broker="amqp://guest@localhost//")
app.conf.beat_schedule = {
    'test-task': {
        'task': 'tasks.email',
        'schedule': crontab(),
    },
}
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
