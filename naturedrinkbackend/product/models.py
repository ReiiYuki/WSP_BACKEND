from django.db import models
from design.models import DesignBottle
# Create your models here.
class Category(models.Model) :
    name = models.CharField(max_length=50)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    def __str__(self)  :
        return self.name

class Product(models.Model) :
    name = models.CharField(max_length=50)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    price = models.FloatField()
    image = models.CharField(max_length=500)
    category = models.ForeignKey(Category,related_name='products',null=True)
    design = models.ForeignKey(DesignBottle,null=True,default=None,blank=True)
    def __str__(self)  :
        return self.name
