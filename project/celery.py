import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

# =================================================================
from django.conf import settings

app = Celery('messages', broker='pyamqp://guest@localhost//')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
