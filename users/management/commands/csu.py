import json

from django.core.management import BaseCommand

from users.models import User


with open('prvt.json') as file:
    superuser_pass = json.load(file)['superuser_pass']


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='zhorikzeniuk@gmail.com',
            first_name='zhorik',
            last_name='zeniuk',
            is_staff=True,
            is_superuser=True
        )
        user.set_password(superuser_pass)
        user.save()
