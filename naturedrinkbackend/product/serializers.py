from rest_framework import serializers
from .models import Category,Product

class CategorySerializer(serializers.ModelSerializer) :
    class Meta :
        model = Category
        field = ('name','detail')

class ProductSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Product
        field = ('name','detail','catagory','price')
