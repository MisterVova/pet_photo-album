from django.db import models
from django.http import HttpRequest

from user.models import User
from photo_album.models.tag import Tag
from photo_album.models.album import Album
from garpix_utils.file import get_file_path

from django.core.validators import FileExtensionValidator

extensions = [
    'jpg',
    'jpeg',
    'png',
]


def validate_image_size(image_field_obj):
    file_size = image_field_obj.size
    megabyte_limit = 5.0
    if file_size > megabyte_limit * 1024 * 1024:
        from django.core.exceptions import ValidationError
        raise ValidationError("Max file size is %sMB" % str(megabyte_limit))


def validate_image_content_type(image_field_obj):
    allowed_types = [
        'image/jpeg',
        'image/png',
    ]

    file = image_field_obj
    # print(type(file))

    from django.db.models.fields.files import ImageFieldFile
    from django.core.exceptions import ValidationError
    from django.core.files.uploadedfile import InMemoryUploadedFile

    if isinstance(file, ImageFieldFile):
        # print(type(file))
        # print(type(file.file))
        file = file.file

    if not isinstance(file, InMemoryUploadedFile):
        return

    try:
        content_type = file.content_type
    except Exception:
        raise ValidationError(f'Не удалось определить MIME тип файла. Разрешенные MIME  типы: {", ".join(allowed_types)}.', )

    if not (content_type in allowed_types):
        raise ValidationError(
            f'MIME  тип  файла “{content_type}” не допускается. Разрешенные MIME  типы: {", ".join(allowed_types)}.',
        )


class Photo(models.Model):
    name = models.CharField(verbose_name="Название", max_length=254, unique=False)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True, )
    updated_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True, )
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, related_name='photos', null=False)
    album = models.ForeignKey(Album, verbose_name='Альбом', on_delete=models.CASCADE, related_name='photos', null=False)
    tags = models.ManyToManyField(Tag, verbose_name="Теги", related_name="photos", blank=True)

    image = models.ImageField(verbose_name="Изображение", blank=False, null=False, upload_to=get_file_path, validators=[validate_image_size, validate_image_content_type, FileExtensionValidator(allowed_extensions=extensions), ])
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

        from_make_miniature = kwargs.pop("from_make_miniature", False)
        super().save(*args, **kwargs)
        if from_make_miniature:
            return

        if self.image:
            # self.make_miniature2(*args, **kwargs)
            try:
                self.make_miniature2()
            except Exception:
                from rest_framework import serializers
                serializers.ValidationError("Не удалось создать миниатюру")
                # print("make_miniature except")

        else:
            self.image_small = None

        # super().save(*args, **kwargs)

    #
    # def delete(self, using=None, keep_parents=False):
    #     super().delete(using=using, keep_parents=keep_parents)
    #     print("===================delete")

    def make_miniature(self):
        # print("make_miniature Start")
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

        file, ext = os.path.split(path_new)
        if not os.path.exists(file):
            os.makedirs(file)
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

    def make_miniature2(self, *args, **kwargs):
        # print("make_miniature Start")
        # if kwargs.get("save_from_make_miniature"):
        #     return
        image = self.image

        name_original = image.name
        path_original = image.path
        import os
        # print("name_original     ", name_original)
        # file_path = get_file_path(path_original, name_original)
        # print("file_path     ", file_path)
        root, ext = os.path.splitext(name_original)
        # root, ext = os.path.splitext(file_path)
        # print("root, ext ", (root, ext))
        name_new = f"{root}_small{ext}"
        # path_new = path_original[0:-len(name_original)] + file_path + name_new
        path_new = path_original[0:-len(name_original)] + name_new

        # print("name_original", name_original)
        # print("name_new     ", name_new)
        # print("path_original", path_original)
        # print("path_new_head", path_original[0:-len(name_original)])
        # print("path_new     ", path_new)
        # return
        from PIL import Image as PIL_Image
        # img = PIL_Image.open(path_original)
        img = PIL_Image.open(image)
        img_small = img.copy()
        if img_small.height > 150 or img_small.width > 150:
            output_size = (150, 150)
            img_small.thumbnail(output_size)

        file, ext = os.path.split(path_new)
        if not os.path.exists(file):
            os.makedirs(file)
        img_small.save(path_new)
        # img_s = PIL_Image.open(path_new)
        # print("img_s     ", img_s)
        from django.db.models.fields.files import ImageFieldFile
        self.image_small = ImageFieldFile(instance=self.image_small, field=self.image_small, name=name_new)
        self.save(from_make_miniature=True)
        # bb = Photo.objects.get(id=self.id)
        # # print(bb)
        #
        # bb.image_small = ImageFieldFile(instance=self.image_small, field=self.image_small, name=name_new)
        # bb.save(kwargs={"from_make_miniature":True})

        # self.image_small = ImageFieldFile(instance=self.image_small, field=self.image_small, name=name_new)
        # self.image_small.save()
        # print("self.image_small", self.image_small)
        # print("self.image_small.name", self.image_small.name)
        # print("self.image_small.path", self.image_small.path)

        # print("make_miniature Finish")

    @classmethod
    def get_queryset_by_request(cls, request: HttpRequest, user: User):
        # print("get_queryset_by_request")
        # print(request)
        # print(request.GET)

        from photo_album.serializers.photo import PhotoFilterSerializer
        p = PhotoFilterSerializer(data=request.GET)
        p.is_valid()
        # print(is_valid)
        # print(p.validated_data)

        from photo_album.filters.photo import PhotoFilter
        photo_filter = PhotoFilter(**p.validated_data)
        # print(photo_filter)
        # items = Photo.objects.all()
        # user = request.user
        return cls.objects.filter(user=user).filter(photo_filter.get_q_filter()).order_by(*photo_filter.get_ordering())
        # return cls.objects.filter(photo_filter.get_q_filter()) photo_filter.get_ordering()
