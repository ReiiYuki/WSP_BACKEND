from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Address(models.Model) :
    user = models.ForeignKey(User)
    address_number = models.CharField(max_length=10)
    village = models.CharField(max_length=100)
    road = models.CharField(max_length=100)
    sub_distinct = models.CharField(max_length=100)
    distinct = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zipcode=  models.CharField(max_length=6)
