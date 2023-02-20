from time import sleep

from celery import shared_task
from django.core.mail import send_mail
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
# Show or hide browser
options.headless = True
# disable webrdiver-mode:
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options,
                          )


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
def add_quote_to_db():
    # driver.get("https://quotes.toscrape.com")
    # # find all objects with quotes
    # all_quotes = driver.find_elements(by=By.CLASS_NAME, value='quote')
    # for quote_element in all_quotes:
    #     author_name = quote_element.find_element(by=By.CLASS_NAME, value='author').text
    #     quote_text = quote_element.find_element(by=By.CLASS_NAME, value='text').text
    #
    #     # Check if the author already exists in the database
    #     author = Author.objects.filter(name=author_name).first()
    #     if not author:
    #         # Create a new Author object
    #         author = Author.objects.create(name=author_name)
    #
    #     # Check if the quote already exists in the database
    #     if not Quotes.objects.filter(author=author, quote=quote_text).exists():
    #         # If the quote doesn't exist, create a new Quotes object and save it to the database
    #         quote = Quotes.objects.create(author=author, quote=quote_text)
    #         quote.save()
    return print("Task done. Check db.")