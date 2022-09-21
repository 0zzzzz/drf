from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        User.objects.create_superuser(username='admin', password='admin')
        for user in range(10):
            User.objects.create_user(
                username=f'{user}_name',
                password=f'{user}',
                first_name=f'{user}_first',
                last_name=f'{user}_last',
                email=f'{user}@{user}.ru'
            )
