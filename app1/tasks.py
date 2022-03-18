from __future__ import absolute_import
from time import sleep

from celery import shared_task

from django.core.mail import send_mail
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)





@shared_task
def add(x, y):
  return x + y


@shared_task
def send_email_task():
  sleep(10)
  send_mail('Subject', 'How are you doing?', None, ['how@gmail.com',])
  
  
@shared_task
def family_task(name:str, age:int, sisters:list, brothers:list, parent:list):
  logger.info(f'My name is {name} and i"m {age}. below are my sisters')
  
  for sis in sisters:
    logger.info(sis)
    
  logger.info('COMPLETED')
  return 1
  
