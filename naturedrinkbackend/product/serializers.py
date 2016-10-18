from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer) :
    class Meta :
        model = Category
        fields = ('id','name','description','is_active')
        extra_kwargs = {'id':{'read_only':True},'is_active':{'read_only':True}}
        
