from django import forms
from . import models


class CreateReviewForm(forms.ModelForm):

    """ Create Review Form Definition """

    rating = forms.IntegerField(min_value=0, max_value=10)
    text = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = models.Review
        fields = (
            "rating",
            "text",
        )

    def save(self):
        review = super().save(commit=False)
        return review
