from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class DesignBottle(models.Model) :
    name = models.CharField(max_length=1000)
    description = models.TextField()
    image = models.CharField(max_length=1000)
    user = models.ForeignKey(User)
    is_active = models.BooleanField(default=True)
    is_request = models.BooleanField(default=False)
    is_confirm = models.BooleanField(default=False)

class Bottle(models.Model) :
    name = models.CharField(max_length=1000)
    img = models.CharField(max_length=1000)
    is_active = models.BooleanField(default=True)

class Banner(models.Model) :
    name = models.CharField(max_length=1000)
    img = models.CharField(max_length=1000)
    bottle = models.ForeignKey(Bottle)
    is_active = models.BooleanField(default=True)

class Logo(models.Model) :
    name = models.CharField(max_length=1000)
    img = models.CharField(max_length=1000)
    is_active = models.BooleanField(default=True)
