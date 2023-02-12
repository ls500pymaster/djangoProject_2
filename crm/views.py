from django.shortcuts import render, get_object_or_404
from crm.models import Author, Publisher, Book, Store


def crm_main(request):
    pass
    return render(request, 'crm/templates/crm.html')


def authors_all(request):
    authors_all = Author.objects.all()
    return render(request, 'crm/templates/authors_all.html', {'authors_all': authors_all})


def author_solo(request, pk):
    author_solo = Author.objects.filter(name__exact=pk)
    return render(request, 'crm/templates/author.html', {'author_solo': author_solo})


def publishers_all(request):
    publishers_all = Publisher.objects.all()
    return render(request, 'crm/templates/publishers_all.html', {'publishers_all': publishers_all})


def publisher_solo(request, pk):
    publisher_solo_name = Publisher.objects.filter(name__exact=pk)
    count = Publisher.objects.prefetch_related().all().filter
    return render(request, 'crm/templates/publisher.html', {'publisher': publisher_solo_name, 'publisher_books': count})


def books_all(request):
    books_all = Book.objects.prefetch_related().all
    return render(request, 'crm/templates/books_all.html', {'books_all': books_all})


def book_solo(request, book_id):
    # book_solo = Book.objects.filter(name__exact=pk)
    book = Book.objects.get(name=book_id)
    authors = book.authors.all()
    return render(request, 'crm/templates/book.html', {'authors': authors})


def stores_all(request):
    store_all = Store.objects.all()
    return render(request, 'crm/templates/store_all.html', {'store_all': store_all})


def store_solo(request, pk):
    store_solo = Store.objects.filter(name__exact=pk)
    return render(request, 'crm/templates/store.html', {'store_solo': store_solo})


def error_404(request, exception):
    return render(request, 'crm/templates/404.html')
