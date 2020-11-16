import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from movies.models import Movie
from people.models import Person
from categories.models import Category
import list_of_movies


class Command(BaseCommand):

    help = "This command creates movies"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, help="How many movies you want to create"
        )

    def handle(self, *args, **options):
        number = int(options.get("number"))
        seeder = Seed.seeder()
        seeder.add_entity(
            Movie,
            number,
            {
                "title": lambda x: random.choice(list_of_movies.movies),
                "year": lambda x: random.randint(1900, 2020),
                "cover_image": None,
                "director": lambda x: random.choice(
                    Person.objects.filter(kind="director")
                ),
                "category": lambda x: random.choice(
                    Category.objects.filter(kind="movie")
                    | Category.objects.filter(kind="both")
                ),
            },
        )
        seeder.execute()
        created_movies = seeder.execute()
        created_clean = flatten(list(created_movies.values()))
        casts = Person.objects.filter(kind="actor")
        for pk in created_clean:
            movie = Movie.objects.get(pk=pk)
            for c in casts:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    movie.cast.add(c)

        self.stdout.write(self.style.SUCCESS("Movies created!"))
