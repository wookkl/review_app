from django.db import models
from core.models import TimeStampedModel
from users import models as user_models
from movies import models as movie_models
from books import models as book_models


class FavList(TimeStampedModel):

    """ Fav Model Definition """

    created_by = models.OneToOneField(user_models.User, on_delete=models.CASCADE)
    books = models.ManyToManyField(book_models.Book, blank=True)
    movies = models.ManyToManyField(movie_models.Movie, blank=True)
