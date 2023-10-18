import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MMORPG_board.settings')

app = Celery('MMORPG_board')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.timezone = 'Europe/Moscow'
app.autodiscover_tasks()
app.conf.beat_schedule = {
    'send_mail_monday_10am': {
        'task': 'board.tasks.send_mail_monday_10am',
        'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
    },
}
