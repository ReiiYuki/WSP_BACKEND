from rest_framework.response import Response
from rest_framework import viewsets
from .models import Category,Product
from .serializers import CategorySerializer,ProductSerializer
from .permissions import AdminOrReadOnly

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet) :
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes  = (AdminOrReadOnly,)

class ProductViewSet(viewsets.ModelViewSet) :
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes  = (AdminOrReadOnly,)
