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
