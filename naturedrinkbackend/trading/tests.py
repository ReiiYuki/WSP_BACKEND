from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import PaymentMethod,Order,ItemLine
from product import models
from user.models import Address
class PaymentMethodTest(APITestCase) :

    def setUp(self):
        self.paymentMethod = PaymentMethod.objects.create(type="B",name="1103702001392")

    def test_list_payment_method(self) :
        response = self.client.get('/api/v1/t/method/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data,[{'type':'B','name':'1103702001392','is_active':True,'id':self.paymentMethod.id}])

class CartTest(APITestCase) :

    def setUp(self):
        self.user=User.objects.create(username="A",password="B")
        self.client.credentials(HTTP_AUTHORIZATION="Token "+Token.objects.get(user__username='A').key)
        self.category = models.Category.objects.create(name='Sample',description='Sample')
        self.product = models.Product.objects.create(name='P',description='PP',price=9,category=self.category)
        self.paymentMethod = PaymentMethod.objects.create(type="B",name="1103702001392")
        self.address = Address.objects.create(
        user=self.user,address_number="57/138",village="Thiptanee",road="Latphrao",sub_distinct="Chandrasem",distinct="Chatujak",province="Bangokok",country="Thailand",zipcode="10900"
        )

    def test_add_item_to_cart(self) :
        data = {"product":self.product.id,"quantity":10}
        response = self.client.post('/api/v1/t/cart/',data,format="json")
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_get_item_in_cart(self) :
        data = {"product":self.product.id,"quantity":10}
        response = self.client.post('/api/v1/t/cart/',data,format="json")
        response = self.client.get('/api/v1/t/cart/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data,[
        {
            'id': response.data[0]['id'],
            'product' : self.product.id,
            'user' : self.user.id,
            'order' : None,
            'quantity' : 10,
            'is_active' : True
        }
        ])

    def test_delete_item_in_cart(self) :
        data = {"product":self.product.id,"quantity":10}
        response = self.client.post('/api/v1/t/cart/',data,format="json")
        response = self.client.get('/api/v1/t/cart/')
        id = response.data[0]['id']
        response = self.client.delete('/api/v1/t/cart/'+str(id)+'/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        response = self.client.get('/api/v1/t/cart/')
        self.assertEqual(response.data,[])

    def test_update_item_in_cart(self) :
        data = {"product":self.product.id,"quantity":10}
        response = self.client.post('/api/v1/t/cart/',data,format="json")
        response = self.client.get('/api/v1/t/cart/')
        id = response.data[0]['id']
        data = {
        "product":response.data[0]['product'],
        "quantity" : 100
        }
        response = self.client.put('/api/v1/t/cart/'+str(id)+'/',data,format="json")
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        response = self.client.get('/api/v1/t/cart/')
        self.assertEqual(response.data,[
        {
            'id': response.data[0]['id'],
            'product' : self.product.id,
            'user' : self.user.id,
            'order' : None,
            'quantity' : 100,
            'is_active' : True
        }
        ])

    def test_pay_item_in_cart(self) :
        data = {"product":self.product.id,"quantity":10}
        response = self.client.post('/api/v1/t/cart/',data,format="json")
        data = {"method":self.paymentMethod.id,"address":self.address.id}
        response = self.client.post('/api/v1/t/cart/pay/',data,format="json")
        self.assertEqual(response.status_code,status.HTTP_200_OK)
