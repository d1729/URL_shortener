from django.contrib import admin

from shortner.models import ShortUrl


# Register your models here.
@admin.register(ShortUrl)
class ShortUrlAdmin(admin.ModelAdmin):
    pass
