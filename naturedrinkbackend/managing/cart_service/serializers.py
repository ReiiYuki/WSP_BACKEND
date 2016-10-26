from trading.models import ItemLine,PaymentMethod
from rest_framework import serializers

class PaymentMethodSerializer(serializers.ModelSerializer) :
    class Meta :
        model = PaymentMethod
        fields = ('id','type','name','is_active')
        extra_kwargs = {'id':{'read_only':True}}

class ItemLineSerializer(serializers.ModelSerializer) :
    class Meta :
        model = ItemLine
        fields = ('id','product','user','order','quantity','is_active')
        extra_kwargs = {'id':{'read_only':True}}
