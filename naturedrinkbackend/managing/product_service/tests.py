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

    def test_put_category(self) :
        data={"name":"Drink","description":"Small Molecule"}
        response = self.client.post('/api/v1/m/category/',data,format="json")
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        data={"name":"Water","description":"Small Molecule","is_active":True}
        response = self.client.put('/api/v1/m/category/'+str(response.data['id'])+'/',data,format="json")
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data['name'],'Water')

    def test_get_category(self):
        response = self.client.get('/api/v1/m/category/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_deactivve_category(self) :
        data={"name":"Drink","description":"Small Molecule"}
        response = self.client.post('/api/v1/m/category/',data,format="json")
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        response = self.client.get('/api/v1/m/category/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        id = str(response.data[0]['id'])
        response = self.client.delete('/api/v1/m/category/'+str(response.data[0]['id'])+'/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        response = self.client.get('/api/v1/m/category/'+id+'/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data['is_active'],False)

    def test_reactive_category(self):
        data={"name":"Drink","description":"Small Molecule"}
        response = self.client.post('/api/v1/m/category/',data,format="json")
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        response = self.client.get('/api/v1/m/category/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        id = str(response.data[0]['id'])
        response = self.client.delete('/api/v1/m/category/'+str(response.data[0]['id'])+'/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        response = self.client.get('/api/v1/m/category/'+id+'/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data['is_active'],False)
        response = self.client.put('/api/v1/m/category/'+id+'/reactive/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        response = self.client.get('/api/v1/m/category/'+id+'/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data['is_active'],True)

class ProductTest(APITestCase) :

    def setUp(self) :
        self.user = User.objects.create(username='admin',password='admin',is_staff=True)
        self.client.credentials(HTTP_AUTHORIZATION="Token "+Token.objects.get(user__username='admin').key)
        self.category = models.Category.objects.create(name="D",description="B")

    def test_create_product(self) :
        data = {
            'image':'dummy.jpg',
            'name':'AAA',
            'description':'BBB',
            'price':100,
            'category': self.category.id,
            'is_active':True
        }
        response = self.client.post('/api/v1/m/product/',data,format='json')
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_update_product(self):
        data = {
            'image':'dummy.jpg',
            'name':'AAA',
            'description':'BBB',
            'price':100,
            'category': self.category.id,
            'is_active':True
        }
        response = self.client.post('/api/v1/m/product/',data,format='json')
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        id = response.data['id']
        data = {
            'image':'ssadsadsadsa.jpg',
            'name':'avvvdvdvd',
            'description':'BBB',
            'price':100,
            'category': self.category.id,
            'is_active':True
        }
        response = self.client.put('/api/v1/m/product/'+str(id)+'/',data,format="json")
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data['name'],'avvvdvdvd')

    def test_get_product(self):
        response=self.client.get('/api/v1/m/product/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_deactive_product(self):
        data = {
            'image':'dummy.jpg',
            'name':'AAA',
            'description':'BBB',
            'price':100,
            'category': self.category.id,
            'is_active':True
        }
        response = self.client.post('/api/v1/m/product/',data,format='json')
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        id = response.data['id']
        response = self.client.delete('/api/v1/m/product/'+str(id)+'/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        response=self.client.get('/api/v1/m/product/'+str(id)+'/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data['is_active'],False)

    def test_reactive_product(self):
        data = {
            'image':'dummy.jpg',
            'name':'AAA',
            'description':'BBB',
            'price':100,
            'category': self.category.id,
            'is_active':True
        }
        response = self.client.post('/api/v1/m/product/',data,format='json')
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        id = response.data['id']
        response = self.client.delete('/api/v1/m/product/'+str(id)+'/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        response=self.client.get('/api/v1/m/product/'+str(id)+'/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data['is_active'],False)
        response = self.client.put('/api/v1/m/product/'+str(id)+'/reactive/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        response=self.client.get('/api/v1/m/product/'+str(id)+'/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data['is_active'],True)
