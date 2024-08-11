from django.db import models


class ShortUrl(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=8, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

