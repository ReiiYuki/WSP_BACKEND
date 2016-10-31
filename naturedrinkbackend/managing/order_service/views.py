from rest_framework.response import Response
from trading.models import Order
from ..permissions import isAdmin
from .serializers import OrderSerializer
from rest_framework import viewsets,renderers
from rest_framework.decorators import detail_route
import datetime

class OrderViewSet(viewsets.ModelViewSet) :
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (isAdmin,)
    @detail_route(methods=['put'],renderer_classes=[renderers.JSONRenderer])
    def confirmPayment(self,request,pk=None) :
        order=Order.objects.get(id=pk)
        order.is_paid = True
        order.last_upate_date = datetime.datetime.now()
        order.save()
        return Response(OrderSerializer(order).data)

    @detail_route(methods=['put'],renderer_classes=[renderers.JSONRenderer])
    def unconfirmPayment(self,request,pk=None) :
        order=Order.objects.get(id=pk)
        order.is_paid = False
        order.postal_track=''
        order.is_shipped=False
        order.last_upate_date = datetime.datetime.now()
        order.save()
        return Response(OrderSerializer(order).data)

    @detail_route(methods=['put'],renderer_classes=[renderers.JSONRenderer])
    def updateTrack(self,request,pk=None) :
        track=request.data['track']
        order=Order.objects.get(id=pk)
        order.last_upate_date = datetime.datetime.now()
        order.postal_track=track
        order.is_shipped=True
        order.save()
        return Response(OrderSerializer(order).data)
