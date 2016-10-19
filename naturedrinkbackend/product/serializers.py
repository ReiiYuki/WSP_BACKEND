from rest_framework import serializers
from .models import Category,Product,ProductOption,ProductChocie

class ProductChoiceSerializer(serializers.ModelSerializer) :
    class Meta :
        model = ProductChocie
        fields = ('id','name','is_active','option')
        extra_kwargs = {'id':{'read_only':True},'is_active':{'read_only':True}}

class ProductOptionSerializer(serializers.ModelSerializer) :
    choices = ProductChocieSerializer(many=True)
    class Meta :
        model = ProductOption
        fields = ('id','name','is_active','product','choices')
        extra_kwargs = {'id':{'read_only':True},'is_active':{'read_only':True},'choices':{'read_only':True}}

class ProductSerializer(serializers.ModelSerializer) :
    options = ProductOptionSerializer(many=True)
    class Meta :
        model = Product
        fields = ('id','name','description','price','is_active','category','options')
        extra_kwargs = {'id':{'read_only':True},'is_active':{'read_only':True},'options':{'read_only':True}}

class CategorySerializer(serializers.ModelSerializer) :
    products = ProductSerializer(many=True)
    class Meta :
        model = Category
        fields = ('id','name','description','is_active','products')
        extra_kwargs = {'id':{'read_only':True},'is_active':{'read_only':True},'product':{'read_only':True}}
