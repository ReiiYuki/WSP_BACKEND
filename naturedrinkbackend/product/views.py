from rest_framework.response import Response
from rest_framework import viewsets
from .models import Category,Product
from .serializers import CategorySerializer,ProductSerializer

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet) :
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet) :
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
