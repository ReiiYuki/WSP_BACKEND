from django.db import models
from product.models import  Product,ProductOption,ProductChoice
from django.contrib.auth.models import User

# Create your models here.

class Order(models.Model) :
    user = models.ForeignKey(User)
    status = models.CharField(max_length=1)

class ItemLine(models.Model) :
    user = models.ForeignKey(User)
    product = models.ForeignKey(Product)
    quantity = models.PositiveIntegerField()
    order = models.ForeignKey(Order,default=None)

class ItemProperty(models.Model) :
    item = models.ForeignKey(ItemLine)
    option = models.ForeignKey(ProductOption)
    choice = models.ForeignKey(ProductChoice)
