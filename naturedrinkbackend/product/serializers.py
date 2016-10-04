from rest_framework import serializers
from .models import Category,Product,ProductOption,ProductChoice

class CategorySerializer(serializers.ModelSerializer) :
    class Meta :
        model = Category
        field = ('name','detail')

class ProductSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Product
        field = ('name','detail','catagory','price')

class ProductOptionSerializer(serializers.ModelSerializer) :
    class Meta :
        model = ProductOption
        field = ('name')

class ProductChoiceSerializer(serializers.ModelSerializer) :
    class Meta :
        model = ProductChoice
        field = ('name')
