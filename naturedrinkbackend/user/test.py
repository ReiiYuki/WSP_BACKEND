from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserTest(APITestCase) :
    
    def test_register_user(self):
        data = {"username":"test","password":"test","first_name":"test","last_name":"test","email":"test@test.test"}
        response = self.client.post('/api/v1/u/user/',data,format="json")
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_incomplete_register_user(self):
        data = {"password":"test","first_name":"test","last_name":"test","email":"test@test.test"}
        response = self.client.post('/api/v1/u/user/',data,format="json")
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
        data = {"username":"test","first_name":"test","last_name":"test","email":"test@test.test"}
        response = self.client.post('/api/v1/u/user/',data,format="json")
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)

    def test_login_user(self):
        data = {"username":"test","password":"test","first_name":"test","last_name":"test","email":"test@test.test"}
        response = self.client.post('/api/v1/u/user/',data,format="json")
        data={"username":"test","password":"test"}
        response = self.client.post('/api/v1/u/login/',data,format="json")
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        token = Token.objects.get(user__username='test')
        self.assertEqual(response.data['token'],token.key)
