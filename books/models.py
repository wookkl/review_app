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
    rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)], default=5
    )
    writer = models.ForeignKey(
        person_models.Person,
        on_delete=models.CASCADE,
    )
