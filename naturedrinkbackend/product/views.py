from django.shortcuts import render
from .models import Category,Product,ProductOption,ProductChoice
from .serializers import CategorySerializer,ProductSerializer
from rest_framework import viewsets,renderers,status
from rest_framework.response import Response
from rest_framework.decorators import list_route,detail_route

# Create your views here.
PERMISSION_DENIED_CONTENT = { "detail" : "Permission denied."}

'''Get OK'''
class CategoryViewSet(viewsets.ModelViewSet) :
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    ''' Add (create) OK'''
    def create(self,request) :
        if request.user.is_staff :
            return super(CategoryViewSet,self).create(request)
        return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)

    ''' List OK '''
    def list(self,request) :
        if request.user.is_staff :
            return super(CategoryViewSet,self).list(request)
        return Response(CategorySerializer(Category.objects.filter(is_active=True),many=True).data)

    ''' Edit (update) OK '''
    def update(self,request,pk=None) :
        if request.user.is_staff :
            return super(CategoryViewSet,self).update(request,pk)
        return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)

    ''' Deactive (destroy) OK '''
    def destroy(self,request,pk=None) :
        if request.user.is_staff :
            category = Category.objects.get(id=pk)
            category.is_active = False
            category.save()
            return Response({"detail" : "Deactive successful"})
        return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)

    ''' Reactive OK '''
    @detail_route(methods=['put'],renderer_classes=[renderers.JSONRenderer])
    def reactive(self,request,pk=None) :
        if request.user.is_staff :
            category = Category.objects.get(id=pk)
            category.is_active = True
            category.save()
            return super(CategoryViewSet,self).retrieve(request,pk)
        return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)

''' Get OK '''
class ProductViewSet(viewsets.ModelViewSet) :
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    ''' Create OK '''
    def create(self,request) :
        if request.user.is_staff :
            product = Product(name=request.data['name'],category=Category.objects.get(id=request.data['category']),description=request.data['description'],price=request.data['price'])
            product.save()
            options =  request.data['options']
            for op in options :
                option = ProductOption(name=op['name'],product=product)
                option.save()
                for ch in op['choices'] :
                    choice = ProductChoice(name=ch['name'],option=option)
                    choice.save()
            return Response(ProductSerializer(product).data)
        return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)

    ''' List OK '''
    def list(self,request) :
        if request.user.is_staff :
            return super(ProductViewSet,self).list(request)
        return Response(ProductSerializer(Product.objects.filter(is_active=True),many=True).data)

    ''' Edit (update) OK '''
    def update(self,request,pk=None) :
        if request.user.is_staff :
            return super(ProductViewSet,self).update(request,pk)
        return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)

    ''' Deactive (destroy) OK '''
    def destroy(self,request,pk=None) :
        if request.user.is_staff :
            product = Product.objects.get(id=pk)
            product.is_active = False
            product.save()
            return Response({"detail" : "Deactive successful"})
        return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)

    ''' Reactive OK '''
    @detail_route(methods=['put'],renderer_classes=[renderers.JSONRenderer])
    def reactive(self,request,pk=None) :
        if request.user.is_staff :
            product = Product.objects.get(id=pk)
            product.is_active = True
            product.save()
            return super(ProductViewSet,self).retrieve(request,pk)
        return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)
