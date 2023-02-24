from datetime import datetime, timedelta

from django.contrib import messages
from django.urls import reverse_lazy
from selenium.webdriver.chrome.options import Options
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from crm.models import Author, Book, Publisher, Store
from django.db.models import Count, Avg, Max
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect

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


class AuthorListView(generic.ListView):
    model = Author
    context_object_name = 'author_list'
    paginate_by = 20
    template_name = "templates/author_list.html"


class AuthorDetailView(generic.DetailView):
    model = Author
    context_object_name = 'author_detail'
    template_name = "templates/author_detail.html"


class AuthorCreate(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    model = Author
    fields = ["name", "age"]
    template_name = "templates/author_form.html"
    permission_required = "catalog.can_mark_returned"
    success_url = reverse_lazy("crm:author_list")


class AuthorUpdate(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    model = Author
    fields = ["name", "age"]
    template_name = "templates/author_form.html"
    permission_required = "catalog.can_mark_returned"
    success_url = reverse_lazy("crm:author_list")


class AuthorDelete(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = Author
    template_name = "templates/author_confirm_delete.html"
    permission_required = "catalog.can_mark_returned"
    success_url = reverse_lazy("crm:author_list")


class PublisherListView(generic.ListView):
    model = Publisher
    context_object_name = 'publisher_list'
    paginate_by = 5
    template_name = "templates/publisher_list.html"


class PublisherDetailView(generic.DetailView):
    model = Publisher
    context_object_name = "publisher_detail"
    paginate_by = 5
    template_name = "templates/publisher_detail.html"


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
        if remind_date_time - datetime.now() > timedelta(days=2):
            send_feedback_email_task.apply_async(kwargs=
                                                 {"name": name,
                                                  "email": email,
                                                  "subject": subject,
                                                  "message": message}, eta=remind_date_time)
            # redirect to a page that shows the user that the email was scheduled
            return redirect('crm:success')
        else:
            messages.info(request, 'Time must be 2 days ahead.')

    return render(request, 'templates/feedback.html')


def feedback_error(request):
    return render(request, 'templates/feedback_error.html')


def send_success_email(request):
    return render(request, 'templates/success.html')


def error_404(request, exception):
    return render(request, 'templates/404.html')


# def get_all_authors(request):
#     authors_all = Author.objects.all()
#     young_authors = Author.objects.annotate(Min("age")).filter(age__lte=16)
#     return render(request, 'templates/author_list.html', {'authors_all': authors_all, 'young_authors': young_authors})


# def get_author_object(request, name):
#     get_author = Author.objects.filter(book__authors__name=name)
#     get_object_or_404(Author, name=name)
#     get_author_books = Book.objects.filter(authors__name=name).select_related("publisher").order_by("authors__age")
#     return render(request, 'templates/author_detail.html', {'get_author_books': get_author_books,
#                                                          'get_author': get_author[0]})


# def get_all_publishers(request):
#     publishers_all = Publisher.objects.annotate(num_books=Count('book', distinct=True)).filter(book__rating__gt=5)
#     publisher_count = Publisher.objects.aggregate(publisher_count=Count("name"))['publisher_count']
#     return render(request, 'templates/publisher_list.html', {'publishers_all': publishers_all,
#                                                              'publisher_count': publisher_count})


# def get_publisher_object(request, pk):
#     publisher_name = Publisher.objects.filter(name__exact=pk)
#     count_publishers = Publisher.objects.select_related("publisher").filter(name__contains=pk[0],
#                                                                             name__endswith=pk[-1]).count()
#     return render(request, 'templates/publisher_detail.html', {'publisher_name': publisher_name,
#                                                             'count_publishers': count_publishers})

