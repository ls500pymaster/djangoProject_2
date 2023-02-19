from django.shortcuts import redirect
from django.views import generic

from .models import Book, Author
from django.shortcuts import render, get_object_or_404
from .forms import BookForm, TriangleForm, AuthorForm
from django.utils import timezone
import math


class BookListView(generic.ListView):
    model = Book
    template_name = 'catalog/templates/catalog/book_list.html'  # Определение имени вашего шаблона и его расположения
    context_object_name = 'my_book_list'

    def get_queryset(self):
        return Book.objects.filter(title__icontains='py')[:5] # Получить 5 книг, содержащих 'war' в заголовке


class BookDetailView(generic.DetailView):
    template_name = 'catalog/templates/catalog/book_detail.html'  # Определение имени вашего шаблона и его расположения
    context_object_name = 'book_detail'
    model = Book


class AuthorDetailView(generic.DetailView):
    template_name = 'catalog/templates/catalog/author_detail.html'
    context_object_name = 'author_detal'
    model = Author


def author_detail(request, pk):
    author_detail = get_object_or_404(Author, pk=pk)
    return render(request, 'catalog/templates/catalog/author_detail.html', {'author': author_detail})


def author_edit(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == "POST":
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            author = form.save(commit=False)
            author.save()
            return redirect('author_detail', pk=author.pk)
    else:
        form = AuthorForm(instance=author)
    return render(request, 'catalog/templates/catalog/author_edit.html', {'form': form})


def catalog(request):
    books = Book.objects.all().count()
    authors = Author.objects.all().count()
    return render(request, 'catalog/templates/catalog/catalog.html', {'books': books, 'authors': authors})


# def book_detail(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     return render(request, 'catalog/templates/catalog/book_detail.html', {'book': book})


def book_new(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.author = request.user
            book.publication_date = timezone.now()
            book.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm()
    return render(request, 'catalog/templates/catalog/book_new.html', {'form': form})


def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.author = request.user
            book.published_date = timezone.now()
            book.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'catalog/templates/catalog/book_edit.html', {'form': form})


def triangle(request):
    form = TriangleForm(request.GET)
    if form.is_valid():
        form.result = math.hypot(form.cleaned_data['cat_a'], form.cleaned_data['cat_b'])
    return render(request, 'catalog/templates/catalog/triangle.html', {'form': form})


def error_404(request, exception):
    return render(request, 'catalog/templates/catalog/404.html')
