from django.db.models import Count, Avg, Max
from django.shortcuts import render, get_object_or_404
from crm.models import Author, Publisher, Book, Store


def index_crm(request):
    total_authors = Author.objects.aggregate(book_count=Count("book"))['book_count']
    average_price = Book.objects.aggregate(Avg('price'))['price__avg']
    # author = Author.objects.filter(age__gte=20, age__lte=30)
    return render(request, 'templates/index.html', {'total_authors': total_authors, 'average_price': average_price})


def get_all_authors(request):
    authors_all = Author.objects.all()
    # young_authors = Author.objects.annotate(Min("age")).filter(age__lte=16)
    return render(request, 'templates/authors_all.html', {'authors_all': authors_all})


def get_author_object(request, name):
    get_author = Author.objects.filter(book__authors__name=name)
    get_object_or_404(Author, name=name)
    get_author_books = Book.objects.filter(authors__name=name)
    return render(request, 'templates/author.html', {'get_author_books': get_author_books,
                                                         'get_author': get_author[0]})


def get_all_publishers(request):
    publishers_all = Publisher.objects.annotate(num_books=Count('book', distinct=True)).filter(book__rating__gt=8.5)
    return render(request, 'templates/publishers_all.html', {'publishers_all': publishers_all})


def get_publisher_object(request, pk):
    publisher_name = Publisher.objects.filter(name__exact=pk)
    count_publishers = Publisher.objects.prefetch_related().all().filter
    return render(request, 'templates/publisher.html', {'publisher_name': publisher_name,
                                                            'count_publishers': count_publishers})


def get_all_books(request):
    books_all = Book.objects.all()
    return render(request, 'templates/books_all.html', {'books_all': books_all})


def get_book_object(request, book_id):
    book = Book.objects.get(name=book_id)
    authors = book.authors.prefetch_related()
    return render(request, 'templates/book.html', {'authors': authors})


def get_all_stores(request):
    stores_all = Store.objects.order_by("name").prefetch_related()
    return render(request, 'templates/stores_all.html', {'stores_all': stores_all})


def get_store_object(request, pk):
    get_store = Store.objects.filter(name__exact=pk)
    books_price_avg = Store.objects.filter(books__store__name=pk).annotate(Max("books__price"))
    return render(request, 'templates/store.html', {'store': get_store,
                                                        'books_price_avg': books_price_avg[0].books__price__max})


def generate_celery_form(request):
    pass
    return render(request, 'templates/celery_form.html')


def error_404(request, exception):
    return render(request, 'templates/404.html')
