from django.db import models
from product.models import  Product,ProductOption,ProductChoice
from django.contrib.auth.models import User

# Create your models here.
class ItemLine(models.Model) :
    user = models.ForeignKey(User)
    product = models.ForeignKey(Product)
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=1,default="C")

class ItemProperty(models.Model) :
    item = models.ForeignKey(ItemLine)
    option = models.ForeignKey(ProductOption)
    choice = models.ForeignKey(ProductChoice)
