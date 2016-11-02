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

    def test_assign_staff(self) :
        user = User.objects.create(username="A",password="B")
        response = self.client.put('/api/v1/m/user/'+str(user.id)+'/assign_staff/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        response = self.client.get('/api/v1/m/user/'+str(user.id)+'/')
        self.assertEqual(response.data['is_staff'],True)

    def test_fire_staff(self) :
        user = User.objects.create(username="A",password="B")
        response = self.client.put('/api/v1/m/user/'+str(user.id)+'/assign_staff/')
        response = self.client.get('/api/v1/m/user/'+str(user.id)+'/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        response = self.client.get('/api/v1/m/user/'+str(user.id)+'/')
        self.assertEqual(response.data['is_staff'],True)
        response = self.client.put('/api/v1/m/user/'+str(user.id)+'/fire_staff/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        response = self.client.get('/api/v1/m/user/'+str(user.id)+'/')
        self.assertEqual(response.data['is_staff'],False)
