import os

from celery import Celery, shared_task
from celery.schedules import crontab
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('shop')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

@app.on_after_configure.connect
def setup_periodic_tasks(sender: Celery, **kwargs):
    sender.add_periodic_task(220.0, some_task_1.s(), name="3 minute 40 sec")

    sender.add_periodic_task(
        crontab(hour=[19,20,21], minute=0),
        some_task_2.s()
    )


@app.task(bind=True, ignore_result=True)
def some_task_1(self):
    return "3 minute 40 sec"

@app.task()
def some_task_2(self):
    return "19-21"


