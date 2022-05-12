from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse


class PhotoTestCase(APITestCase):
    # fixtures = [
    #     "backend/user/fixtures/init_fixtures.json",
    #      "backend/photo_album/fixtures/init_fixtures.json",
    # ]
    def setUp(self):
        self.register_url = reverse('user-list')
        self.login_url = reverse('login')
        self.album_list_url = reverse('album-list')
        self.photo_list_url = reverse('photo-list')
        self.tag_list_url = reverse('tag-list')

        self.user_01 = {
            'username': 'user_01',
            'email': 'user_01@mm.mm',
            'password': 'User_01_password',
            'first_name': "user_01",
            'last_name': "user_01",
        }

        self.user_02 = {
            'username': 'user_02',
            'email': 'user_02@mm.mm',
            'password': 'User_02_password',
            'first_name': "user_02_first_name",
            'last_name': "user_02_last_name",
        }
        # self._set_up_user()
        # self._set_up_tags()
        # self._set_up_album()

    def _set_up_tags(self):
        from photo_album.models import Tag

        self.tag_01 = Tag(name="TAG_01")
        self.tag_02 = Tag(name="TAG_02")
        self.tag_03 = Tag(name="TAG_03")
        self.tag_04 = Tag(name="TAG_04")
        self.tag_05 = Tag(name="TAG_05")
        self.tag_01.save()
        self.tag_02.save()
        self.tag_03.save()
        self.tag_04.save()
        self.tag_05.save()

        # print(
        #     self.tag_01.id,
        #     self.tag_02.id,
        #     self.tag_03.id,
        #     self.tag_04.id,
        #     sep="\n"
        # )

    def _set_up_user(self):
        # добавляем пользователей
        for user in [self.user_01, self.user_02]:
            self.client.post(self.register_url, user)
            data = {
                'username': user.get("username"),
                'password': user.get("password"),
            }
            user["auth_token"] = self.client.post(self.login_url, data).json()["auth_token"]
        # print(self.user_01, self.user_02, sep="\n")

    def _set_up_album(self):
        # добавляем пользователей
        for user in [self.user_01, self.user_02]:
            user["albums"] = {}
            self.client.credentials(HTTP_AUTHORIZATION='Token ' + user["auth_token"])
            # # Добавляю Альбомы для пользователей
            for nr in ["01", "02"]:
                new_data = {
                    "name": f"Album_{nr}_{user['username']}",
                }
                user["albums"][f"album_{nr}"] = self.client.post(self.album_list_url, new_data).json()

    def test_as_unauthorized(self):
        self._set_up_user()
        from django.test.client import Client
        client = Client()
        response = client.get(self.photo_list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_as_authorized(self):
        self._set_up_user()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_01["auth_token"])
        response = self.client.get(self.photo_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def _set_up_images(self):
        import os
        from app.basedir import BASE_DIR
        from photo_album.tests.fixtures.images.images import images
        self.images = images
        for image in self.images["bad"]:
            image["patch"] = (os.path.join(BASE_DIR, 'photo_album', 'tests', 'fixtures', 'images', image["patch"]))
        for image in self.images["ok"]:
            image["patch"] = (os.path.join(BASE_DIR, 'photo_album', 'tests', 'fixtures', 'images', image["patch"]))
        # print("self.images", self.images)

    def _add_photo_by_data(self, data):

        # print("_add_photo_by_data", data)
        # data_send = dict(data)
        # print("_add_photo_by_data", data_send)
        patch = data["image"]
        with open(patch, 'rb') as image:
            from django.core.files.uploadedfile import SimpleUploadedFile
            uploaded_image = SimpleUploadedFile(patch, image.read())
            data_send = dict(data)
            data_send['image'] = uploaded_image
            return self.client.post(self.photo_list_url, data_send)

    # def test_aa(self):
    #     self._set_up_images()

    def test_ok_photo_create(self):
        self._set_up_user()
        self._set_up_tags()
        self._set_up_album()
        self._set_up_images()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_01["auth_token"])
        data = {
            "name": self.images["ok"][0]["name"],
            "image": self.images["ok"][0]["patch"],
            "album": self.user_01["albums"]["album_01"]["id"],
            "tags": [self.tag_01.id, self.tag_02.id],
        }
        response = self._add_photo_by_data(data)
        # print("response.status_code", response.status_code)
        # print("response.data", response.data)
        # print("response.json()", response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # проверяем возможность добавить фото другому пользователь альбом

        data = {
            "name": self.images["ok"][0]["name"],
            "image": self.images["ok"][0]["patch"],
            "album": self.user_02["albums"]["album_01"]["id"],
            "tags": [self.tag_01.id, self.tag_02.id],
        }
        response = self._add_photo_by_data(data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # проверяем возможность добавить фото в несуществующий альбом
        data = {
            "name": self.images["ok"][0]["name"],
            "image": self.images["ok"][0]["patch"],
            "album": 999,
            "tags": [self.tag_01.id, self.tag_02.id],
        }
        response = self._add_photo_by_data(data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_bad_photo_create(self):
        self._set_up_user()
        self._set_up_tags()
        self._set_up_album()
        self._set_up_images()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_01["auth_token"])
        for i in range(len(self.images["bad"])):
            data = {
                "name": self.images["bad"][i]["name"],
                "image": self.images["bad"][i]["patch"],
                "album": self.user_01["albums"]["album_01"]["id"],
                "tags": [self.tag_01.id, self.tag_01.id],
            }
            response = self._add_photo_by_data(data)
            # print()
            # print(self.images["bad"][i]["name"])
            # print("response.status_code", response.status_code)
            # print("response.data", response.data)
            # print("response.json()", response.json())
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_count_photo(self):
        # mm = "test_manage_photo"
        # print(f"vvvvvvvvvvvvvvvvvvvv============{mm}============vvvvvvvvvvvvvvvvvvvv")
        self._set_up_user()
        self._set_up_tags()
        self._set_up_album()
        self._set_up_images()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_01["auth_token"])
        for image in self.images["ok"]:
            data = {
                "name": image["name"],
                "image": image["patch"],
                "album": self.user_01["albums"]["album_01"]["id"],
                "tags": [self.tag_01.id, self.tag_02.id],
            }
            response = self._add_photo_by_data(data)
            if response.status_code != status.HTTP_201_CREATED:
                print()
                print(image["name"])
                print("response.status_code", response.status_code)
                print("response.data", response.data)
                print("response.json()", response.json())
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Проверяем количество фотографий всего у пользователя
        response = self.client.get(self.photo_list_url)
        self.assertEqual(len(response.json()), len(self.images["ok"]))

        # Проверяем количество фотографий в альбоме
        response = self.client.get(self.album_list_url + f'{self.user_01["albums"]["album_01"]["id"]}/')
        # print("response.status_code", response.status_code)
        # print("response.data", response.data)
        # print("response.json()", response.json())
        self.assertEqual(response.json()["count"], len(self.images["ok"]))
        # print(f"^^^^^^^^^^^^^^^^^^^^============{mm}============^^^^^^^^^^^^^^^^^^^^")

    def test_filter_photo(self):
        # mm = "test_filter_photo"
        # print(f"vvvvvvvvvvvvvvvvvvvv============{mm}============vvvvvvvvvvvvvvvvvvvv")
        self._set_up_user()
        self._set_up_tags()
        self._set_up_album()
        self._set_up_images()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_01["auth_token"])
        #  добавляем фото в первый альбом
        i = 0
        for image in self.images["ok"]:
            i += 1
            data = {
                "name": image["name"],
                "image": image["patch"],
                "album": self.user_01["albums"]["album_01"]["id"],
                "tags": [self.tag_01.id, self.tag_02.id, self.tag_04.id if i % 2 == 0 else self.tag_05.id],
            }
            response = self._add_photo_by_data(data)
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        #  добавляем фото во второй альбом
        i = 0
        for image in self.images["ok"]:
            i += 1
            data = {
                "name": image["name"],
                "image": image["patch"],
                "album": self.user_01["albums"]["album_02"]["id"],
                "tags": [self.tag_01.id, self.tag_03.id, self.tag_04.id if i % 2 != 0 else self.tag_05.id],
            }
            response = self._add_photo_by_data(data)
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Проверяем количество фотографий всего у пользователя
        response = self.client.get(self.photo_list_url)
        self.assertEqual(len(response.json()), len(self.images["ok"]) * 2)

        # Проверяем количество фотографий в альбоме album_01
        response = self.client.get(self.album_list_url + f'{self.user_01["albums"]["album_01"]["id"]}/')
        self.assertEqual(response.json()["count"], len(self.images["ok"]))

        # Проверяем количество фотографий в альбоме album_02
        response = self.client.get(self.album_list_url + f'{self.user_01["albums"]["album_02"]["id"]}/')
        self.assertEqual(response.json()["count"], len(self.images["ok"]))

        # фильтрация по id альбома album_02
        url = self.photo_list_url + f"""?album_id={self.user_01["albums"]["album_02"]["id"]}"""
        response = self.client.get(url)
        self.assertEqual(len(response.json()), len(self.images["ok"]))

        # фильтрация по name альбома album_02
        url = self.photo_list_url + f"""?album_name={self.user_01["albums"]["album_02"]["name"]}"""
        response = self.client.get(url)
        self.assertEqual(len(response.json()), len(self.images["ok"]))

        # фильтрация по  id и name альбома album_02 и album_01
        url = self.photo_list_url + f"""?album_name={self.user_01["albums"]["album_02"]["name"]}&album_id={self.user_01["albums"]["album_01"]["id"]}"""
        response = self.client.get(url)
        self.assertEqual(len(response.json()), len(self.images["ok"]) * 2)

        # фильтрация по id тега
        url = self.photo_list_url + f"""?tag_id={self.tag_04.id}"""
        response = self.client.get(url)
        self.assertEqual(len(response.json()), len(self.images["ok"]))

        # фильтрация по name тега
        url = self.photo_list_url + f"""?tag_name={self.tag_05.name}"""
        response = self.client.get(url)
        self.assertEqual(len(response.json()), len(self.images["ok"]))

        # фильтрация по name и id тега
        url = self.photo_list_url + f"""?tag_name={self.tag_05.name}&tag_id={self.tag_04.id}"""
        response = self.client.get(url)
        self.assertEqual(len(response.json()), len(self.images["ok"]) * 2)

        # фильтрация по  id и name альбома album_02 и album_01  и тегу
        url = self.photo_list_url + f"""?album_name={self.user_01["albums"]["album_02"]["name"]}&album_id={self.user_01["albums"]["album_01"]["id"]}&tag_id={self.tag_04.id}"""
        response = self.client.get(url)
        self.assertEqual(len(response.json()), len(self.images["ok"]))

        # фильтрация по  id и name альбома album_02  и тегу
        url = self.photo_list_url + f"""?album_name={self.user_01["albums"]["album_02"]["name"]}&tag_id={self.tag_05.id}"""
        response = self.client.get(url)
        self.assertEqual(len(response.json()), len(self.images["ok"]) // 2)

        # print("response.status_code", response.status_code)
        # print("response.data", response.data)
        # print("response.json()", response.json())
        # print(f"^^^^^^^^^^^^^^^^^^^^============{mm}============^^^^^^^^^^^^^^^^^^^^")
