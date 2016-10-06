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

    def retrieve(self,request,pk=None) :
        category = Category.objects.get(id=pk)
        content = CategorySerializer(category).data
        content['products'] = ProductSerializer(Product.objects.filter(category=category),many=True).data
        return Response(content)

class ProductViewSet(viewsets.ModelViewSet) :
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes  = (AdminOrReadOnly,)

    def create(self,request) :
        name = request.data['name']
        detail = request.data['detail']
        category = Category.objects.get(id=request.data['category'])
        price = request.data['price']
        product = Product.objects.create(name=name,detail=detail,category=category,price=price)
        options = request.data['options']
        for op in options :
            name = op['name']
            option = ProductOption.objects.create(name=name,product=product)
            choices = op['choices']
            for choice in choices :
                name = choice['name']
                choice = ProductChoice.objects.create(name=name,option=option)
        return self.retrieve(request,pk=product.id)

    def retrieve(self,request,pk=None) :
        product = Product.objects.get(id=pk)
        options = ProductOption.objects.filter(product=product)
        content = ProductSerializer(product).data
        content["options"] = ProductOptionSerializer(options,many=True).data
        counter = 0
        for op in options :
            choices = ProductChoice.objects.filter(option=op)
            content["options"][counter]["choices"] = ProductChoiceSerializer(choices,many=True).data
            counter+=1
        return Response(content)

class ProductOptionViewSet(viewsets.ModelViewSet) :
    queryset = ProductOption.objects.all()
    serializer_class = ProductOptionSerializer
    permission_classes = (AdminOrReadOnly,)

class ProductChoiceViewSet(viewsets.ModelViewSet) :
    queryset = ProductChoice.objects.all()
    serializer_class = ProductChoiceSerializer
    permission_classes = (AdminOrReadOnly,)
