from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse


class UserTestCase(APITestCase):

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

    def test_registration(self):
        """
        Регистрация пользователя
        """
        # pass
        response = self.client.post(self.register_url, self.user_01_test)
        # print("response.status_code", response.status_code)
        # print("response.data", response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_data = {'username': 'user_01', 'email': 'user_01@mm.mm', 'first_name': 'user_01', 'last_name': 'user_01'}
        self.assertEqual(response.data, response_data)
        # self.assertEqual(response.data, self.user_01)
        from user.models import User
        user_01_test = User.objects.get(username=self.user_01_test.get("username"))
        self.assertIsNotNone(user_01_test)
        print(user_01_test.pk)

    def test_auth_token(self):
        """
        Получения Токена Авторизации
        """
        self.client.post(self.register_url, self.user_01_test)
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

    def test_auth_token_bad_password(self):
        """
        Получения Токена Авторизации при неверном пароле
        """
        self.client.post(self.register_url, self.user_01_test)
        data = {
            'username': self.user_01_test.get("username"),
            'password': self.user_01_test.get("password") + "bad",
        }
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('non_field_errors', response.json())

    def test_auth_token_bad_username(self):
        """
        Получения Токена Авторизации при неверном имени пользователя
        """
        self.client.post(self.register_url, self.user_01_test)
        data = {
            'username': self.user_01_test.get("username") + "bad",
            'password': self.user_01_test.get("password"),
        }
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('non_field_errors', response.json())

    def test_token_authentication(self):
        """
        Авторизации с помощью токена и попытка получения данных
        Не авторизованным пользователем
        Авторизованным пользователем не администратором
        Авторизованным администратором
        """
        self.client.post(self.register_url, self.user_01_test)
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
        # print("auth_token", self.user_01["auth_token"])

        response = self.client.get(self.tag_list_url)
        # print("response.status_code", response.status_code)
        # print("response.data", response.data)
        # print("response.json()", response.json())
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_01_test["auth_token"])
        response = self.client.get(self.tag_list_url)
        # print("response.status_code", response.status_code)
        # print("response.data", response.data)
        # print("response.json()", response.json())
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        from user.models import User
        user_01_test = User.objects.get(username=self.user_01_test.get("username"))
        user_01_test.is_superuser = True
        user_01_test.is_staff = True
        user_01_test.save()

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_01_test["auth_token"])
        response = self.client.get(self.tag_list_url)
        # print("response.status_code", response.status_code)
        # print("response.data", response.data)
        # print("response.json()", response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # mm = "test_token_authentication"
        # print(f"^^^^^^^^^^^^^^^^^^^^============{mm}============^^^^^^^^^^^^^^^^^^^^")
