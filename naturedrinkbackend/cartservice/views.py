from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import CartItemLineSerializer, ItemPropertySerializer
from .models import ItemLine , ItemProperty
# Create your views here.
class CartViewSet(viewsets.ModelViewSet) :
    queryset = ItemLine.objects.filter(order=None)
    serializer_class = CartItemLineSerializer

    def list(self,request) :
        return Response(CartItemLineSerializer(ItemLine.objects.filter(order=None,user=request.user),many=True).data)

    # def create(self,request) :
    #
