import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject_2.settings')
app = Celery('djangoProject_2')

# 'CELERY' means all celery-related configuration keys should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


app.conf.beat_schedule = {
    # Scraper
    'quote-scraper-three-hours-daily': {
        # Task Name Specified in Decorator
        'task': 'quotes_scraper',
        # Schedule
        'schedule': crontab(minute="*/1"),
        # Function Arguments
        # 'args': ("Hello",)
    },
}


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')