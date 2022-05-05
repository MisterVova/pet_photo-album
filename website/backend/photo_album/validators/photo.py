from django.db import DataError
from rest_framework.serializers import BaseSerializer


def qs_exists(queryset):
    try:
        return queryset.exists()
    except (TypeError, ValueError, DataError):
        return False


def qs_filter(queryset, **kwargs):
    try:
        return queryset.filter(**kwargs)
    except (TypeError, ValueError, DataError):
        return queryset.none()


class PhotoValidator:
    """
    Validator that corresponds to `unique=True` on a model field.

    Should be applied to an individual field on the serializer.
    """
    message = 'This field must be unique.'
    requires_context = True

    def __init__(self, queryset_album, queryset_photo, message=None, ):
        self.queryset_album = queryset_album
        self.queryset_photo = queryset_photo
        self.message = message or self.message
        # self.lookup = lookup

    def filter_queryset(self, value, queryset, serializer):
        """
        Filter the queryset to all instances matching the given attribute.
        """
        # # filter_kwargs = {'%s__%s' % (field_name, self.lookup): value}
        # # filter_kwargs = {'%s__%s' % (field_name, self.lookup): value}
        # field_name = ""
        # filter_kwargs = {'%s__%s' % (field_name, self.lookup): value}
        # return qs_filter(queryset, **filter_kwargs)

    # def filter_queryset(self, value, queryset, serializer):
    #     """
    #     Filter the queryset to all instances matching the given attribute.
    #     """
    #     # filter_kwargs = {'%s__%s' % (field_name, self.lookup): value}
    #     # filter_kwargs = {'%s__%s' % (field_name, self.lookup): value}
    #     field_name
    #     filter_kwargs = {'%s__%s' % (field_name, self.lookup): value}
    #     return qs_filter(queryset, **filter_kwargs)

    # def exclude_current_instance(self, queryset, instance):
    #     """
    #     If an instance is being updated, then do not include
    #     that instance itself as a uniqueness conflict.
    #     """
    #     if instance is not None:
    #         return queryset.exclude(pk=instance.pk)
    #     return queryset

    # def __call__(self, value, serializer_field):
    #     # Determine the underlying model field name. This may not be the
    #     # same as the serializer field name if `source=<>` is set.
    #     field_name = serializer_field.source_attrs[-1]
    #     # Determine the existing instance, if this is an update operation.
    #     instance = getattr(serializer_field.parent, 'instance', None)
    #
    #     queryset = self.queryset
    #     queryset = self.filter_queryset(value, queryset, field_name)
    #     # queryset = self.exclude_current_instance(queryset, instance)
    #     if qs_exists(queryset):
    #         raise ValidationError(self.message, code='unique')

    def __call__(self, attrs, serializer: BaseSerializer):
        pass
        # self.enforce_required_fields(attrs, serializer)
        # queryset = self.queryset
        # queryset = self.filter_queryset(attrs, queryset, serializer)
        # queryset = self.exclude_current_instance(attrs, queryset, serializer.instance)

        # queryset_album = self.queryset_album
        # print("serializer == ", serializer)
        # print("type(serializer)",type(serializer))
        # print(serializer.is_valid())
        # print("serializer..initial_data.get(user,)",serializer.initial_data.get("user",))
        # print("serializer..initial_data",serializer.initial_data)
        # print("serializer.validated_data.get(user,)",serializer.validated_data.get("user",))

        # from django.db.models import Q
        # filter_kwargs = Q(user__exact=serializer.get("user"))
        # queryset_album = qs_filter(queryset_album, **filter_kwargs)
        # print("queryset_album == ",queryset_album)
        #
        # # Ignore validation if any field is None
        # checked_values = [
        #     value for field, value in attrs.items() if field in self.fields
        # ]
        # if None not in checked_values and qs_exists(queryset):
        #     field_names = ', '.join(self.fields)
        #     message = self.message.format(field_names=field_names)
        #     # raise ValidationError(message, code='unique')
        #     raise ValidationError(message)
        # # qs_filter(queryset, **filter_kwargs)

    # def __repr__(self):
    #     return '<%s(queryset=%s)>' % (
    #         self.__class__.__name__,
    #         smart_repr(self.queryset)
    #     )
