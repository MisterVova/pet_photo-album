from django.db import models
from user.models import User
from photo_albums.models.tag import Tag
from photo_albums.models.album import Album
from photo_albums.models.image import Image


class Photo(models.Model):
    name = models.CharField(verbose_name="Название", max_length=254, unique=False)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True, )
    updated_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True, )
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, related_name='photos', null=True)
    album = models.ForeignKey(Album, verbose_name='Альбом', on_delete=models.CASCADE, related_name='photos', null=True)
    tags = models.ManyToManyField(Tag, verbose_name="Теги", related_name="photos",blank=True)

    image = models.OneToOneField(Image, verbose_name="Изображение", on_delete=models.CASCADE, related_name="photos", blank=False)


    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"
        ordering = ("user", "album", "name")
        unique_together = ('name', 'album')
