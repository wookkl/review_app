import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from reviews.models import Review
from users.models import User
from movies.models import Movie


class Command(BaseCommand):

    help = "This command creates movie reviews"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, help="How many movie reviews you want to create"
        )

    def handle(self, *args, **options):
        number = int(options.get("number"))
        seeder = Seed.seeder()
        seeder.add_entity(
            Review,
            number,
            {
                "created_by": lambda x: random.choice(User.objects.all()),
                "movie": lambda x: random.choice(Movie.objects.all()),
                "book": None,
                "rating": lambda x: random.randint(1, 10),
            },
        )
        seeder.execute()

        self.stdout.write(self.style.SUCCESS("Movie reviews created!"))
