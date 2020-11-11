from django.db import models
from core.models import TimeStampedModel
from users import models as user_models
from movies import models as movie_models
from books import models as book_models
from django.core.validators import MaxValueValidator, MinValueValidator


class Review(TimeStampedModel):

    """ Review Model Definition """

    created_by = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    movie = models.ForeignKey(
        movie_models.Movie, on_delete=models.CASCADE, null=True, blank=True
    )
    book = models.ForeignKey(
        book_models.Book, on_delete=models.CASCADE, null=True, blank=True
    )
    rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)], default=10
    )

    def __str__(self):
        return f"{self.text[:20]} - {self.created_by}"
