from datetime import datetime
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from core.models import TimeStampedModel
from categories import models as category_models
from people import models as person_models


class Book(TimeStampedModel):

    """ Book Model Definition """

    title = models.CharField(max_length=40)
    year = models.PositiveIntegerField(
        validators=[MinValueValidator(1700), MaxValueValidator(datetime.now().year)],
        help_text="Use the following format: <YYYY>",
        default=1700,
    )
    category = models.ManyToManyField(category_models.Category)
    cover_image = models.ImageField(null=True, blank=True)
    writer = models.ForeignKey(
        person_models.Person,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.title} - {self.writer.name}"

    def rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        if len(all_reviews) > 0:
            for review in all_reviews:
                all_ratings += review.rating_average()
            return round(all_ratings / len(all_reviews), 1)
        return 0
