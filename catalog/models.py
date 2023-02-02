from django.db import models


class BookManager(models.Model):
    def title_count(self, keyword):
        return self.filter(title__icontains=keyword).count()


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    date_of_birth = models.DateField(verbose_name="Birthday", null=True)
    email = models.EmailField(verbose_name="Author email", null=True)

    def __str__(self):
        return self.first_name


class AuthorProfile(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    bio = models.TextField(verbose_name="Bio of author", max_length=255)

    def __str__(self):
        return self.author.first_name


class Genre(models.Model):
    genre_name = models.CharField(max_length=30, unique=True)


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField(unique=True)


class Book(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(verbose_name="About book", blank=True)
    authors = models.ManyToManyField(Author)
    genre = models.ManyToManyField(Genre)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField(verbose_name="Date the book was published")

    def __str__(self):
        return self.title
