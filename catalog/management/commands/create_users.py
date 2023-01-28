from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from faker import Faker

fake = Faker()


class Command(BaseCommand):
    help = u'Create random user'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, choices=range(1, 11), help=u'Number of users')

    def handle(self, *args, **kwargs):
        number_of_users = kwargs['total']
        try:
            User.objects.bulk_create
            ([User(
                username=fake.user_name(),
                email=fake.email(),
                password=make_password(password=fake.password(length=8)))
                for _ in range(number_of_users)]
            )
        finally:
            self.stdout.write(f"Successfully added {number_of_users} users.")
