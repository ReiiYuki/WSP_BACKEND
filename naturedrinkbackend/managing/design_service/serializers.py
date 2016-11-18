from design.models import DesignBottle,Bottle,Logo,Banner
from rest_framework import serializers

class DesignBottleSerializer(serializers.ModelSerializer) :
    class Meta :
        model = DesignBottle
        fields = ('id','name','description','image','is_active','user','is_request','is_confirm')
        extra_kwargs = {'id':{'read_only':True},'is_active':{'read_only':True},'is_request':{'read_only':True},'is_confirm':{'read_only':True}}

class BottleSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Bottle
        fields = ('id','name','img','is_active')

class BannerSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Banner
        fields = ('id','name','img','bottle','is_active')

class LogoSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Logo
        fields = ('id','name','img','is_active')
