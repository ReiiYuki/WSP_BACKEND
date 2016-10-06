from django.db import models

# Create your models here.
class Category (models.Model) :
    name = models.CharField(max_length=100)
    detail = models.TextField()


class Product (models.Model) :
    name = models.CharField(max_length=100)
    detail = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

class ProductOption(models.Model) :
    name = models.CharField(max_length=100)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

class ProductChoice(models.Model) :
    name = models.CharField(max_length=100)
    option = models.ForeignKey(ProductOption,on_delete=models.CASCADE)
