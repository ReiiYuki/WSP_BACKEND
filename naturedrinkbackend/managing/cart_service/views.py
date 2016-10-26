from trading.models import ItemLine,PaymentMethod
from ..permissions import isAdmin
from .serializers import ItemLineSerializer,PaymentMethodSerializer
from rest_framework import viewsets

class ItemLineViewSet(viewsets.ModelViewSet) :
    queryset = ItemLine.objects.all()
    serializer_class = ItemLineSerializer
    permission_classes = (isAdmin,)

class PaymentMethodViewSet(viewsets.ModelViewSet) :
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
    permission_classes = (isAdmin,)
