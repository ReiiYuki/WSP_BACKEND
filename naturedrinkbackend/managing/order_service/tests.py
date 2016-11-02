from rest_framework.test import APITestCase,APIClient
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from product import models
from trading.models import ItemLine,Order,PaymentMethod
from user.models import Address
class OrderTest(APITestCase) :
    def setUp(self) :
        self.user = User.objects.create(username='admin',password='admin',is_staff=True)
        self.client.credentials(HTTP_AUTHORIZATION="Token "+Token.objects.get(user__username='admin').key)
        self.category = models.Category.objects.create(name="A",description="dsa")
        self.product = models.Product.objects.create(name="A",price=555,category=self.category,description="sad")
        self.method = PaymentMethod.objects.create(name="1103702001392",type="B")
        self.address = Address.objects.create(user=self.user,address_number="57/138",village="Thiptanee",road="Latphrao",sub_distinct="Chandrasem",distinct="Chatujak",province="Bangokok",country="Thailand",zipcode="10900")
    def test_get_order(self) :
        response=self.client.get('/api/v1/m/order/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    def test_confirm_order(self) :
        order = Order.objects.create(user=self.user,address=self.address,method=self.method)
        response = self.client.put('/api/v1/m/order/'+str(order.id)+'/confirmPayment/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        response=self.client.get('/api/v1/m/order/'+str(order.id)+'/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data['is_paid'],True)
