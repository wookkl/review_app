# Standard Library
import random

# Django
from django.core.management.base import BaseCommand

# local Django
from categories.models import Category


class Command(BaseCommand):

    help = "This command creates categories"

    def handle(self, *args, **options):
        categories = [
            "Action",
            "Comedy",
            "Drama",
            "Fantasy",
            "Horror",
            "Mystery",
            "Romance",
            "Thriller",
            "Western",
            "Gangster",
            "Romance",
            "Adventure",
            "Musical",
        ]
        choices = [
            Category.KIND_BOOK,
            Category.KIND_MOVIE,
            Category.KIND_BOTH,
        ]
        for c in categories:
            Category.objects.create(name=c, kind=choices[random.randint(0, 2)])
        self.stdout.write(self.style.SUCCESS("Categories created!"))
