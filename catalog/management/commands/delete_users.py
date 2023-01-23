from django.contrib.auth.models import User, UserManager
from django.core.management.base import BaseCommand


class Command(BaseCommand):
	help = u'Delete user'

	def add_arguments(self, parser):
		parser.add_argument('user_id', nargs='+', type=int, help='User ID')

	def handle(self, *args, **kwargs):
		users_ids = kwargs['user_id']
		try:
			for user in users_ids:
				if User.objects.filter(pk=user, is_superuser=True).exists():
					self.stdout.write(u'You can\'t delete superuser!')
				else:
					user = User.objects.get(pk=user).delete()
		except User.DoesNotExist:
			self.stdout.write(u'Does not exist!')
