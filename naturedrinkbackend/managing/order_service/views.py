from trading.models import Order
from ..permissions import isAdmin
from .serializers import OrderSerializer
from rest_framework import viewsets
from rest_framework.decorators import detail_route
class OrderViewSet(viewsets.ModelViewSet) :
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (isAdmin,)
