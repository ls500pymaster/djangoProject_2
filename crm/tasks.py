from time import sleep
from webdriver_auto_update import check_driver
from celery import shared_task
from django.core.mail import send_mail
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from .models import Author, Quotes

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
    send_mail(
        subject,
        message,
        "support@example.com",
        [email],
        fail_silently=False,
    )


# This task is running by celery.py.conf.beat_schedule
@shared_task(name="quotes_scraper")
def quote_scraper():
    page_number = 1
    max_quotes = 5
    counter = 0
    while counter < max_quotes:
        driver.get(f"https://quotes.toscrape.com/page/{page_number}/")
        for quote_element in driver.find_elements(by=By.CLASS_NAME, value='quote'):
            if counter >= max_quotes:
                break
            author_name = quote_element.find_element(by=By.CLASS_NAME, value='author').text
            text = quote_element.find_element(by=By.CLASS_NAME, value='text').text
            author, _ = Author.objects.get_or_create(name=author_name)
            quote, _ = Quotes.objects.get_or_create(text=text, author=author)
            counter += 1
            print(f"Added quote {counter}: {author_name} - {text}")
        page_number += 1
        if driver.find_elements(by=By.CSS_SELECTOR, value='li.next a'):
            driver.find_element(by=By.CSS_SELECTOR, value='li.next a').click()
        else:
            break
        sleep(1)
    driver.quit()
    send_mail(
        'Quote Scraper Done',
        f'The quote scraper has added {counter} quotes to the database',
        'sender@example.com',
        ['recipient@example.com'],
        fail_silently=False,
    )


