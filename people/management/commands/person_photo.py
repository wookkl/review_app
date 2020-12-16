from django.core.management.base import BaseCommand
from people.models import Person
import random


class Command(BaseCommand):

    help = "This command adds person's photo"

    def handle(self, *args, **options):
        for person in Person.objects.all():
            person.photo = f"person_photos/{random.randint(1, 20)}.jpeg"
            person.save()
        self.stdout.write(self.style.SUCCESS("Photo added!"))
