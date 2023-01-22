from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from django.contrib.auth.hashers import make_password


class Command(BaseCommand):
    help = u'Create random user'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help=u'Number of users')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        if 0 < total <= 10:
            for i in range(total):
                User.objects.bulk_create([
                    User(
                        username=get_random_string(6),
                        email="",
                        password=make_password(password="112233"),
                        is_active=True,
                    )
                ])
        else:
            self.stdout.write(u'Number of users must be 0-10')
