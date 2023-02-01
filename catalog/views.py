from django.shortcuts import redirect
from .models import Book
from django.shortcuts import render, get_object_or_404
from .forms import BookForm, TriangleForm
from django.utils import timezone
import math


def catalog(request):
    books = Book.objects.all()
    return render(request, 'catalog/catalog.html', {'books': books})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'catalog/book_detail.html', {'book': book})


def book_new(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publication_date = timezone.now()
            post.save()
            return redirect('book_detail', pk=post.pk)
    else:
        form = BookForm()
    return render(request, 'catalog/book_new.html', {'form': form})


def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('book_detail', pk=post.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'catalog/book_edit.html', {'form': form})


def triangle(request):
    if request.method == "POST":
        cat_a = request.POST.get("cat_a")
        cat_b = request.POST.get("cat_b")
        result = math.sqrt((int(cat_a) ** 2) + (int(cat_b) ** 2))
        return render(request, "catalog/triangle_result.html", {"result": result})
    else:
        triangle_form = TriangleForm()
        return render(request, "catalog/triangle.html", {"form": triangle_form})