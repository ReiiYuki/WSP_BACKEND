from product.models import Product,Category
from ..permissions import isAdmin
from .serializers import CategorySerializer,ProductSerializer
from rest_framework import viewsets

class ProductViewSet(viewsets.ModelViewSet) :
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (isAdmin,)

class CategoryViewSet(viewsets.ModelViewSet) :
    queryset = Category.objects.all()
    serializer_class = CategoryViewSet
    permission_classes = (isAdmin,)
