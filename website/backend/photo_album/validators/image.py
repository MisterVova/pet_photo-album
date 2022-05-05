from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator

extensions = [
    # 'pdf',
    'jpg',
    'jpeg',
    'png',
]


def validate_image_size(image_field_obj):
    # print('image_field_obj==', image_field_obj)
    # print('image_field_obj==', type(image_field_obj))
    # print('image_field_obj.file', type(image_field_obj.file))
    # print('validate_image_size==', image_field_obj.file)
    #
    # from PIL import Image as PIL_Image
    # # img = PIL_Image.open(path_original)
    # img = PIL_Image.open(image_field_obj.file)
    #
    # print('type(img)==', type(img))
    # print('img.size==', img.size)
    # print('img.size==', img. .size)

    # print(' image_field_obj.size==', image_field_obj.size)
    # print('validate_image_size==', image_field_obj.file.size)
    # try:
    # print('image_field_obj.size', image_field_obj.file.size)
    # print('content_type==', image_field_obj.file.content_type)
    # except:
    #     pass
    # file_size = image_field_obj.file.size
    file_size = image_field_obj.size
    # megabyte_limit = 0.5
    megabyte_limit = 5.0
    if file_size > megabyte_limit * 1024 * 1024:
        raise ValidationError("Max file size is %sMB" % str(megabyte_limit))


def validate_image_content_type(image_field_obj):
    # print('image_field_obj==', image_field_obj)
    allowed_types = [
        'image/jpeg',
        'image/png',
    ]
    # message = _(
    #     'MIME  тип  файла “%(content_type)s” не допускается. Разрешенные MIME  типы: %(allowed_types).'
    # )
    # message = f'MIME  тип  файла “{content_type}” не допускается. Разрешенные MIME  типы: %(allowed_types).'

    # code = 'invalid_MIME_type'
    # content_type = None
    # print('image_field_obj==', type(image_field_obj))
    # print('image_field_obj==', type(image_field_obj.file))

    # image_field_obj ==  class 'django.db.models.fields.files.ImageFieldFile'>
    # image_field_obj == class 'django.core.files.uploadedfile.InMemoryUploadedFile'>

    # image_field_obj == < class 'django.core.files.uploadedfile.InMemoryUploadedFile'>
    # image_field_obj == < class '_io.BytesIO'>
    file = image_field_obj
    from django.db.models.fields.files import ImageFieldFile
    if isinstance(file, ImageFieldFile):
        file = file.file
    content_type = file.content_type
    # print('content_type==', content_type, content_type in allowed_types)

    if not (content_type in allowed_types):
        raise ValidationError(
            # "не верный тип",
            f'MIME  тип  файла “{content_type}” не допускается. Разрешенные MIME  типы: {", ".join(allowed_types)}.',
            # code=code,
            # params={
            #     'content_type': content_type,
            #     # 'allowed_types': ', '.join(allowed_types),
            #     # 'allowed_types': f',gdfgsdf ',
            # }
        )


validators = [
    FileExtensionValidator(allowed_extensions=extensions),
    validate_image_content_type,
    validate_image_size,
    # validate_image_content_type,
]
