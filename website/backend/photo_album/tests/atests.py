# from rest_framework import status
# # from rest_framework.authtoken.models import Token
# from rest_framework.test import APITestCase
# from django.urls import reverse
#
#
# # python3 manage.py test photo_album.tests --verbosity 2
#
# class UserTestCase(APITestCase):
#     def setUp(self):
#         self.register_url = reverse('user-list')
#         # print("register_url", self.register_url)
#         self.login_url = reverse('login')
#         # print("login_url", self.login_url)
#         self.tag_list_url = reverse('tag-list')
#         # print("tag_list_url", self.tag_list_url)
#
#         self.user_01 = {
#             'username': 'user_01',
#             'email': 'user_01@mm.mm',
#             'password': 'User1Qwert',
#             'first_name': "user_01",
#             'last_name': "user_01",
#         }
#
#     def test_registration(self):
#         """
#         Регистрация пользователя
#         """
#         # pass
#         response = self.client.post(self.register_url, self.user_01)
#         # print("response.status_code", response.status_code)
#         # print("response.data", response.data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         response_data = {'username': 'user_01', 'email': 'user_01@mm.mm', 'first_name': 'user_01', 'last_name': 'user_01'}
#         self.assertEqual(response.data, response_data)
#         # self.assertEqual(response.data, self.user_01)
#         from user.models import User
#         user_01 = User.objects.get(username=self.user_01.get("username"))
#         # print(user_01.pk)
#
#     def test_auth_token(self):
#         """
#         Получения Токена Авторизации
#         """
#         self.client.post(self.register_url, self.user_01)
#         data = {
#             'username': self.user_01.get("username"),
#             'password': self.user_01.get("password"),
#         }
#
#         response = self.client.post(self.login_url, data)
#         # print("response.status_code", response.status_code)
#         # print("response.data", response.data)
#         # print("response.json()", response.json())
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertIn('auth_token', response.json())
#
#     def test_auth_token_bad_password(self):
#         """
#         Получения Токена Авторизации при неверном пароле
#         """
#         self.client.post(self.register_url, self.user_01)
#         data = {
#             'username': self.user_01.get("username"),
#             'password': self.user_01.get("password") + "bad",
#         }
#         response = self.client.post(self.login_url, data)
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertIn('non_field_errors', response.json())
#
#     def test_auth_token_bad_username(self):
#         """
#         Получения Токена Авторизации при неверном имени пользователя
#         """
#         self.client.post(self.register_url, self.user_01)
#         data = {
#             'username': self.user_01.get("username") + "bad",
#             'password': self.user_01.get("password"),
#         }
#         response = self.client.post(self.login_url, data)
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertIn('non_field_errors', response.json())
#
#     def test_token_authentication(self):
#         """
#         Авторизации с помощью токена и попытка получения данных
#         Не авторизованным пользователем
#         Авторизованным пользователем не администратором
#         Авторизованным администратором
#         """
#         self.client.post(self.register_url, self.user_01)
#         data = {
#             'username': self.user_01.get("username"),
#             'password': self.user_01.get("password"),
#         }
#
#         response = self.client.post(self.login_url, data)
#         # print("response.status_code", response.status_code)
#         # print("response.data", response.data)
#         # print("response.json()", response.json())
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertIn('auth_token', response.json())
#
#         # print("auth_token", response.json()["auth_token"])
#         self.user_01["auth_token"] = response.json()["auth_token"]
#         # print("auth_token", self.user_01["auth_token"])
#
#         response = self.client.get(self.tag_list_url)
#         # print("response.status_code", response.status_code)
#         # print("response.data", response.data)
#         # print("response.json()", response.json())
#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
#
#         self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_01["auth_token"])
#         response = self.client.get(self.tag_list_url)
#         # print("response.status_code", response.status_code)
#         # print("response.data", response.data)
#         # print("response.json()", response.json())
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
#
#         from user.models import User
#         user_01 = User.objects.get(username=self.user_01.get("username"))
#         user_01.is_superuser = True
#         user_01.is_staff = True
#         user_01.save()
#
#         self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_01["auth_token"])
#         response = self.client.get(self.tag_list_url)
#         # print("response.status_code", response.status_code)
#         # print("response.data", response.data)
#         # print("response.json()", response.json())
#         self.assertEqual(response.status_code, status.HTTP_200_OK)


