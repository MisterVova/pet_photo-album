from ..models.image_small import ImageSmall
from django.contrib import admin


@admin.register(ImageSmall)
class ImageSmallAdmin(admin.ModelAdmin):
    list_display = ["__str__", "image", "height", "width", "image_original", ]
