from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ItemLine,ItemProperty,Order

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
        field = ('user','status')
