from django.db.models import Count, Q, Avg, Max, Min, Sum
from django.shortcuts import render, get_object_or_404
from crm.models import Author, Publisher, Book, Store


def crm_main(request):
    pass
    return render(request, 'crm/templates/crm.html')


def authors_all(request):
    authors_all = Author.objects.prefetch_related()
    young_authors = Author.objects.annotate(Min("age")).filter(age__lte=16)
    mylist = zip(authors_all, young_authors)
    context = {
        'mylist': mylist,
    }
    return render(request, 'crm/templates/authors_all.html', {'authors_all': authors_all, 'young_authors': young_authors})


def author_solo(request, pk):
    author_solo = Author.objects.filter(name__exact=pk)
    return render(request, 'crm/templates/author.html', {'author_solo': author_solo})


def publishers_all(request):
    publishers_all = Publisher.objects.annotate(num_books=Count('book', distinct=True)).filter(book__rating__gt=8.5)
    return render(request, 'crm/templates/publishers_all.html', {'publishers_all': publishers_all})


def publisher_solo(request, pk):
    publisher_solo_name = Publisher.objects.filter(name__exact=pk)
    count = Publisher.objects.prefetch_related().all().filter
    return render(request, 'crm/templates/publisher.html', {'publisher': publisher_solo_name, 'publisher_books': count})


def books_all(request):
    books_all = Book.objects.all().prefetch_related()
    return render(request, 'crm/templates/books_all.html', {'books_all': books_all})


def book_solo(request, book_id):
    book = Book.objects.get(name=book_id)
    authors = book.authors.prefetch_related()
    return render(request, 'crm/templates/book.html', {'authors': authors})


def stores_all(request):
    store_all = Store.objects.order_by("name").prefetch_related()
    return render(request, 'crm/templates/store_all.html', {'store_all': store_all})


def store_solo(request, pk):
    store_solo = Store.objects.filter(name__exact=pk)
    books_price_avg = Store.objects.filter(books__store__name=pk).annotate(Max("books__price"))
    return render(request, 'crm/templates/store.html', {'store_solo': store_solo, 'books_price_avg': books_price_avg[0].books__price__max})


def error_404(request, exception):
    return render(request, 'crm/templates/404.html')
