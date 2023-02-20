from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=300)
    age = models.IntegerField(null=True, blank=True)
    password = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


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
    quote = models.CharField(max_length=500, null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class Reminder(models.Model):
    email = models.EmailField()
    text = models.TextField()
    remind_at = models.DateTimeField()
    start_date = models.DateField()
    end_date = models.DateField()



