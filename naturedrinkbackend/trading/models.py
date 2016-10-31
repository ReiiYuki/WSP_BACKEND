from django.db import models
from product.models import Product,ProductOption,ProductChoice
from django.contrib.auth.models import User
from user.models import Address
from . import thai_posttracking
# Create your models here.
class PaymentMethod(models.Model) :
    type = models.CharField(max_length=1)
    name = models.CharField(max_length=13)
    is_active = models.BooleanField(default=True)

class ItemProperty(models.Model) :
    option = models.ForeignKey(ProductOption)
    choice = models.ForeignKey(ProductChoice)

class Order(models.Model) :
    method = models.ForeignKey(PaymentMethod)
    address = models.ForeignKey(Address)
    create_date = models.DateField(auto_now_add=True)
    last_update_date = models.DateField(default=None,blank=True,null=True)
    transfer_slip = models.CharField(max_length=500)
    is_paid = models.BooleanField(default=False)
    is_shipped = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    postal_track = models.CharField(default=None,blank=True,null=True,max_length=13)
    user = models.ForeignKey(User)
    @property
    def status(self) :
        print (self.transfer_slip)
        if self.transfer_slip == "" and not self.is_paid:
            return "Wait for slip"
        if self.is_paid and not self.is_shipped:
            return "Upload Recieved"
        if self.is_shipped :
            data = thai_posttracking.check_tracking(self.postal_track)
            if len(data['tracking']['checkpoints'])<=0 :
                return "Pending Postal"
            status = data['tracking']['checkpoints'][0]['message']+' '+data['tracking']['checkpoints'][0]['location']+','+data['tracking']['checkpoints'][0]['country_iso3']
            return status
        return ""

class ItemLine(models.Model) :
    product = models.ForeignKey(Product)
    user = models.ForeignKey(User)
    order = models.ForeignKey(Order,default=None,null=True,blank=True)
    quantity = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)

class PostalTrack(models.Model) :
    order = models.ForeignKey(Order)
    is_active = models.BooleanField(default=True)
    tracking_number = models.CharField(max_length=13)
    upload_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
