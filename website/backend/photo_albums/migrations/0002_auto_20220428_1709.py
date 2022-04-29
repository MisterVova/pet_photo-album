# Generated by Django 3.1 on 2022-04-28 14:09

from django.conf import settings
from django.db import migrations, models
import garpix_utils.file.file_field


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photo_albums', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image_small',
            field=models.ImageField(blank=True, null=True, upload_to=garpix_utils.file.file_field.get_file_path, verbose_name='Изображение_m'),
        ),
        migrations.AlterField(
            model_name='image',
            name='height',
            field=models.PositiveSmallIntegerField(blank=True, verbose_name='Высота'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=garpix_utils.file.file_field.get_file_path, verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='image',
            name='width',
            field=models.PositiveSmallIntegerField(blank=True, verbose_name='Ширина'),
        ),
        migrations.AlterUniqueTogether(
            name='album',
            unique_together={('name', 'user')},
        ),
        migrations.AlterUniqueTogether(
            name='photo',
            unique_together={('name', 'album')},
        ),
    ]