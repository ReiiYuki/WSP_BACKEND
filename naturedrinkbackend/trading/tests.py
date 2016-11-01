from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import PaymentMethod,Order,ItemLine

class PaymentMethodTest(APITestCase) :

    def setUp(self):
        self.paymentMethod = PaymentMethod.objects.create(type="B",name="1103702001392")

    def test_list_payment_method(self) :
        response = self.client.get('/api/v1/t/method/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data,[{'type':'B','name':'1103702001392','is_active':True,'id':self.paymentMethod.id}])
