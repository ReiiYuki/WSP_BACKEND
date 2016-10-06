from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ItemLine,ItemProperty

class ItemLineSerializer(serializers.ModelSerializer) :
    class Meta :
        model = ItemLine
        field = ('user','product','quantity')

class ItemPropertySerializer(serializers.ModelSerializer) :
    class Meta :
        model = ItemProperty
        field = ('item','option','choice')
