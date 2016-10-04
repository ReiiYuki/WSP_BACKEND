from django.db import models

# Create your models here.
class Category (models.Model) :
    name = models.CharField(max_length=100)
    detail = models.TextField()


class Product (models.Model) :
    name = models.CharField(max_length=100)
    detail = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey(Category)
