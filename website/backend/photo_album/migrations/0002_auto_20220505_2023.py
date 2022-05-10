# Generated by Django 3.1 on 2022-05-05 17:23

from django.db import migrations, models
import garpix_utils.file.file_field
import photo_album.models.photo


class Migration(migrations.Migration):

    dependencies = [
        ('photo_album', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to=garpix_utils.file.file_field.get_file_path, validators=[photo_album.models.photo.validate_image_size], verbose_name='Изображение'),
        ),
    ]