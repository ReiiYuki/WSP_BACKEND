from django.db import models
from product.models import  Product,ProductOption,ProductChoice
from django.contrib.auth.models import User

# Create your models here.

class Order(models.Model) :
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.CharField(max_length=1)

class ItemLine(models.Model) :
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    order = models.ForeignKey(Order,default=None)

class ItemProperty(models.Model) :
    item = models.ForeignKey(ItemLine,on_delete=models.CASCADE)
    option = models.ForeignKey(ProductOption,on_delete=models.CASCADE)
    choice = models.ForeignKey(ProductChoice,on_delete=models.CASCADE)
