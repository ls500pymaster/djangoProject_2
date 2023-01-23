from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from django.contrib.auth.hashers import make_password


class Command(BaseCommand):
    help = u'Create random user'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, choices=range(1, 11), help=u'Number of users')

    def handle(self, *args, **kwargs):
        number_of_users = kwargs['total']
        try:
            User.objects.bulk_create([User(username=get_random_string(6), email="", password=make_password(password="112233")
                                               , is_superuser=False, is_active=True) for _ in range(number_of_users)])
        finally:
            self.stdout.write(f"Succesfully added {number_of_users} users.")
