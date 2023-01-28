from django.contrib.auth.models import User, UserManager
from django.core.management.base import BaseCommand


class Command(BaseCommand):
	help = u'Delete user'

	def add_arguments(self, parser):
		parser.add_argument('user_id', nargs='+', type=int, help='Users ID')

# Builtin lookup https://docs.djangoproject.com/en/4.1/ref/models/lookups/

	def handle(self, *args, **kwargs):
		users_ids = kwargs['user_id']
		if User.objects.filter(id__in=users_ids, is_superuser=True):
			self.stdout.write(f"Can't delete superusers {users_ids}.")
		else:
			User.objects.filter(id__in=users_ids, is_superuser=False).delete()














		# users_ids = kwargs['user_id']
		# try:
		# 	for user in users_ids:
		# 		if User.objects.filter(pk=user, is_superuser=True).exists():
		# 			self.stdout.write(u'You can\'t delete superuser!')
		# 		else:
		# 			user = User.objects.get(pk=user).delete()
		# except User.DoesNotExist:
		# 	self.stdout.write(u'Does not exist!')
