from .models import PaymentMethod , ItemProperty , Order , ItemLine , PostalTrack
from .serializers import PaymentMethodSerializer, ItemPropertySerializer,OrderSerializer,ItemLineSerializer,PostalTrackSerializer
from rest_framework import viewsets,renderers,status
from rest_framework.response import Response
from rest_framework.decorators import list_route,detail_route

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
