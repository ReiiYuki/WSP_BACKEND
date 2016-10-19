from django.db import models

# Create your models here.
class PaymentMethod(models.Model) :
    type = models.CharField(max_length=1)
    name = models.CharField(max_length=13)
    is_active = models.BooleanField(default=True)
