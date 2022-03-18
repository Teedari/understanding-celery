from __future__ import absolute_import, unicode_literals



import os
from django.conf import settings
from celery import Celery
from celery.schedules import crontab
from app1.tasks import add

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TutCelery.settings')
 
app = Celery('TutCelery')
 
app.config_from_object('django.conf:settings', namespace='CELERY') 

app.autodiscover_tasks()



app.conf.beat_schedule = {
  'Summation':{
    'task': 'app1.tasks.add',
    'schedule': crontab(minute='*/2'),
    'args': (1,2)
  }
    
}


@app.task(bind=True)
def debug(self):
  print("Task start test")