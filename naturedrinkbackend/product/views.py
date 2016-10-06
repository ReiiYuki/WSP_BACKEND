from rest_framework.response import Response
from rest_framework import viewsets,renderers
from .models import Category,Product,ProductOption,ProductChoice
from .serializers import CategorySerializer,ProductSerializer,ProductOptionSerializer,ProductChoiceSerializer
from .permissions import AdminOrReadOnly
from rest_framework.decorators import detail_route

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet) :
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes  = (AdminOrReadOnly,)

    @detail_route(renderer_classes=[renderers.JSONRenderer])
    def product(self,request,pk=None) :
        category = Category.objects.get(id=pk)
        return Response(ProductSerializer(Product.objects.filter(category=category),many=True).data)

class ProductViewSet(viewsets.ModelViewSet) :
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes  = (AdminOrReadOnly,)

class ProductOptionViewSet(viewsets.ModelViewSet) :
    queryset = ProductOption.objects.all()
    serializer_class = ProductOptionSerializer
    permission_classes = (AdminOrReadOnly,)

class ProductOptionViewSet(viewsets.ModelViewSet) :
    queryset = ProductChoice.objects.all()
    serializer_class = ProductChoiceSerializer
    permission_classes = (AdminOrReadOnly,)
