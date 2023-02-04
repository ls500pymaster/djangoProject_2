from django import forms
from .models import Book, Author


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('title', 'description', 'publisher',)


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'email', 'date_of_birth',)


class TriangleForm(forms.Form):
    cat_a = forms.IntegerField(min_value=1)
    cat_b = forms.IntegerField(min_value=1)
