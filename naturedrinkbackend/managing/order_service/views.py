from trading.models import Order
from ..permissions import isAdmin
from .serializers import OrderSerializer
from rest_framework import viewsets
from rest_framework.decorators import detail_route
import datetime

class OrderViewSet(viewsets.ModelViewSet) :
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (isAdmin,)

    def comfirmPayment(self,request,pk=None) :
        order=Order.objects.get(id=pk)
        order.is_paid = True
        order.last_upate_date = datetime.datetime.now()
        order.save()
        return Response(OrderSerializer(order).data)

    def updateTrack(self,request,pk=None) :
        track=request.data['track']
        order=Order.objects.get(id=pk)
        order.last_upate_date = datetime.datetime.now()
        order.postal_track=track
        order.is_shipped=True
        order.save()
        return Response(OrderSerializer(order).data)
