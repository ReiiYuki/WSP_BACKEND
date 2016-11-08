from django.db import models

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
    category = models.ForeignKey(Category,related_name='products')
    def __str__(self)  :
        return self.name
