from datetime import datetime
from django.db import models
from django.shortcuts import reverse
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
from core.models import TimeStampedModel


class Book(TimeStampedModel):

    """ Book Model Definition """

    title = models.CharField(max_length=40)
    year = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(datetime.now().year)],
        help_text=_("Use the following format: <YYYY>"),
        default=datetime.now().year,
    )
    cover_image = models.ImageField(null=True, blank=True, upload_to="book_photos")
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.CASCADE,
        related_name="books",
    )
    writer = models.ForeignKey(
        "people.Person",
        on_delete=models.CASCADE,
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
        except models.ObjectDoesNotExist:
            return 0

    def get_absolute_url(self):
        return reverse("books:detail", kwargs={"pk": self.pk})