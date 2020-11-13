from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from core.models import TimeStampedModel


class Review(TimeStampedModel):

    """ Review Model Definition """

    created_by = models.ForeignKey("users.User", on_delete=models.CASCADE)
    text = models.TextField()
    movie = models.ForeignKey(
        "movies.Movie",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="reviews",
    )
    book = models.ForeignKey(
        "books.Book",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="reviews",
    )
    rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)], default=10
    )

    def __str__(self):
        return f"{self.text[:20]}..."
