from django.contrib.auth.models import User
from crm.models import Author
from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from faker import Faker

fake = Faker()


class Command(BaseCommand):
    help = u'Create random author'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, choices=range(1, 500), help=u'Number of users')

    def handle(self, *args, **kwargs):
        number_of_users = kwargs['total']
        Author.objects.bulk_create(
            [
                Author(
                    name=fake.name(), age=fake.random_int(18, 50)
                ) for _ in range(number_of_users)
            ]
        )
        self.stdout.write(f"Successfully added {number_of_users} authors.")
