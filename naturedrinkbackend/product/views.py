from django.shortcuts import render
from .models import Category
from .serializers import CategorySerializer
from rest_framework import viewsets,renderers,status
from rest_framework.response import Response
from rest_framework.decorators import list_route,detail_route

# Create your views here.
PERMISSION_DENIED_CONTENT = { "detail" : "Permission denied."}

'''Get and List OK '''
class CategoryViewSet(viewsets.ModelViewSet) :
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    ''' Add (create) OK'''
    def create(self,request) :
        if request.user.is_staff :
            return super(CategoryViewSet,self).create(request)
        return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)

    ''' Edit (update) OK '''
    def update(self,request,pk=None) :
        if request.user.is_staff :
            return super(CategoryViewSet,self).update(request,pk)
        return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)
