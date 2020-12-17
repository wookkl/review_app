# Standard Library

import random

# Django
from django.core.management.base import BaseCommand
from django_seed import Seed

# local Django
from books.models import Book
from people.models import Person
from categories.models import Category

# local File
import list_of_books


class Command(BaseCommand):

    help = "This command creates books"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, help="How many books you want to create"
        )

    def handle(self, *args, **options):
        number = int(options.get("number"))
        seeder = Seed.seeder()
        seeder.add_entity(
            Book,
            number,
            {
                "title": lambda x: random.choice(list_of_books.books),
                "year": lambda x: random.randint(1800, 2020),
                "cover_image": None,
                "writer": lambda x: random.choice(Person.objects.filter(kind="writer")),
                "category": lambda x: random.choice(
                    Category.objects.filter(kind="book")
                    | Category.objects.filter(kind="both")
                ),
            },
        )
        seeder.execute()

        self.stdout.write(self.style.SUCCESS("Books created!"))
