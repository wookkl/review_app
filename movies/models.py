from datetime import datetime
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
from core.models import TimeStampedModel


class Movie(TimeStampedModel):

    """ Movie Model Definition """

    title = models.CharField(max_length=40)
    year = models.PositiveIntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(datetime.now().year)],
        help_text=_("Use the following format: <YYYY>"),
        default=1900,
    )
    cover_image = models.ImageField(null=True, blank=True, upload_to="movie_photos")
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.CASCADE,
        related_name="movies",
    )
    director = models.ForeignKey(
        "people.Person",
        on_delete=models.CASCADE,
        related_name="movies",
    )
    cast = models.ManyToManyField(
        "people.Person",
        related_name="casted_movies",
    )

    def __str__(self):
        return self.title

    def rating(self):
        try:
            all_reviews = self.reviews.all()
            all_ratings = 0
            if len(all_reviews) > 0:
                for review in all_reviews:
                    all_ratings += review.rating
                return round(all_ratings / len(all_reviews), 1)
            else:
                return 0
        except models.ObjectDoesNotExist:
            return 0

    def get_absolute_url(self):
        return reverse("movies:detail", kwargs={"pk": self.pk})
