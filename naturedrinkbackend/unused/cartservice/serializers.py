from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ItemLine,ItemProperty,Order,PaymentMethod

class CartItemLineSerializer(serializers.ModelSerializer) :
    class Meta :
        model = ItemLine
        field = ('product','quantity')

class ItemPropertySerializer(serializers.ModelSerializer) :
    class Meta :
        model = ItemProperty
        field = ('item','option','choice')

class OrderSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Order
        field = ('user','status','method')

class PaymentMethodSerializer(serializers.ModelSerializer) :
    class Meta :
        model = PaymentMethod
        field = ('type','info','status')
