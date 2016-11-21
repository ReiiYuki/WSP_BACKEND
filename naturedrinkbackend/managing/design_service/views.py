from design.models import DesignBottle,Bottle,Logo,Banner
from .serializers import DesignBottleSerializer,LogoSerializer,BannerSerializer,BottleSerializer
from rest_framework import viewsets,renderers,status
from rest_framework.response import Response
from rest_framework.decorators import list_route,detail_route
from ..permissions import isAdmin
from product.models import Product
from trading.models import ItemLine

PERMISSION_DENIED_CONTENT = { "detail" : "Permission denied."}

class BottleViewSet(viewsets.ModelViewSet) :
    queryset = Bottle.objects.all()
    serializer_class = BottleSerializer
    permission_classes = (isAdmin,)

    def destroy(self,request,pk=None) :
        bottle = Bottle.objects.get(id=pk)
        bottle.is_active = False
        bottle.save()
        return Response(BottleSerializer(bottle).data)

    @detail_route(methods=['put'],renderer_classes=[renderers.JSONRenderer])
    def reactive(self,request,pk=None) :
        bottle = Bottle.objects.get(id=pk)
        bottle.is_active = True
        bottle.save()
        return Response(BottleSerializer(bottle).data)

class BannerViewSet(viewsets.ModelViewSet) :
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    permission_classes = (isAdmin,)

    def destroy(self,request,pk=None) :
        banner = Banner.objects.get(id=pk)
        banner.is_active = False
        banner.save()
        return Response(BannerSerializer(banner).data)

    @detail_route(methods=['put'],renderer_classes=[renderers.JSONRenderer])
    def reactive(self,request,pk=None) :
        banner = Banner.objects.get(id=pk)
        banner.is_active = True
        banner.save()
        return Response(BannerSerializer(banner).data)

class LogoViewSet(viewsets.ModelViewSet) :
    queryset = Logo.objects.all()
    serializer_class = LogoSerializer
    permission_classes = (isAdmin,)
    def destroy(self,request,pk=None) :
        logo = Logo.objects.get(id=pk)
        logo.is_active = False
        logo.save()
        return Response(LogoSerializer(logo).data)

    @detail_route(methods=['put'],renderer_classes=[renderers.JSONRenderer])
    def reactive(self,request,pk=None) :
        logo = Logo.objects.get(id=pk)
        logo.is_active = True
        logo.save()
        return Response(LogoSerializer(logo).data)

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
        product = Product.objects.create(name=design.name,description=design.description,price=float(price),image=design.image,design=design)
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
        itemLine.delete()
        product.delete()
        return Response({"status":"Deconfirm Success"})
