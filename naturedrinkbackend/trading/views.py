from .models import PaymentMethod  , Order , ItemLine
from .serializers import PaymentMethodSerializer,OrderSerializer,ItemLineSerializer
from rest_framework import viewsets,renderers,status
from rest_framework.response import Response
from rest_framework.decorators import list_route,detail_route
from user.models import Address
import datetime
import requests
PERMISSION_DENIED_CONTENT = { "detail" : "Permission denied."}

# Create your views here.
''' Get OK '''
class PaymentMethodViewSet(viewsets.ModelViewSet) :
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer

    ''' Create OK '''
    def create(self,request) :
        return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)

    ''' Update OK '''
    def update(self,request,pk=None) :
        return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)

    ''' Deactive OK '''
    def destroy(self,request,pk=None) :
        return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)

    ''' Reactive OK '''
    @detail_route(methods=['put'],renderer_classes=[renderers.JSONRenderer])
    def reactive(self,request,pk=None) :
        return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)

''' Get OK'''
class ItemLineViewSet(viewsets.ModelViewSet) :
    queryset = ItemLine.objects.all()
    serializer_class = ItemLineSerializer
    ''' List Ok '''
    def list(self,request) :
        if request.user.is_anonymous :
            return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)
        return Response(ItemLineSerializer(ItemLine.objects.filter(user=request.user,is_active=True,order=None),many=True).data)

    @list_route(methods=['get'],renderer_classes=[renderers.JSONRenderer])
    def lines(self,request) :
        if request.user.is_anonymous :
            return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)
        return  Response(ItemLineSerializer(ItemLine.objects.filter(user=request.user,is_active=True),many=True).data)

    ''' Create OK '''
    def create(self,request) :
        if request.user.is_anonymous :
            return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)
        return super(ItemLineViewSet,self).create(request)

    ''' Put OK '''
    def update(self,request,pk) :
        if request.user.is_anonymous :
            return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)
        return super(ItemLineViewSet,self).update(request)

    ''' Deactive OK '''
    def destroy(self,request,pk=None) :
        if request.user.is_anonymous :
            return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)
        line = ItemLine.objects.get(id=pk)
        line.is_active = False
        line.save()
        return Response({"detail" : "Deactive successful"})

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    ''' Work '''
    @list_route(methods=['post'],renderer_classes=[renderers.JSONRenderer])
    def pay(self,request) :
        if request.user.is_anonymous :
            return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)
        address = Address.objects.get(id=request.data['address'])
        method = PaymentMethod.objects.get(id=request.data['method'])
        order = Order(method=method,address=address,user=request.user)
        order.save()
        cart_item =  ItemLine.objects.filter(user=request.user,order=None)
        for i in cart_item :
            i.order = order
            i.save()
        return Response(OrderSerializer(order).data)

''' Get OK'''
class OrderViewSet(viewsets.ModelViewSet) :
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    def list(self,request) :
        if request.user.is_anonymous :
            return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)
        return Response(OrderSerializer(Order.objects.filter(user=request.user,is_active=True),many=True).data)

    def create(self,request) :
        return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)

    def change_method(self,request,pk=None) :
        if request.user.is_anonymous :
            return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)
        method = PaymentMethod.objects.get(id=request.data['method'])
        order = Order.objects.get(id=pk)
        order.method = method
        order.save()
        return Response(OrderSerializer(order).data)
    @detail_route(methods=['put'],renderer_classes=[renderers.JSONRenderer])
    def upload_slip(self,request,pk=None) :
        if request.user.is_anonymous :
            return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)
        order = Order.objects.get(id=pk)
        order.transfer_slip = request.data['transfer_slip']
        order.save()
        return Response(OrderSerializer(order).data)

    @detail_route(methods=['put'],renderer_classes=[renderers.JSONRenderer])
    def delete_slip(self,request,pk=None) :
        if request.user.is_anonymous :
            return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)
        order = Order.objects.get(id=pk)
        order.transfer_slip = ""
        order.save()
        return Response(OrderSerializer(order).data)

    @detail_route(methods=['put'],renderer_classes=[renderers.JSONRenderer])
    def update_track(self,request,pk=None) :
        if not request.user.is_staff :
            return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)
        order = Order.objects.get(id=pk)
        order.postal_track = request.data['postal_track']
        order.is_shipped = True
        order.save()
        return Response(OrderSerializer(order).data)

    @detail_route(methods=['delete'],renderer_classes=[renderers.JSONRenderer])
    def delete_track(self,request,pk=None) :
        if not request.user.is_staff :
            return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)
        order = Order.objects.get(id=pk)
        order.postal_track = None
        order.is_shipped = False
        order.save()
        return Response(OrderSerializer(order).data)

    @detail_route(methods=['put'],renderer_classes=[renderers.JSONRenderer])
    def confirm(self,request,pk=None) :
        if not request.user.is_staff :
            return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)
        order = Order.objects.get(id=pk)
        order.is_paid = True
        order.save()
        return Response(OrderSerializer(order).data)

    @detail_route(methods=['delete'],renderer_classes=[renderers.JSONRenderer])
    def deconfirm(self,request,pk=None) :
        if not request.user.is_staff :
            return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)
        order = Order.objects.get(id=pk)
        order.is_paid = False
        order.save()
        return Response(OrderSerializer(order).data)

    def destroy(self,request,pk=None) :
        if request.user.is_anonymous :
            return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)
        order = Order.objects.get(id=pk)
        order.is_active = False
        order.save()
        return Response({"detail" : "Deactive successful"})
