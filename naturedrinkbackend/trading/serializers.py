from rest_framework import serializers
from .models import PaymentMethod , ItemProperty , Order , ItemLine , PostalTrack

class PaymentMethodSerializer(serializers.ModelSerializer) :
    class Meta :
        model = PaymentMethod
        fields = ('id','type','name','is_active')
        extra_kwargs = {'id':{'read_only':True},'is_active':{'read_only':True}}
