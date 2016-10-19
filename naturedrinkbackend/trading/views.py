from .models import PaymentMethod , ItemProperty , Order , ItemLine , PostalTrack
from .serializers import PaymentMethodSerializer, ItemPropertySerializer,OrderSerializer,ItemLineSerializer,PostalTrackSerializer
from rest_framework import viewsets,renderers,status
from rest_framework.response import Response
from rest_framework.decorators import list_route,detail_route

PERMISSION_DENIED_CONTENT = { "detail" : "Permission denied."}

# Create your views here.
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
