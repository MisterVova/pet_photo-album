from django.db import models
from photo_albums.models.image import Image
from garpix_utils.file import get_file_path


class ImageSmall(Image):
    image_original = models.OneToOneField(Image, verbose_name="Оригинал изображение", on_delete=models.CASCADE, related_name="small", blank=False)

    def __str__(self):
        return f'ImageSmall: {self.image} | {self.width}x{self.height}'

    class Meta:
        verbose_name = "Миниатюра Изображения"
        verbose_name_plural = "Миниатюры Изображений"
        ordering = ("image", "image_original")
