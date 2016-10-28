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
    def destroy(self,request,pk=None) :
        method = PaymentMethod.objects.get(id=pk)
        method.is_active = False
        method.save()
        return Response({"detail" : "Deactive successful"})

    @detail_route(methods=['put'],renderer_classes=[renderers.JSONRenderer])
    def reactive(self,request,pk=None) :
        method = PaymentMethod.objects.get(id=pk)
        method.is_active = True
        method.save()
        return Response({"detail" : "Reactive successful"})
