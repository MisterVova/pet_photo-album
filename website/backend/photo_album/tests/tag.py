from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse


class TagTestCase(APITestCase):

    def setUp(self):
        self.register_url = reverse('user-list')
        # print("register_url", self.register_url)
        self.login_url = reverse('login')
        # print("login_url", self.login_url)
        self.tag_list_url = reverse('tag-list')
        # print("tag_list_url", self.tag_list_url)

        self.user_01_test = {
            'username': 'user_01',
            'email': 'user_01@mm.mm',
            'password': 'User1Qwert',
            'first_name': "user_01",
            'last_name': "user_01",
        }

    def test_add_tag(self):
        # mm = "test_add_tag"
        # print(f"vvvvvvvvvvvvvvvvvvvv============{mm}============vvvvvvvvvvvvvvvvvvvv")
        # добавляем пользователя
        self.client.post(self.register_url, self.user_01_test)

        # делаем его админом
        from user.models import User
        user_01_test = User.objects.get(username=self.user_01_test.get("username"))
        user_01_test.is_superuser = True
        user_01_test.is_staff = True
        user_01_test.save()

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
        response = self.client.get(self.tag_list_url)
        # print("response.status_code", response.status_code)
        # print("response.data", response.data)
        # print("response.json()", response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Добавляю тег
        new_tag_data = {
            "name": "TEST_TAG",
        }
        response = self.client.post(self.tag_list_url, new_tag_data)
        # print("response.status_code", response.status_code)
        # print("response.data", response.data)
        # print("response.json()", response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # проверяю Добавлен ли тег
        response = self.client.get(self.tag_list_url)
        # print("response.status_code", response.status_code)
        # print("response.data", response.data)
        # print("response.json()", response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.json(), [{'id': 1, 'name': 'TEST_TAG'}])
        # self.assertEqual(response.data, [{'id': 1, 'name': 'TEST_TAG'}])

        # print(f"^^^^^^^^^^^^^^^^^^^^============{mm}============^^^^^^^^^^^^^^^^^^^^")
