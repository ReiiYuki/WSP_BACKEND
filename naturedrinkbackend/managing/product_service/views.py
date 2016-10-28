from product.models import Product,Category
from ..permissions import isAdmin
from .serializers import CategorySerializer,ProductSerializer
from rest_framework import viewsets,renderers
from rest_framework.decorators import detail_route
from rest_framework.response import Response


class ProductViewSet(viewsets.ModelViewSet) :
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (isAdmin,)
    def destroy(self,request,pk=None) :
        product = Product.objects.get(id=pk)
        product.is_active = False
        product.save()
        return Response({"detail" : "Deactive successful"})

    @detail_route(methods=['put'],renderer_classes=[renderers.JSONRenderer])
    def reactive(self,request,pk=None) :
        product = Product.objects.get(id=pk)
        product.is_active = True
        product.save()
        return Response({"detail" : "Reactive successful"})

class CategoryViewSet(viewsets.ModelViewSet) :
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (isAdmin,)
    def destroy(self,request,pk=None) :
        category = Category.objects.get(id=pk)
        category.is_active = False
        category.save()
        return Response({"detail" : "Deactive successful"})

    @detail_route(methods=['put'],renderer_classes=[renderers.JSONRenderer])
    def reactive(self,request,pk=None) :
        category = Category.objects.get(id=pk)
        category.is_active = True
        category.save()
        return Response({"detail" : "Reactive successful"})
