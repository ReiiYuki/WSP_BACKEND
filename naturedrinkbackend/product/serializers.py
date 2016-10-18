from rest_framework import serializers
from .models import Category,Product

class ProductSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Product
        fields = ('id','name','description','price','is_active','category')
        extra_kwargs = {'id':{'read_only':True},'is_active':{'read_only':True}}

class CategorySerializer(serializers.ModelSerializer) :
    products = ProductSerializer(many=True)
    class Meta :
        model = Category
        fields = ('id','name','description','is_active','products')
        extra_kwargs = {'id':{'read_only':True},'is_active':{'read_only':True},'product':{'read_only':True}}
