from product.models import Product,Category
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer) :
    class Meta :
        model = Category
        fields = ('id','name','description','is_active')
        extra_kwargs = {'id':{'read_only':True}}
class ProductSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Product
        fields = ('id','name','description','price','is_active','category','image')
        extra_kwargs = {'id':{'read_only':True}}
