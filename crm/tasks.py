from celery import shared_task
from celery import Celery
from time import sleep
from django.core.mail import send_mail


@shared_task(name="send_feedback_email")
def send_feedback_email_task(name, email, subject, message):
    sleep(1)
    send_mail(
        subject,
        message,
        "support@example.com",
        [email],
        fail_silently=False,
    )