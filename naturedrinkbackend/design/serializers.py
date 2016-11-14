from .models import DesignBottle,DesignRequest
from rest_framework import serializers

class DesignBottleSerializer(serializers.ModelSerializer) :
    class Meta :
        model = DesignBottle
        fields = ('id','name','description','image','is_active')
        extra_kwargs = {'id':{'read_only':True},'is_active':{'read_only':True}}
class DesignRequestSerializer(serializers.ModelSerializer) :
    class Meta :
        model = DesignRequest
        fields = ('id','bottle','is_confirm','price','is_active')
        extra_kwargs = {'id':{'read_only':True},'is_active':{'read_only':True}}
