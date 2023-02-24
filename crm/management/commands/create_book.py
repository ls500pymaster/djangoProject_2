import random
from crm.models import Book, Author, Publisher, Store
from django.core.management.base import BaseCommand
from faker import Faker

fake = Faker()


class Command(BaseCommand):
    help = u'Create random authors, books, publishers'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, choices=range(2, 5000), help=u'Number of users')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        publishers = [Publisher.objects.create(name=fake.company()) for i in range(total // 2)]
        for i in range(total):
            author = Author.objects.create(
                name=fake.name(),
                age=fake.random.randint(15, 80),
                password=fake.password()
            )
            book = Book.objects.create(
                name=fake.sentence(nb_words=3),
                pages=fake.random.randint(200, 1000),
                price=fake.random.uniform(100, 1000),
                rating=fake.random.randrange(0, 10),
                publisher=random.choice(publishers),
                pubdate=fake.date_this_decade()
            )
            book.authors.add(author)
            store = Store.objects.create(
                name=fake.company(),
            )
            store.books.add(book)
        self.stdout.write(self.style.SUCCESS(f'Successfully created {total} objects'))
