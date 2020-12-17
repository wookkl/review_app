# Standard Library
import random

# Django
from django.core.management.base import BaseCommand
from django_seed import Seed

# local Django
from reviews.models import Review
from users.models import User
from books.models import Book


class Command(BaseCommand):

    help = "This command creates book reviews"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, help="How many book reviews you want to create"
        )

    def handle(self, *args, **options):
        number = int(options.get("number"))
        seeder = Seed.seeder()
        seeder.add_entity(
            Review,
            number,
            {
                "created_by": lambda x: random.choice(User.objects.all()),
                "book": lambda x: random.choice(Book.objects.all()),
                "movie": None,
                "rating": lambda x: random.randint(1, 10),
            },
        )
        seeder.execute()

        self.stdout.write(self.style.SUCCESS("Book reviews created!"))
