from __future__ import absolute_import, unicode_literals

import datetime
import sys
import redis
import requests
import os
from celery import Celery
from celery.schedules import crontab

app = Celery('hello', broker="redis://127.0.0.1:6379/")
app.conf.beat_schedule = {
    'test-task': {
        'task': 'tasks.email',
        # 'schedule': datetime.timedelta(seconds=55),
    },
}


@app.task()
def email():
    requests.get(url="http://localhost:8778/api/celery",)
