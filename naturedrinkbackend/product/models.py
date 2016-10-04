from django.db import models

# Create your models here.
class Catagory (models.Model) :
    name = models.CharField(max_length=100)
    detail = models.TextField()

class Product (models.Model) :
    name = models.CharField(max_length=100)
    detail = models.TextField()
    price = models.FloatField()
    catagory = models.ForeignKey(Catagory)
