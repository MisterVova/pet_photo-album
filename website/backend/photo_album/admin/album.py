from ..models.album import Album
from django.contrib import admin


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ["name", "pk", "user"]
