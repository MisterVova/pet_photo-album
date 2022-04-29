from django.db import models

from user.models import User


class Album(models.Model):
    # name = models.CharField(verbose_name="Название", max_length=254, unique=True)
    name = models.CharField(verbose_name="Название", max_length=254, unique=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='albums', verbose_name='Пользователь', null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Альбом"
        verbose_name_plural = "Альбомы"
        ordering = ("user", "name",)
        unique_together = ('name', 'user')
