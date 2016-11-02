from rest_framework.test import APITestCase,APIClient
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from trading.models import ItemLine,PaymentMethod

class PaymentMethodTest(APITestCase):
    def setUp(self) :
        self.user = User.objects.create(username='admin',password='admin',is_staff=True)
        self.client.credentials(HTTP_AUTHORIZATION="Token "+Token.objects.get(user__username='admin').key)

    def test_create_payment_method(self) :
        data = {
            "name" : "1103702001392",
            "type" : "B",
            "is_active" : True
        }
        response = self.client.post('/api/v1/m/method/',data,format="json")
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_update_payment_method(self) :
        data = {
            "name" : "1103702001392",
            "type" : "B",
            "is_active" : True
        }
        response = self.client.post('/api/v1/m/method/',data,format="json")
        id = response.data['id']
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        data = {
            "name" : "110-702-013-2",
            "type" : "B",
            "is_active" : True
        }
        response = self.client.put('/api/v1/m/method/'+str(id)+'/',data,format="json")
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data['name'],data['name'])

    def test_get_payment_method(self) :
        data = {
            "name" : "1103702001392",
            "type" : "B",
            "is_active" : True
        }
        response = self.client.get('/api/v1/m/method/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_deactive_method(self) :
        data = {
            "name" : "1103702001392",
            "type" : "B",
            "is_active" : True
        }
        response = self.client.post('/api/v1/m/method/',data,format="json")
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        id = response.data['id']
        response = self.client.delete('/api/v1/m/method/'+str(id)+'/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        response = self.client.get('/api/v1/m/method/'+str(id)+'/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data['is_active'],False)
