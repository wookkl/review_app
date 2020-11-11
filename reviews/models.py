from django.db import models
from core.models import TimeStampedModel
from users import models as user_models
from movies import models as movie_models
from books import models as book_models


class Review(TimeStampedModel):

    """ Review Model Definition """

    """
        Here are the models you have to create:
        - Review
        created_by (ForeignKey => users.User)
        text
        movie (ForeignKey => movies.Movie, null,blank)
        book (ForeignKey => movies.Movie, null,blank)
        rating
    ="""
    created_by = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    text = models.TextField()
    movie = models.ForeignKey(
        movie_models.Movie, on_delete=models.CASCADE, null=True, blank=True
    )
    book = models.ForeignKey(
        book_models.Book, on_delete=models.CASCADE, null=True, blank=True
    )
