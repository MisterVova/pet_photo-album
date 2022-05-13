from django.db.models import Q


class AlbumFilter:
    # def __init__(self, album_id=None, tags_id=None, album_name=None, tags_name=None, ordering=None):
    def __init__(self, **kwargs):
        self.ordering = kwargs.get("ordering")
        self.ordering = self.ordering if self.ordering else []

        # self.album_id = []
        # self.album_name = []
        # self.tag_id = []
        # self.tag_name = ["город", "дом"]
        # self.ordering = ["-name",  "-created_at", "album"]
        # self.ordering = ["-album", "created_at"]

    def __str__(self):
        return f"""
        orders       {self.ordering}
        get_q_filter {self.get_q_filter()}
        get_ordering {self.get_ordering()}
        """

    def get_q_filter(self) -> Q:
        """
        das
        """

        # q_list += [ Q(album_pk__in=min_value) for i in self.album_id]
        q = Q()
        # if len(self.album_id):
        #     q_album |= Q(album__id__in=self.album_id)
        # if len(self.album_name):
        #     q_album |= Q(album__name__in=self.album_name)
        #
        # q_tag = Q()
        # if len(self.tag_id):
        #     q_tag |= Q(tags__id__in=self.tag_id)
        # if len(self.tag_name):
        #     q_tag |= Q(tags__name__in=self.tag_name)
        #
        # q = q_tag & q_album
        return q

    def get_ordering(self, valid_fields=["count", "created_at"]) -> [str]:
        valid_fields += [f'-{i}' for i in valid_fields] + [f'+{i}' for i in valid_fields]
        ret_ordering = []
        for item in self.ordering:
            if item in valid_fields:
                if item[0] == "+":
                    item = item[1:]
                if item == "count": item = "count"
                if item == "-count": item = "-count"

                # if item == "count": item = "photos"
                # if item == "-count": item = "-photos"
                ret_ordering.append(item)
        return ret_ordering
