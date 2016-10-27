from trading.models import Order
from rest_framework import serializers
class OrderSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Order
        fields = ('id','method','address','create_date','last_update_date','transfer_slip','is_paid','is_shipped','user','is_active','postal_track')
        extra_kwargs = {'id':{'read_only':True}}
