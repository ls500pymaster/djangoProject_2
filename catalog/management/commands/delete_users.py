from django.contrib.auth.models import User, UserManager
from django.core.management.base import BaseCommand


class Command(BaseCommand):
	help = u'Delete user'

	def add_arguments(self, parser):
		parser.add_argument('user_id', nargs='+', type=int, help='User ID')

	def handle(self, *args, **kwargs):
		users_ids = kwargs['user_id']
		for user_id in users_ids:
			user = User.objects.get(pk=user_id, is_superuser=False)
			user.delete()
			self.stdout.write(u'User"%s (%s)" deleted!' % (user.username, user_id))
