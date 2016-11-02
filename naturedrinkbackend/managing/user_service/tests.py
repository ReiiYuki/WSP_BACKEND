from rest_framework.test import APITestCase,APIClient
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserTest(APITestCase) :
    def setUp(self) :
        self.user = User.objects.create(username='admin',password='admin',is_staff=True)
        self.client.credentials(HTTP_AUTHORIZATION="Token "+Token.objects.get(user__username='admin').key)

    def test_get_user(self) :
        response = self.client.get('/api/v1/m/user/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)