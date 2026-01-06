from django.db import models

class Content(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    content_name = models.CharField()
    rating = models.CharField()
    review = models.TextField()
    cover = models.ImageField(upload_to="content/", blank=True, null=True)

