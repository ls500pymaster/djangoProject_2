from django.db.models import Count, Q, Avg, Max, Min, Sum
from django.shortcuts import render, get_object_or_404
from crm.models import Author, Publisher, Book, Store


def crm_main(request):
    pass
    return render(request, 'crm/templates/crm.html')


def get_all_authors(request):
    authors_all = Author.objects.prefetch_related()
    young_authors = Author.objects.annotate(Min("age")).filter(age__lte=16)
    return render(request, 'crm/templates/authors_all.html', {'authors_all': authors_all, 'young_authors': young_authors})


def get_author_object(request, pk):
    get_author = Author.objects.filter(name__exact=pk)
    return render(request, 'crm/templates/author.html', {'get_author': get_author})


def get_all_publishers(request):
    publishers_all = Publisher.objects.annotate(num_books=Count('book', distinct=True)).filter(book__rating__gt=8.5)
    return render(request, 'crm/templates/publishers_all.html', {'publishers_all': publishers_all})


def get_publisher_object(request, pk):
    publisher_name = Publisher.objects.filter(name__exact=pk)
    count_publishers = Publisher.objects.prefetch_related().all().filter
    return render(request, 'crm/templates/publisher.html', {'publisher_name': publisher_name, 'count_publishers': count_publishers})


def get_all_books(request):
    books_all = Book.objects.all().prefetch_related()
    return render(request, 'crm/templates/books_all.html', {'books_all': books_all})


def get_book_object(request, book_id):
    book = Book.objects.get(name=book_id)
    authors = book.authors.prefetch_related()
    return render(request, 'crm/templates/book.html', {'authors': authors})


def get_all_stores(request):
    stores_all = Store.objects.order_by("name").prefetch_related()
    return render(request, 'crm/templates/stores_all.html', {'stores_all': stores_all})


def get_store_object(request, pk):
    store = Store.objects.filter(name__exact=pk)
    books_price_avg = Store.objects.filter(books__store__name=pk).annotate(Max("books__price"))
    return render(request, 'crm/templates/store.html', {'store': store,
                                                        'books_price_avg': books_price_avg[0].books__price__max})


def error_404(request, exception):
    return render(request, 'crm/templates/404.html')
