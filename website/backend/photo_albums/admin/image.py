from ..models.image import Image
from django.contrib import admin


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ["__str__", "image", "height", "width"]
