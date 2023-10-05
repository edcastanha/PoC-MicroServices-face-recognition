from django.conf import settings
from core.cadastros.models import Aluno
from core.loggingMe import logger
from celery import shared_task
from time import sleep


@shared_task()
def send_email():
    print('send_email chamado')
    

# python -m celery -A core worker -l info
# python -m celery -A core beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler