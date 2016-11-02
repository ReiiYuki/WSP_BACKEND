from rest_framework.test import APITestCase,APIClient
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from product import models

class CategoryTest(APITestCase) :
    def setUp(self) :
        self.user = User.objects.create(username='admin',password='admin',is_staff=True)
        self.client.credentials(HTTP_AUTHORIZATION="Token "+Token.objects.get(user__username='admin').key)

    def test_add_category(self) :
        data={"name":"Drink","description":"Small Molecule"}
        response = self.client.post('/api/v1/m/category/',data,format="json")
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
