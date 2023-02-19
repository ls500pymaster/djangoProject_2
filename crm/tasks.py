from celery import shared_task
from celery import Celery
from django.db import transaction
from time import sleep
from django.core.mail import send_mail
from .models import Quotes, Author


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


@shared_task(name="quotes_scraper")
def add_quote_to_db(quote, author):
    sleep(1)
    with transaction.atomic():
        quote = Quotes.objects.create(quote=quote)
        author = Author.objects.create(name=author)
    return f"Added author {author} and quote {quote} to the database."
