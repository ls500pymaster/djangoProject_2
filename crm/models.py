from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=300)
    age = models.IntegerField(null=True, blank=True)
    password = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class AuthorProfile(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    about = models.TextField(max_length=1000, help_text="Author bio")

    def __str__(self):
        return f"{self.author.name} {self.author.age} Profile"


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
    text = models.CharField(max_length=500, null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class Reminder(models.Model):
    email = models.EmailField()
    text = models.TextField()
    remind_at = models.DateTimeField()
    start_date = models.DateField()
    end_date = models.DateField()



