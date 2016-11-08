from django.db import models
from product.models import Product
from django.contrib.auth.models import User
from user.models import Address
from . import thai_posttracking
# Create your models here.
class PaymentMethod(models.Model) :
    type = models.CharField(max_length=1)
    name = models.CharField(max_length=13)
    is_active = models.BooleanField(default=True)

class Order(models.Model) :
    method = models.ForeignKey(PaymentMethod)
    address = models.ForeignKey(Address)
    create_date = models.DateField(auto_now_add=True)
    transfer_slip = models.CharField(max_length=500)
    is_paid = models.BooleanField(default=False)
    is_shipped = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    postal_track = models.CharField(default=None,blank=True,null=True,max_length=13)
    user = models.ForeignKey(User)
    @property
    def status(self) :
        if self.transfer_slip == "" and not self.is_paid:
            return "Wait for slip"
        if self.transfer_slip is not "" and not self.is_paid and not self.is_shipped:
            return "Upload Recieved"
        if self.is_paid and not self.is_shipped:
            return "Payment Comfirmed"
        if self.is_shipped :
            data = thai_posttracking.check_tracking(self.postal_track)
            if len(data)==0 or len(data['tracking']['checkpoints'])<=0 :
                return "Pending Postal"
            status = data['tracking']['checkpoints'][len(data['tracking']['checkpoints'])-1]['message']+' '+data['tracking']['checkpoints'][len(data['tracking']['checkpoints'])-1]['location']+','+data['tracking']['checkpoints'][len(data['tracking']['checkpoints'])-1]['country_iso3']
            return status
        return ""

class ItemLine(models.Model) :
    product = models.ForeignKey(Product)
    user = models.ForeignKey(User)
    order = models.ForeignKey(Order,default=None,null=True,blank=True)
    quantity = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
