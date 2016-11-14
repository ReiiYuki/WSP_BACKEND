from .models import DesignBottle,DesignRequest
from rest_framework import serializers

class DesignBottleSerializer(serializers.ModelSerializer) :
    class Meta :
        model = DesignBottle
        fields = ('id','name','description','image')
        extra_kwargs = {'id':{'read_only':True}}
