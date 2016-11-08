from rest_framework import serializers
from .models import PaymentMethod  , Order , ItemLine

class PaymentMethodSerializer(serializers.ModelSerializer) :
    class Meta :
        model = PaymentMethod
        fields = ('id','type','name','is_active')
        extra_kwargs = {'id':{'read_only':True},'is_active':{'read_only':True}}

class OrderSerializer(serializers.ModelSerializer) :
    status = serializers.ReadOnlyField()
    class Meta :
        model = Order
        fields = ('id','method','address','create_date','last_update_date','transfer_slip','is_paid','is_shipped','user','is_active','postal_track','status')
        extra_kwargs = {'id':{'read_only':True},'is_active':{'read_only':True},'create_date':{'read_only':True},'last_update_date':{'read_only':True},'transfer_slip':{'read_only':True},'is_paid':{'read_only':True},'is_shipped':{'read_only':True},'user':{'read_only':True},'postal_track':{'read_only':True}}

class ItemLineSerializer(serializers.ModelSerializer) :
    class Meta :
        model = ItemLine
        fields = ('id','product','user','order','quantity','is_active')
        extra_kwargs = {'id':{'read_only':True},'is_active':{'read_only':True},'user':{'read_only':True},'order':{'read_only':True}}
