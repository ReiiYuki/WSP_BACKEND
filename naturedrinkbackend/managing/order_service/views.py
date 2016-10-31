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
        header = {"aftership-api-key": "9442c41d-f380-482e-954c-2a1c996f1815","Content-Type": "application/json"}
        url = "https://api.aftership.com/v4/trackings"
        r = requests.post(url,headers=header,json={"slug":"thailand-post","tracking":{"tracking_number":track}})
        print (r.json())
        url = url+"/thailand-post/"+track
        r = requests.get(url,headers=header)
        print (r.json())
        order=Order.objects.get(id=pk)
        order.last_upate_date = datetime.datetime.now()
        order.postal_track=track
        order.is_shipped=True
        order.save()
        return Response(OrderSerializer(order).data)

    @detail_route(methods=['put'],renderer_classes=[renderers.JSONRenderer])
    def deleteTrack(self,request,pk=None) :
        header = {"aftership-api-key": "9442c41d-f380-482e-954c-2a1c996f1815","Content-Type": "application/json"}
        url = "https://api.aftership.com/v4/trackings/thailand-post/"+order.postal_track
        r = requests.delete(url,header)
        print (r.json())
        track=""
        order=Order.objects.get(id=pk)
        order.last_upate_date = datetime.datetime.now()
        order.postal_track=track
        order.is_shipped=False
        order.save()
        return Response(OrderSerializer(order).data)
