from design.models import DesignBottle
from .serializers import DesignBottleSerializer
from rest_framework import viewsets,renderers,status
from rest_framework.response import Response
from rest_framework.decorators import list_route,detail_route
from ..permissions import isAdmin
from product.models import Product
from trading.models import ItemLine

PERMISSION_DENIED_CONTENT = { "detail" : "Permission denied."}

class DesignBottleViewSet(viewsets.ModelViewSet) :
    queryset = DesignBottle.objects.all()
    serializer_class = DesignBottleSerializer
    permission_classes = (isAdmin,)

    @detail_route(methods=['put'],renderer_classes=[renderers.JSONRenderer])
    def confirm(self,request,pk=None) :
        price = request.data['price']
        design = DesignBottle.objects.get(id=pk)
        design.is_confirm = True
        design.save()
        product = Product.objects.create(name=design.name,description=design.description,price=price,image=design.image,design=design)
        product.save()
        return Response(DesignBottleSerializer(design).data)

    @detail_route(methods=['put'],renderer_classes=[renderers.JSONRenderer])
    def confirm(self,request,pk=None) :
        price = request.data['price']
        design = DesignBottle.objects.get(id=pk)
        design.is_confirm = True
        design.save()
        product = Product.objects.create(name=design.name,description=design.description,price=price,image=design.image,design=design)
        product.save()
        user = design.user
        itemLine = ItemLine.objects.create(user=user,product=product,quantity=1)
        itemLine.save()
        return Response(DesignBottleSerializer(design).data)

    @detail_route(methods=['put'],renderer_classes=[renderers.JSONRenderer])
    def deconfirm(self,request,pk=None) :
        design = DesignBottle.objects.get(id=pk)
        design.is_confirm = False
        design.save()
        product = Product.objects.get(design=design)
        itemLine= ItemLine.objects.get(product=product,user=design.user)
        itemLine.remove()
        product.remove()
        return Response({"status":"Deconfirm Success"})
