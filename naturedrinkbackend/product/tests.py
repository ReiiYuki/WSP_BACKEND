from rest_framework.test import APITestCase,APIClient
from rest_framework import status
from . import models
import json
class ProductTest(APITestCase) :

    def setUp(self) :
        self.category = models.Category.objects.create(name='Sample',description='Sample')
        self.product = models.Product.objects.create(name='P',description='PP',price=9,category=self.category)

    def test_list_product(self) :
        response = self.client.get('/api/v1/p/product/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(json.loads(json.dumps(response.data)),[{"name":"P","description":"PP","price":9,"category":self.category.id,"is_active":True,"image":"","id":self.product.id}])

    def test_get_product(self) :
        response = self.client.get('/api/v1/p/product/'+str(self.product.id)+'/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data,{"name":"P","description":"PP","price":9,"category":self.category.id,"is_active":True,"image":"","id":self.product.id})

class Category(APITestCase) :

    def setUp(self) :
        self.category = models.Category.objects.create(name='Sample',description='Sample')

    def test_list_category(self) :
        response = self.client.get('/api/v1/p/category/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data,[{'id':self.category.id,'name':'Sample','description':'Sample','is_active':True}])

    def test_get_category(self) :
        response = self.client.get('/api/v1/p/category/'+str(self.category.id)+'/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data,{'id':self.category.id,'name':'Sample','description':'Sample','is_active':True})
