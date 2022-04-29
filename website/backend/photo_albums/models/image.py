from django.db import models
from garpix_utils.file import get_file_path
import photo_albums.validators as validator


# validators=validator.image
class Image(models.Model):
    image = models.ImageField(verbose_name="Изображение", blank=False, null=True, upload_to=get_file_path, )
    image_small = models.ImageField(verbose_name="Изображение_m", blank=True, null=True, upload_to=get_file_path, )
    height = models.PositiveSmallIntegerField(verbose_name="Высота", blank=True)
    width = models.PositiveSmallIntegerField(verbose_name="Ширина", blank=True)

    def __str__(self):
        return f'''{self.pk}|Image: {self.image} | {self.width}x{self.height} | {self.image.width}x{self.image.height} | {self.image.name}'''

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"
        ordering = ("image",)

    def need_miniature(self):
        height = self.image.height
        width = self.image.width
        return max(height, width) > 150

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            self.height = self.image.height
            self.width = self.image.width
        else:
            self.height = None
            self.width = None
        # try:
        #     print("Image.save=width", self.width)
        #     print("Image.save=height", self.height)
        #     print("Image.save=content_type", self.image.file.content_type)
        # except:
        #     pass

        if self.image:
            # self.make_miniature()
            try:
                self.make_miniature()
            except:
                print("make_miniature except")

        super().save(*args, **kwargs)

    def make_miniature(self):
        print("make_miniature Start")
        image = self.image

        name_original = image.name
        path_original = image.path
        import os
        root, ext = os.path.splitext(name_original)
        name_new = f"{root}_small{ext}"
        path_new = path_original[0:-len(name_original)] + name_new

        print("name_original", name_original)
        print("name_new     ", name_new)
        print("path_original", path_original)
        print("path_new_head", path_original[0:-len(name_original)])
        print("path_new     ", path_new)

        from PIL import Image as PIL_Image
        img = PIL_Image.open(path_original)
        img_small = img.copy()
        if img_small.height > 150 or img_small.width > 150:
            output_size = (150, 150)
            img_small.thumbnail(output_size)
        img_small.save(path_new)

        from django.db.models.fields.files import ImageFieldFile, FileField, ImageField
        self.image_small = ImageFieldFile(instance=self.image_small, field=self.image_small, name=name_new)

        print("self.image_small", self.image_small)
        print("self.image_small.name", self.image_small.name)
        print("self.image_small.path", self.image_small.path)
        print("make_miniature Finish")
