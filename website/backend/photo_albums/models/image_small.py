from django.db import models
from photo_albums.models.image import Image


class ImageSmall(Image):
    image_original = models.OneToOneField(Image, verbose_name="Оригинал изображение", on_delete=models.CASCADE, related_name="small", blank=False)

    def __str__(self):
        return f'ImageSmall: {self.image} | {self.width}x{self.height}'

    class Meta:
        verbose_name = "Миниатюра Изображения"
        verbose_name_plural = "Миниатюры Изображений"
        ordering = ("image", "image_original")

    #
    #
    #
    # def make_miniature(self):
    # # def save(self, *args, **kwargs):
    # #     super().save(*args, **kwargs)
    #     print("make_miniature Start")
    #     from PIL import Image as i_PIL_Image
    #     img = i_PIL_Image.open(self.image.path)
    #     if img.height > 150 or img.width > 150:
    #         output_size = (150, 150)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
    #
    #     print("make_miniature Finish")
    #
    #
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #
    #
    #     try:
    #         image = self.image_original.image
    #         from PIL import Image as PIL_Image
    #         img = PIL_Image.open(image.path)
    #         if img.height > 150 or img.width > 150:
    #             output_size = (150, 150)
    #             img.thumbnail(output_size)
    #             img.save(image.path)
    #
    #
    #
    #
    #         # self.make_miniature()
    #         # super().save(*args, **kwargs)
    #
    #         self.image = self.image_original.image
    #
    #         # self.height = self.image.height
    #         # self.width = self.image.width
    #
    #
    #
    #
    #         # print("Image.save=", self.file.content_type)
    #         # print("ImageSmall.save=width", self.width)
    #         # print("ImageSmall.save=height", self.height)
    #         # print("ImageSmall.save=content_type", self.image.file.content_type)
    #         # print("ImageSmall.save=need_miniature", self.need_miniature())
    #
    #         print("make_miniature Finish")
    #     except:
    #         pass
    #
    #
