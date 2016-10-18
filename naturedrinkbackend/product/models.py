from django.db import models

# Create your models here.
class Category(models.Model) :
    name = models.CharField(max_length=50)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

class Product(models.Model) :
    name = models.CharField(max_length=50)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    price = models.FloatField()
    category = models.ForeignKey(Category,related_name='products')

class ProductOption(models.Model) :
    name = models.CharField(max_length=30)
    product = models.ForeignKey(Product,related_name='options')
    is_active = models.BooleanField(default=True)

class ProductChocie(models.Model) :
    name = models.CharField(max_length=30)
    option = models.ForeignKey(ProductOption,related_name='choices')
    is_active = models.BooleanField(default=True)
