from celery import shared_task
from celery import Celery
from time import sleep

from django.core.mail import send_mail

app = Celery('crm', broker='amqp://guest@localhost//', backend='redis://127.0.0.1:6379')

@shared_task()
def send_feedback_email_task(name, email, subject, message):
    sleep(1)  # Simulate expensive operation(s) that freeze Django
    send_mail(
        [name],
        [email],
        [subject],
        "support@example.com",
        [message],
    )