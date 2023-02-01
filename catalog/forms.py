from django import forms
from .models import Book


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('title', 'description', 'publisher',)


class TriangleForm(forms.Form):
    cat_a = forms.IntegerField()
    cat_b = forms.IntegerField()
