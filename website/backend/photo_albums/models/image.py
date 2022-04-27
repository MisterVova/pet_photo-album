from django.db import models
from garpix_utils.file import get_file_path


class Image(models.Model):
    image = models.ImageField(verbose_name="Изображение", blank=False, null=True, upload_to=get_file_path)
    height = models.PositiveSmallIntegerField(verbose_name="Высота")
    width = models.PositiveSmallIntegerField(verbose_name="Ширина")
    # image_small = models.OneToOneField(ImageSmall,verbose_name="Изображение миниатюры", on_delete=models.CASCADE, related_name="original", blank=False)

    def __str__(self):
        return f'Image: {self.image} | {self.width}x{self.height}'

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"
        ordering = ("image", )
