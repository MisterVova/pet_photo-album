from django.db import models

from photo_albums.validators.image import validate_image_content_type, validate_image_size, extensions
from user.models import User
from photo_albums.models.tag import Tag
from photo_albums.models.album import Album
from garpix_utils.file import get_file_path
# import photo_albums.validators as validator
# import photo_albums.validators as validator
from django.core.validators import FileExtensionValidator

validators_image = [
    FileExtensionValidator(allowed_extensions=extensions),
    validate_image_content_type,
    validate_image_size,
]
validators = validators_image


class Photo(models.Model):
    name = models.CharField(verbose_name="Название", max_length=254, unique=False)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True, )
    updated_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True, )
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, related_name='photos', null=False)
    album = models.ForeignKey(Album, verbose_name='Альбом', on_delete=models.CASCADE, related_name='photos', null=False)
    tags = models.ManyToManyField(Tag, verbose_name="Теги", related_name="photos", blank=True)

    image = models.ImageField(verbose_name="Изображение", blank=False, null=False, upload_to=get_file_path, )
    image_small = models.ImageField(verbose_name="миниатюра Изображения", blank=True, null=True, upload_to=get_file_path, )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"
        ordering = ("user", "album", "name")
        unique_together = ('name', 'album')

    def save(self, *args, **kwargs):
        # super().save(*args, **kwargs)
        # print("", self.image)
        if self.album.user != self.user:
            # if True:
            from rest_framework import serializers
            raise serializers.ValidationError("Не найден альбом")

        if self.image:
            self.make_miniature()
            # try:
            #     self.make_miniature()
            # except:
            #     print("make_miniature except")
            #     pass
        else:
            self.image_small = None

        super().save(*args, **kwargs)
        # self.save(*args, **kwargs)

    def make_miniature(self):
        # print("make_miniature Start")
        # self.image.
        image = self.image

        name_original = image.name
        path_original = image.path
        import os
        # print("name_original     ", name_original)
        file_path = get_file_path(path_original, name_original)
        # print("file_path     ", file_path)
        # root, ext = os.path.splitext(name_original)
        root, ext = os.path.splitext(file_path)
        # print("root, ext ", (root, ext))
        name_new = f"{root}_small{ext}"
        # path_new = path_original[0:-len(name_original)] + file_path + name_new
        path_new = path_original[0:-len(name_original)] + name_new

        # print("name_original", name_original)
        # print("name_new     ", name_new)
        # print("path_original", path_original)
        # print("path_new_head", path_original[0:-len(name_original)])
        # print("path_new     ", path_new)

        from PIL import Image as PIL_Image
        # img = PIL_Image.open(path_original)
        img = PIL_Image.open(image)
        img_small = img.copy()
        if img_small.height > 150 or img_small.width > 150:
            output_size = (150, 150)
            img_small.thumbnail(output_size)
        img_small.save(path_new)
        # img_s = PIL_Image.open(path_new)
        # print("img_s     ", img_s)
        from django.db.models.fields.files import ImageFieldFile
        # self.image_small = ImageFieldFile(instance=self.image_small, field=self.image_small, name=name_new)
        self.image_small = ImageFieldFile(instance=self.image_small, field=self.image_small, name=name_new)

        # print("self.image_small", self.image_small)
        # print("self.image_small.name", self.image_small.name)
        # print("self.image_small.path", self.image_small.path)

        # print("make_miniature Finish")
