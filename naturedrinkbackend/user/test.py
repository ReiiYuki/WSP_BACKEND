from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

class UserTest(APITestCase) :
    def test_register_user(self):
        data = {"username":"test","password":"test","first_name":"test","last_name":"test","email":"test@test.test"}
        response = self.client.post('/api/v1/u/user/',data,format="json")
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(),1)
        self.assertEqual(User.objects.get().first_name,'test')

    def test_incomplete_register_user(self):
        data = {"password":"test","first_name":"test","last_name":"test","email":"test@test.test"}
        response = self.client.post('/api/v1/u/user/',data,format="json")
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
        data = {"username":"test","first_name":"test","last_name":"test","email":"test@test.test"}
        response = self.client.post('/api/v1/u/user/',data,format="json")
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
    
