# Generated by Django 3.1 on 2022-05-04 17:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import garpix_utils.file.file_field


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photo_albums', '0004_auto_20220429_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='photo_albums.album', verbose_name='Альбом'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to=garpix_utils.file.file_field.get_file_path, verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='user.user', verbose_name='Пользователь'),
        ),
    ]
