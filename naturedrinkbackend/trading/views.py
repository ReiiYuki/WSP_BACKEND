from .models import PaymentMethod , ItemProperty , Order , ItemLine , PostalTrack
from .serializers import PaymentMethodSerializer, ItemPropertySerializer,OrderSerializer,ItemLineSerializer,PostalTrackSerializer
from rest_framework import viewsets,renderers,status
from rest_framework.response import Response
from rest_framework.decorators import list_route,detail_route
from user.models import Address
from datetime import date
PERMISSION_DENIED_CONTENT = { "detail" : "Permission denied."}

# Create your views here.
''' Get OK '''
class PaymentMethodViewSet(viewsets.ModelViewSet) :
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer

    ''' List OK '''
    def list(self,request) :
        if request.user.is_staff :
            return super(PaymentMethodViewSet,self).list(request)
        return Response(PaymentMethodSerializer(PaymentMethod.objects.filter(is_active=True)).data)

    ''' Create OK '''
    def create(self,request) :
        if request.user.is_staff :
            return super(PaymentMethodViewSet,self).create(request)
        return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)

    ''' Update OK '''
    def update(self,request,pk=None) :
        if request.user.is_staff :
            return super(PaymentMethodViewSet,self).update(request)
        return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)

    ''' Deactive OK '''
    def destroy(self,request,pk=None) :
        if request.user.is_staff :
            method = PaymentMethod.objects.get(id=pk)
            method.is_active = False
            method.save()
            return Response({"detail" : "Deactive successful"})
        return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)

    ''' Reactive OK '''
    @detail_route(methods=['put'],renderer_classes=[renderers.JSONRenderer])
    def reactive(self,request,pk=None) :
        if request.user.is_staff :
            method = PaymentMethod.objects.get(id=pk)
            method.is_active = True
            method.save()
            return Response({"detail" : "Reactive successful"})
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
        cart_item =  ItemLine.objects.filter(user=request.user)
        for i in cart_item :
            i.order = order
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

    def destroy(self,request,pk=None) :
        if request.user.is_anonymous :
            return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)
        order = Order.objects.get(id=pk)
        order.is_active = False
        order.save()
        return Response({"detail" : "Deactive successful"})

class PostalTrackViewSet(viewsets.ModelViewSet) :
    queryset = PostalTrack.objects.all()
    serializer_class = PostalTrackSerializer
