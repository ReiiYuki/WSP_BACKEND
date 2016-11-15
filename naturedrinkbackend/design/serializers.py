from .models import DesignBottle
from rest_framework import serializers

class DesignBottleSerializer(serializers.ModelSerializer) :
    class Meta :
        model = DesignBottle
        fields = ('id','name','description','image','is_active','user')
        extra_kwargs = {'id':{'read_only':True},'is_active':{'read_only':True}}
