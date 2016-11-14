from django.db import models

# Create your models here.
class DesignBottle(models.Model) :
    name = models.CharField(max_length=1000)
    description = models.TextField()
    image = models.CharField(max_length=1000)
    is_active = models.BooleanField(default=True)

class DesignRequest(models.Model) :
    bottle = models.ForeignKey(DesignBottle)
    is_confirm = models.BooleanField(default=False)
    price = models.FloatField(default=None,null=True)
    is_active = models.BooleanField(default=True)
