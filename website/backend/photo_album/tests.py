from rest_framework import status
# from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from django.urls import reverse


# python3 manage.py test photo_album.tests --verbosity 2

class RegistrationTestCase(APITestCase):
    def setUp(self):
        self.register_url = reverse('user-list')
        # print("register_url", self.register_url)
        self.login_url = reverse('login')
        print("login_url", self.login_url)
        self.tag_list_url = reverse('tag-list')
        # print("tag_list_url", self.tag_list_url)

        self.user_01_test = {
            'username': 'user_01_test',
            'email': 'user_01_test@mm.mm',
            'password': 'User1Qwert',
            'first_name': "user_01_test",
            'last_name': "user_01_test",
        }

    def test_registration(self):
        # pass
        response = self.client.post(self.register_url, self.user_01_test)
        # print("response.status_code", response.status_code)
        # print("response.data", response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_data = {'username': 'user_01_test', 'email': 'user_01_test@mm.mm', 'first_name': 'user_01_test', 'last_name': 'user_01_test'}
        self.assertEqual(response.data, response_data)
        # self.assertEqual(response.data, self.user_01_test)
        from user.models import User
        user_01_test = User.objects.get(username=self.user_01_test.get("username"))
        # print(user_01_test.pk)

    def test_auth_token(self):
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
        self.client.post(self.register_url, self.user_01_test)
        data = {
            'username': self.user_01_test.get("username"),
            'password': self.user_01_test.get("password") + "bad",
        }
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('non_field_errors', response.json())

    def test_auth_token_bad_username(self):
        self.client.post(self.register_url, self.user_01_test)
        data = {
            'username': self.user_01_test.get("username") + "bad",
            'password': self.user_01_test.get("password"),
        }
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('non_field_errors', response.json())

    def test_token_authentication(self):
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
        # print("auth_token", self.user_01_test["auth_token"])

        # self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_01_test["auth_token"])
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








    # def test_photo_list_as_authorized(self):
    #     self._make_authentication()
    #     response = self.client.get(self.album_list_url)
    #
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #
    # def test_photo_list_as_unauthorized(self):
    #     response = self.client.get(self.album_list_url)
    #
    #     self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)





