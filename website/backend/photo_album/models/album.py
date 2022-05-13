from django.db import models
from django.http import HttpRequest
from django.utils.functional import cached_property
from user.models import User


class Album(models.Model):
    # name = models.CharField(verbose_name="Название", max_length=254, unique=True)
    name = models.CharField(verbose_name="Название", max_length=254, unique=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='albums', verbose_name='Пользователь', null=True)

    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='albums', verbose_name='Пользователь', null=True)
    # settings.AUTH_USER_MODEL
    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Альбом"
        verbose_name_plural = "Альбомы"
        ordering = ("user", "name",)
        unique_together = ('name', 'user')

    # @cached_property
    # def get_ph_count(self):
    #     print("self.photo.count",self.photo.count)
    #     return self.photo.count

    @classmethod
    def get_queryset_by_request(cls, request: HttpRequest, user: User):
        print("get_queryset_by_request")
        # print(request)
        # print(request.GET)

        from photo_album.serializers.album import AlbumFilterSerializer
        p = AlbumFilterSerializer(data=request.GET)
        p.is_valid()
        # print(is_valid)
        # print(p.validated_data)

        from photo_album.filters.album import AlbumFilter
        filter = AlbumFilter(**p.validated_data)
        # print(photo_filter)
        # items = Photo.objects.all()
        # user = request.user

        # return cls.objects.filter(user=user).filter(filter.get_q_filter()).order_by(*filter.get_ordering())
        from django.db.models import Count
        ret = cls.objects.filter(user=user).filter(filter.get_q_filter()).annotate(count=Count("photos")).order_by(*filter.get_ordering())
        # for r in ret:
        #     print(r.name, ": ", r.count, sep="")
        # print(ret)

        return ret
        # return cls.objects.filter(user=user).filter(filter.get_q_filter()).order_by("get_ph_count")
        # return cls.objects.filter(photo_filter.get_q_filter()) photo_filter.get_ordering()
