# Django
from django.core.management.base import BaseCommand
from django_seed import Seed

# local Django
from people.models import Person


class Command(BaseCommand):

    help = "This command creates people"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, help="How many people you want to create"
        )

    def handle(self, *args, **options):
        number = int(options.get("number"))
        seeder = Seed.seeder()
        seeder.add_entity(
            Person,
            number,
            {
                "name": lambda x: seeder.faker.name(),
                "photo": None,
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS("People created!"))
