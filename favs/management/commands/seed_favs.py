import random
from django.core.management.base import BaseCommand
from favs.models import FavList
from users.models import User
from movies.models import Movie
from books.models import Book


class Command(BaseCommand):

    help = "This command creates favs"

    def handle(self, *args, **options):
        books = Book.objects.all()
        movies = Movie.objects.all()
        for user in User.objects.all():
            fav = FavList.objects.create(created_by=user)
            for m in movies:
                magic_number = random.randint(0, 10)
                if magic_number % 4 == 0:
                    fav.movies.add(m)
            for b in books:
                magic_number = random.randint(0, 10)
                if magic_number % 4 == 0:
                    fav.books.add(b)
        self.stdout.write(self.style.SUCCESS("Favorite lists created!"))
