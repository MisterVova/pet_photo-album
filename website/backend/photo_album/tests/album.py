from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse


#
#
# # python3 manage.py test photo_album.tests --verbosity 2


class AlbumTestCase(APITestCase):

    def setUp(self):
        self.register_url = reverse('user-list')
        # print("register_url", self.register_url)
        self.login_url = reverse('login')
        # print("login_url", self.login_url)
        self.album_list_url = reverse('album-list')
        # print("album_list_url", self.album_list_url)

        self.user_01_test = {
            'username': 'user_01',
            'email': 'user_01@mm.mm',
            'password': 'User_01_password',
            'first_name': "user_01_first_name",
            'last_name': "user_01_last_name",
        }

        self.user_02_test = {
            'username': 'user_02',
            'email': 'user_02@mm.mm',
            'password': 'User_02_password',
            'first_name': "user_02_first_name",
            'last_name': "user_02_last_name",
        }

    def test_unauthorized(self):
        # mm = "test_unauthorized"
        # print(f"vvvvvvvvvvvvvvvvvvvv============{mm}============vvvvvvvvvvvvvvvvvvvv")
        # проверка на доступ к альбомам не авторизованного пользователя
        from django.test.client import Client
        client = Client()
        response = client.get(self.album_list_url)
        # print("response.status_code", response.status_code)
        # print("response.data", response.data)
        # print("response.json()", response.json())
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        # print(f"^^^^^^^^^^^^^^^^^^^^============{mm}============^^^^^^^^^^^^^^^^^^^^")

    def test_album(self):
        # mm = "test_add_album"
        # print(f"vvvvvvvvvvvvvvvvvvvv============{mm}============vvvvvvvvvvvvvvvvvvvv")
        # добавляем пользователя
        self.client.post(self.register_url, self.user_01_test)
        # получаю токен
        data = {
            'username': self.user_01_test.get("username"),
            'password': self.user_01_test.get("password"),
        }
        response = self.client.post(self.login_url, data)
        # print("response.status_code", response.status_code)
        # print("response.data", response.data)
        # print("response.json()", response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('auth_token', response.json())
        # print("auth_token", response.json()["auth_token"])
        self.user_01_test["auth_token"] = response.json()["auth_token"]

        # добавляю токен авторизации к запросу
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_01_test["auth_token"])

        # Доступен ли адрес
        response = self.client.get(self.album_list_url)
        # print("response.status_code", response.status_code)
        # print("response.data", response.data)
        # print("response.json()", response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # # Добавляю Альбом
        new_data = {
            "name": "Album_01_User_01",
        }
        response = self.client.post(self.album_list_url, new_data)
        # print("response.status_code", response.status_code)
        # print("response.data", response.data)
        # print("response.json()", response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        album_01 = response.json()
        # print("album_01", album_01)

        # Добавляем еще Альбомы
        album_02 = self.client.post(self.album_list_url, {"name": "Album_02_User_01", }).json()
        album_03 = self.client.post(self.album_list_url, {"name": "Album_03_User_01", }).json()
        # Проверяем список альбомов
        response = self.client.get(self.album_list_url)
        # print("response.status_code", response.status_code)
        # print("response.data", response.data)
        # print("response.json()", response.json())
        # self.assertEqual(response.json(), [album_01, album_02, album_03])
        self.assertEqual(len(response.json()), 3)

        # проверяем доступ к альбомам от имени первого пользователя
        response = self.client.get(self.album_list_url + f"{album_01['id']}/")
        self.assertEqual(response.json(), album_01)
        response = self.client.get(self.album_list_url + f"{album_02['id']}/")
        self.assertEqual(response.json(), album_02)
        response = self.client.get(self.album_list_url + f"{album_03['id']}/")
        self.assertEqual(response.json(), album_03)

        # добавляем второго пользователя
        self.client.post(self.register_url, self.user_02_test)
        # получаю токен
        data = {
            'username': self.user_02_test.get("username"),
            'password': self.user_02_test.get("password"),
        }
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('auth_token', response.json())
        self.user_02_test["auth_token"] = response.json()["auth_token"]
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_02_test["auth_token"])

        # Проверяем список альбомов второго пользователя
        response = self.client.get(self.album_list_url)
        self.assertEqual(len(response.json()), 0)

        # проверяем доступ к альбомам первого пользователя от имени второго пользователя
        response = self.client.get(self.album_list_url + f"{album_02['id']}/")
        # print("response.status_code", response.status_code)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertNotEqual(response.json(), album_02)
        response = self.client.get(self.album_list_url + f"{album_03['id']}/")
        # print("response.status_code", response.status_code)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertNotEqual(response.json(), album_03)

        # print(f"^^^^^^^^^^^^^^^^^^^^============{mm}============^^^^^^^^^^^^^^^^^^^^")
