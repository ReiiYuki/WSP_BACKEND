from rest_framework.test import APITestCase,APIClient
from rest_framework import status
from .models import Category,Product

class ProductTest(APITestCase) :

    def test_list_product(self) :
        response = self.client.get('/api/v1/p/product/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)

class Category(APITestCase) :

    def test_list_category(self) :
        response = self.client.get('/api/v1/p/category/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
