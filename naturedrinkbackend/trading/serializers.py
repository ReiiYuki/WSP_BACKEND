from rest_framework import serializers
from .models import PaymentMethod , ItemProperty , Order , ItemLine , PostalTrack

class PaymentMethodSerializer(serializers.ModelSerializer) :
    class Meta :
        model = PaymentMethod
        fields = ('id','type','name','is_active')
        extra_kwargs = {'id':{'read_only':True},'is_active':{'read_only':True}}

class ItemPropertySerializer(serializers.ModelSerializer) :
    class Meta :
        model = ItemProperty
        fields = ('id','choice','option')
        extra_kwargs = {'id':{'read_only':True}}

class OrderSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Order
        fields = ('id','method','address','create_date','pay_date','transfer_slip','is_paid','is_shipped','is_active')
        extra_kwargs = {'id':{'read_only':True},'is_active':{'read_only':True},'create_date':{'read_only':True},'pay_date':{'read_only':True},'transfer_slip':{'read_only':True},'is_paid':{'read_only':True},'is_shipped':{'read_only':True}}

class ItemLineSerializer(serializers.ModelSerializer) :
    class Meta :
        model = ItemLine
        fields = ('id','product','user','order','property','quantity','is_active')
        extra_kwargs = {'id':{'read_only':True},'is_active':{'read_only':True},'user':{'read_only':True},'order':{'read_only':True}}

class PostalTrackSerializer(serializers.ModelSerializer) :
    class Meta :
        model = PaymentMethod
        fields = ('id','order','tracking_number','upload_date','update_date','is_active')
        extra_kwargs = {'id':{'read_only':True},'is_active':{'read_only':True},'upload_date':{'read_only':True},'update_date':{'read_only':True}}
