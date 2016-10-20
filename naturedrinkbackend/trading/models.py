from django.db import models
from product.models import Product,ProductOption,ProductChoice
from django.contrib.auth.models import User
from user.models import Address
# Create your models here.
class PaymentMethod(models.Model) :
    type = models.CharField(max_length=1)
    name = models.CharField(max_length=13)
    is_active = models.BooleanField(default=True)

class ItemProperty(models.Model) :
    option = models.ForeignKey(ProductOption)
    choice = models.ForeignKey(ProductChoice)

class Order(models.Model) :
    method = models.ForeignKey(PaymentMethod)
    address = models.ForeignKey(Address)
    create_date = models.DateField(auto_now_add=True)
    pay_date = models.DateField(default=None,blank=True,null=True)
    transfer_slip = models.ImageField(upload_to='images/slips',default=None)
    is_paid = models.BooleanField(default=False)
    is_shipped = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User)

class ItemLine(models.Model) :
    product = models.ForeignKey(Product)
    user = models.ForeignKey(User)
    order = models.ForeignKey(Order,default=None,null=True,blank=True)
    property = models.ForeignKey(ItemProperty)
    quantity = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)

class PostalTrack(models.Model) :
    order = models.ForeignKey(Order)
    is_active = models.BooleanField(default=True)
    tracking_number = models.CharField(max_length=13)
    upload_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
