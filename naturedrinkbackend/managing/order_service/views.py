from rest_framework.response import Response
from trading.models import Order
from ..permissions import isAdmin
from .serializers import OrderSerializer
from rest_framework import viewsets,renderers
from rest_framework.decorators import detail_route
import datetime
from . import thai_posttracking
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
        r = thai_posttracking.add_tracking(track)
        order=Order.objects.get(id=pk)
        order.last_upate_date = datetime.datetime.now()
        order.postal_track=track
        order.is_shipped=True
        order.save()
        return Response(OrderSerializer(order).data)

    @detail_route(methods=['put'],renderer_classes=[renderers.JSONRenderer])
    def deleteTrack(self,request,pk=None) :
        track=""
        order=Order.objects.get(id=pk)
        order.last_upate_date = datetime.datetime.now()
        try :
            r = thai_posttracking.delete_tracking(order.postal_track)
        except KeyError :
            pass
        order.postal_track=track
        order.is_shipped=False
        order.save()
        return Response(OrderSerializer(order).data)
