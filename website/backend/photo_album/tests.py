# from rest_framework import status
# from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from django.urls import reverse


# python3 manage.py test photo_album.tests --verbosity 2

class RegistrationTestCase(APITestCase):
    def setUp(self):
        self.register_url = reverse('user-list')
        print(self.register_url)
        self.login_url = reverse('drf-auth')
        # self.login_url = reverse('login')
        print(self.login_url)

        self.credentials = {
            'username': 'ctoiia',
            'email': 'fffxx@mail.ru',
            'password': 'c8846601'
        }






    def test_registration(self):
        pass
    # response = self.client.post(self.register_url, self.credentials)

    # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    # self.assertEqual(response.data, {'email': 'fffxx@mail.ru', 'username': 'ctoiia', 'id': 1})
    #
    # def test_auth_token(self):
    #     self.client.post(self.register_url, self.credentials)
    #     data = {
    #         'username': 'ctoiia',
    #         'password': 'c8846601'
    #     }
    #
    #     response = self.client.post(self.login_url, data)
    #
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertIn('auth_token', response.json())
