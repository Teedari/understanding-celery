import json
from venv import create
from django_celery_beat.models import PeriodicTask, IntervalSchedule


def lauchTask():
  name='John Doe'
  age=170
  sisters = ['Florida', 'Martha', 'Linda', 'Rita', 'Angelina']
  brothers = ['Godwin']
  parents = ['Efua', 'Francis']
  
  schedule, created = IntervalSchedule.objects.get_or_create(every=1, period=IntervalSchedule.MINUTES)
  
  if created:
    p = PeriodicTask.objects.create(
      interval=schedule,
      name='Family Tree',
      task='app1.tasks.family_task',
      kwargs=json.dumps({
        "name":name,
        "age":age,
        "sisters":sisters,
        "brothers":brothers,
        "parents":parents
      })
    )
    
def lauchTask():
  name='John Doe'
  age=170
  sisters = ['Florida', 'Martha', 'Linda', 'Rita', 'Angelina']
  brothers = ['Godwin']
  parents = ['Efua', 'Francis']
  
  schedule, created = IntervalSchedule.objects.get_or_create(every=1, period=IntervalSchedule.MINUTES)
  
  if created:
    p = PeriodicTask.objects.create(
      interval=schedule,
      name='Family Tree',
      task='app1.tasks.family_task',
      kwargs=json.dumps({
        "name":name,
        "age":age,
        "sisters":sisters,
        "brothers":brothers,
        "parents":parents
      })
    )
  