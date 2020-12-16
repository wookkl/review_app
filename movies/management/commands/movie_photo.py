from django.core.management.base import BaseCommand
from movies.models import Movie
import random


class Command(BaseCommand):

    help = "This command adds movie's photo"

    def handle(self, *args, **options):
        for movie in Movie.objects.all():
            movie.cover_image = f"movie_photos/{random.randint(1, 20)}.jpg"
            movie.save()
        self.stdout.write(self.style.SUCCESS("Photo added!"))
