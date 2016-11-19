from .models import DesignBottle,Bottle,Banner,Logo
from rest_framework import serializers

class DesignBottleSerializer(serializers.ModelSerializer) :
    class Meta :
        model = DesignBottle
        fields = ('id','name','description','image','is_active','user','is_request','is_confirm')
        extra_kwargs = {'id':{'read_only':True},'user':{'read_only':True},'is_active':{'read_only':True},'is_request':{'read_only':True},'is_confirm':{'read_only':True}}

class BottleSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Bottle
        fields = ('id','name','img')

class BannerSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Banner
        fields = ('id','name','img','bottle')

class LogoSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Logo
        fields = ('id','name','img')