# class PhotoTestCase(APITestCase):
#     # fixtures = [
#     #     "backend/user/fixtures/init_fixtures.json",
#     #      "backend/photo_album/fixtures/init_fixtures.json",
#     # ]
#     def setUp(self):
#         self.register_url = reverse('user-list')
#         # print("register_url", self.register_url)
#         self.login_url = reverse('login')
#         # print("login_url", self.login_url)
#         self.tag_list_url = reverse('tag-list')
#         # print("tag_list_url", self.tag_list_url)
#
#         self.user_01 = {
#             'username': 'user_01',
#             'email': 'user_01@mm.mm',
#             'password': 'User1Qwert',
#             'first_name': "user_01",
#             'last_name': "user_01",
#         }
#
#
#
#
#         # # pass
#         #
#         # from photo_album.models import Tag
#         # tags = Tag.objects.all()
#
#
#
#
#
#         # self.user = UserFactory.create()
#         # self.token = Token.objects.create(user=self.user)
#         # self.album_list_url = reverse('album-list')
#         # self.valid_image = (
#         #     os.path.join(BASE_DIR, 'backend', 'album', 'fixtures', 'sunset.jpg')
#         # )
#         # self.invalid_image = (
#         #     os.path.join(BASE_DIR, 'backend', 'album', 'fixtures', 'sunset.bmp')
#         # )
#
#     def test_fixtures(self):
#         from photo_album.models import Tag
#         tags = Tag.objects.all()
#         print("tags len", len(tags))
#
#     def test_add_tag(self):
#         mm = "test_add_tag"
#         print(f"vvvvvvvvvvvvvvvvvvvv============{mm}============vvvvvvvvvvvvvvvvvvvv")
#         # добавляем пользователя
#         self.client.post(self.register_url, self.user_01)
#
#         # делаем его админом
#         from user.models import User
#         user_01 = User.objects.get(username=self.user_01.get("username"))
#         user_01.is_superuser = True
#         user_01.is_staff = True
#         user_01.save()
#
#         # получаю токен
#         data = {
#             'username': self.user_01.get("username"),
#             'password': self.user_01.get("password"),
#         }
#         response = self.client.post(self.login_url, data)
#         # print("response.status_code", response.status_code)
#         # print("response.data", response.data)
#         # print("response.json()", response.json())
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertIn('auth_token', response.json())
#         # print("auth_token", response.json()["auth_token"])
#         self.user_01["auth_token"] = response.json()["auth_token"]
#
#         # добавляю токен авторизации к запросу
#         self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_01["auth_token"])
#
#         # Доступен ли адрес
#         response = self.client.get(self.tag_list_url)
#         print("response.status_code", response.status_code)
#         print("response.data", response.data)
#         print("response.json()", response.json())
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#         # Добавляю тег
#         new_tag_data = {
#             "name": "TEST_TAG",
#         }
#         response = self.client.post(self.tag_list_url,new_tag_data)
#         print("response.status_code", response.status_code)
#         print("response.data", response.data)
#         print("response.json()", response.json())
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#
#         # проверяю Добавлен ли тег
#         response = self.client.get(self.tag_list_url)
#         print("response.status_code", response.status_code)
#         print("response.data", response.data)
#         print("response.json()", response.json())
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.json(), [{'id': 1, 'name': 'TEST_TAG'}])
#         self.assertEqual(response.data, [{'id': 1, 'name': 'TEST_TAG'}])
#
#         print(f"^^^^^^^^^^^^^^^^^^^^============{mm}============^^^^^^^^^^^^^^^^^^^^")
#
#
