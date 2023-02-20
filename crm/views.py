from datetime import datetime, date
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from django.contrib import messages

options = Options()
# Show or hide browser
options.headless = True

# disable webrdiver-mode:
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options,
                          )
from django.db.models import Count, Avg, Max, Min
from django.shortcuts import render, get_object_or_404, redirect

from crm.models import Author, Publisher, Book, Store, Quotes
# from .forms import FeedbackForm, ScheduleEmailForm
from .tasks import send_feedback_email_task


def index_crm(request):
    total_authors = Author.objects.aggregate(book_count=Count("book"))['book_count']
    average_price = Book.objects.aggregate(Avg("price"))["price__avg"]
    average_pages = Book.objects.aggregate(Avg("pages"))["pages__avg"]
    author_max_age = Author.objects.aggregate(Max("age"))["age__max"]
    # author = Author.objects.filter(age__gte=20, age__lte=30)
    return render(request, 'templates/index.html', {'total_authors': total_authors,
                                                    'average_price': average_price,
                                                    'average_pages': average_pages,
                                                    'author_max_age': author_max_age})


def get_all_authors(request):
    authors_all = Author.objects.all()
    young_authors = Author.objects.annotate(Min("age")).filter(age__lte=16)
    return render(request, 'templates/author_list.html', {'authors_all': authors_all, 'young_authors': young_authors})


def get_author_object(request, name):
    get_author = Author.objects.filter(book__authors__name=name)
    get_object_or_404(Author, name=name)
    get_author_books = Book.objects.filter(authors__name=name).select_related("publisher").order_by("authors__age")
    return render(request, 'templates/author_detail.html', {'get_author_books': get_author_books,
                                                         'get_author': get_author[0]})


def get_all_publishers(request):
    publishers_all = Publisher.objects.annotate(num_books=Count('book', distinct=True)).filter(book__rating__gt=5)
    publisher_count = Publisher.objects.aggregate(publisher_count=Count("name"))['publisher_count']
    return render(request, 'templates/publisher_list.html', {'publishers_all': publishers_all,
                                                             'publisher_count': publisher_count})


def get_publisher_object(request, pk):
    publisher_name = Publisher.objects.filter(name__exact=pk)
    count_publishers = Publisher.objects.select_related("publisher").filter(name__contains=pk[0],
                                                                            name__endswith=pk[-1]).count()
    return render(request, 'templates/publisher_detail.html', {'publisher_name': publisher_name,
                                                            'count_publishers': count_publishers})


def get_all_books(request):
    books_all = Book.objects.order_by("name").prefetch_related()
    total_books = Book.objects.aggregate(book_count=Count("name"))['book_count']
    return render(request, 'templates/book_list.html', {'books_all': books_all, 'total_books': total_books})


def get_book_object(request, book_id):
    book = Book.objects.get(name=book_id)
    authors = book.authors.filter(age__gt=30).annotate(Max("age"))
    return render(request, 'templates/book_detail.html', {'authors': authors})


def get_all_stores(request):
    stores_all = Store.objects.order_by("name").prefetch_related()
    total_stores = Store.objects.aggregate(store_count=Count("name"))['store_count']
    return render(request, 'templates/store_list.html', {'stores_all': stores_all, 'total_stores': total_stores})


def get_store_object(request, pk):
    get_store = Store.objects.filter(name__exact=pk)
    books_price_avg = Store.objects.filter(books__store__name=pk).annotate(Max("books__price"))
    return render(request, 'templates/store_detail.html', {'store': get_store,
                                                        'books_price_avg': books_price_avg[0].books__price__max})


def schedule_email_view(request):
    if request.method == "POST":
        # get form data
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        remind_date_time = request.POST['remind']
        # convert date string to datetime object
        remind_date_time = datetime.strptime(remind_date_time, '%Y-%m-%dT%H:%M')
        # schedule email using Celery task
        if remind_date_time < datetime.now():
            messages.error(request, 'The email cannot be scheduled in the past')
            return render(request, 'templates/feedback.html')
        send_feedback_email_task.apply_async(kwargs=
                                                {"name": name, "email": email, "subject": subject, "message": message,
                                                 "remind_date_time": remind_date_time})

        # redirect to a page that shows the user that the email was scheduled
        return redirect('crm:success')
    return render(request, 'templates/feedback.html')


def send_success_email(request):
    return render(request, 'templates/success.html')


def error_404(request, exception):
    return render(request, 'templates/404.html')


def quote_scraper(request):
    quotes_bulk = []
    stop_pages = 11
    for n in (range(1, stop_pages)):
        driver.get("https://quotes.toscrape.com/page/" + str(n))
        # Obj with quotes
        all_quotes = driver.find_elements(by=By.CLASS_NAME, value='quote')

        for quote_element in all_quotes:
            author_name = quote_element.find_element(by=By.CLASS_NAME, value='author').text
            quote_text = quote_element.find_element(by=By.CLASS_NAME, value='text').text

            # Check if the author already exists in the database
            author = Author.objects.filter(name=author_name).first()
            if not author:
                # Create a new Author object
                author = Author.objects.create(name=author_name)
            if not Quotes.objects.filter(quote=quote_text).exists():
                quote = Quotes.objects.create(author_id=author.id, quote=quote_text)
                quotes_bulk.append(quote)
                if len(quotes_bulk) == 5:
                    Quotes.objects.bulk_create(quotes_bulk)
                    quotes_bulk.clear()
                else:
                    break

                # quote_obj = Quotes.objects.all(author_id=author.id, quote=quote_text)
                # # Bulk create the Quote objects:
                # Quotes.objects.bulk_create(quote_obj)
            return render(request, 'templates/quote_list.html', {'quotes_bulk': quotes_bulk})
