from django.db import models
from product.models import  Product,ProductOption,ProductChoice
from member.models import Address
from django.contrib.auth.models import User

# Create your models here.
class PaymentMethod(models.Model) :
    type = models.CharField(max_length=10)
    info = models.CharField(max_length=100)
    status = models.BooleanField()

class Order(models.Model) :
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.CharField(max_length=1,default='U')
    method = models.ForeignKey(PaymentMethod)
    address = models.ForeignKey(Address)
    slip = models.ImageField()
    upload_date = models.DateField()

class ItemLine(models.Model) :
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    order = models.ForeignKey(Order,blank=True,default=None,null=True)

class ItemProperty(models.Model) :
    item = models.ForeignKey(ItemLine,on_delete=models.CASCADE)
    option = models.ForeignKey(ProductOption,on_delete=models.CASCADE)
    choice = models.ForeignKey(ProductChoice,on_delete=models.CASCADE)
