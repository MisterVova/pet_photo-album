from ..models.photo import Photo
from django.contrib import admin


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ["name", "pk", "user", "album", ]
