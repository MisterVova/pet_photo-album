from django.db import models


class Tag(models.Model):
    name = models.CharField(verbose_name="имя тега", max_length=254, unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
        ordering = ("name",)

    # def get_serializer(self):
    #     from ..serializers import HomePageSerializer
    #     return HomePageSerializer

    # def get_context(self, request: HttpRequest = None, *args, **kwargs):
    #     print ("Tag get_context request.method=",request.method)
    #     # context = super().get_context(request, *args, **kwargs)
    #     context = {}
    #     message=""
    #     if request.method == "POST":
    #
    #         pass
    #     if request.method == "POST":
    #         pass
    #
    #     if request.method == "POST":
    #         pass
    #
    #
    #     # print(request.get_raw_uri())
    #     other = {
    #         # "other": Tag.objects.values()
    #         "response": {
    #             # # "test": f"test {self.heading}",
    #             # "form_hotel_booking": form,
    #             # # "csrf_token_html" : csrf_token_html,
    #             # "csrf_token": csrf_token,
    #             # 'message': message,
    #             # "form_hotel_booking_data": form.data,
    #         }
    #     }
    #     # global_c = context.get("global")
    #     # print("global_c==", type(global_c), global_c)
    #
    #     context.update(other)
    #     return context
