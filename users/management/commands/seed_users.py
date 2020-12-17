# Standard Library
import random

# Django
from django.core.management.base import BaseCommand
from django_seed import Seed

# local Django
from users.models import User
from categories.models import Category


class Command(BaseCommand):

    help = "This command creates users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, help="How many users you want to create"
        )

    def handle(self, *args, **options):
        number = int(options.get("number"))
        seeder = Seed.seeder()
        seeder.add_entity(
            User,
            number,
            {
                "is_staff": False,
                "is_superuser": False,
                "fav_book_genre": random.choice(
                    Category.objects.filter(kind="book")
                    | Category.objects.filter(kind="both")
                ),
                "fav_movie_genre": random.choice(
                    Category.objects.filter(kind="movie")
                    | Category.objects.filter(kind="both")
                ),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS("Users created!"))
