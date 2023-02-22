from django.db import models
from django.utils.translation import gettext_lazy as _


class Author(models.Model):
    name = models.CharField(_("first name"), max_length=100)
    age = models.IntegerField(blank=True)
    password = models.CharField(max_length=100)
    date_of_birth = models.DateField(_("date of birth"), null=True, blank=True)
    date_of_death = models.DateField(_("date of death"), null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class AuthorProfile(models.Model):
    author = models.OneToOneField("Author", on_delete=models.CASCADE)
    about = models.TextField(_("about"), max_length=1000, help_text=_("Author bio"), null=True, blank=True)

    def __str__(self):
        return f"{self.author.name} {self.author.date_of_birth} Profile"


class Publisher(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.name}"


class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.FloatField()
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    pubdate = models.DateField()

    class Meta:
        ordering = ("name", "price", "rating")

    def __str__(self):
        return f"{self.name}, {self.publisher}"


class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return f"{self.name}"


class Quotes(models.Model):
    quote = models.CharField(max_length=500)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class Reminder(models.Model):
    email = models.EmailField()
    text = models.TextField()
    remind_at = models.DateTimeField()
    start_date = models.DateField()
    end_date = models.DateField()



