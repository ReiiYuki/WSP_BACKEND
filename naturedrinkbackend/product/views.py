from django.shortcuts import render
from .models import Category
from .serializers import CategorySerializer
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
