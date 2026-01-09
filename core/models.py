from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator


class Content(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    content_name = models.CharField()
    rating = models.FloatField(validators=[MinValueValidator(0.0),
                                MaxValueValidator(10.0)])
    review = models.TextField(validators=
    [MinLengthValidator(50, message="review length minimum 50 chapters")])
    cover = models.ImageField(upload_to="content/", blank=True, null=True)

