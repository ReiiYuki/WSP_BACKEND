from .models import PaymentMethod , ItemProperty , Order , ItemLine , PostalTrack
from .serializers import PaymentMethodSerializer, ItemPropertySerializer,OrderSerializer,ItemLineSerializer,PostalTrackSerializer
from rest_framework import viewsets,renderers,status
from rest_framework.response import Response
from rest_framework.decorators import list_route,detail_route
from user.models import Address
from datetime import date
import requests
PERMISSION_DENIED_CONTENT = { "detail" : "Permission denied."}

# Create your views here.
''' Get OK '''
class PaymentMethodViewSet(viewsets.ModelViewSet) :
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer

    ''' List OK '''
    def list(self,request) :
        # if request.user.is_staff :
        #     return super(PaymentMethodViewSet,self).list(request)
        return Response(PaymentMethodSerializer(PaymentMethod.objects.filter(is_active=True),many=True).data)

    ''' Create OK '''
    def create(self,request) :
        # if request.user.is_staff :
        #     return super(PaymentMethodViewSet,self).create(request)
        return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)

    ''' Update OK '''
    def update(self,request,pk=None) :
        # if request.user.is_staff :
        #     return super(PaymentMethodViewSet,self).update(request)
        return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)

    ''' Deactive OK '''
    def destroy(self,request,pk=None) :
        # if request.user.is_staff :
        #     method = PaymentMethod.objects.get(id=pk)
        #     method.is_active = False
        #     method.save()
        #     return Response({"detail" : "Deactive successful"})
        return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)

    ''' Reactive OK '''
    @detail_route(methods=['put'],renderer_classes=[renderers.JSONRenderer])
    def reactive(self,request,pk=None) :
        # if request.user.is_staff :
        #     method = PaymentMethod.objects.get(id=pk)
        #     method.is_active = True
        #     method.save()
        #     return Response({"detail" : "Reactive successful"})
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



class ItemPropertyViewSet(viewsets.ModelViewSet) :
    queryset = ItemProperty.objects.all()
    serializer_class = ItemPropertySerializer
    ''' Create OK '''
    def create(self,request) :
        if request.user.is_anonymous :
            return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)
        return super(ItemPropertyViewSet,self).create(request)

    def update(self,request) :
        return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)

    def destroy(self,request,pk=None) :
        return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)

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

    # def upload_slip(self,request,pk=None) :
    #     if request.user.is_anonymous :
    #         return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)
    #     order = Order.objects.get(id=pk)
    #     order.is_paid = True
    #     order.pay_date = date.today()
    #     order.transfer_slip = request.FILES['slip']
    #     return Response(OrderSerializer(order).data)

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

    def status(self,request,pk=None) :
        order = Order.objects.get(id=pk)
        if order.transfer_slip == None :
            return "Wait for slip"
        if order.is_paid and not order.is_shipped:
            return "Upload Recieved"
        if order.is_shipped :
            header = {"aftership-api-key": "9442c41d-f380-482e-954c-2a1c996f1815","Content-Type": "application/json"}
            url = "https://api.aftership.com/v4/last_checkpoint/thailand-post/"+order.postal_track
            data = requests.get(url,header).json()
            status = data['data']['tag']+' '+data['data']['checkpoint']['city']+','+data['data']['checkpoint']['country_name']
            return status


class PostalTrackViewSet(viewsets.ModelViewSet) :
    queryset = PostalTrack.objects.all()
    serializer_class = PostalTrackSerializer
