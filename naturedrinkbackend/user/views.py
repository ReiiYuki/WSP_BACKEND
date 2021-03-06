from django.shortcuts import render
from .models import Address
from .serializers import UserSerializer,AddressSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets,renderers,status
from rest_framework.response import Response
from rest_framework.decorators import list_route,detail_route
from django.contrib.auth import authenticate

PERMISSION_DENIED_CONTENT = { "detail" : "Permission denied."}
''' Register OK (create)'''
class UserViewSet(viewsets.ModelViewSet) :
    queryset = User.objects.all()
    serializer_class = UserSerializer

    '''List Ok '''
    def list(self,request) :
        return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)

    '''User Detail OK'''
    def retrieve(self, request, pk=None):
        if not request.user.is_anonymous :
            if pk=='0' or pk==str(request.user.id):
                return Response(UserSerializer(request.user).data)
        return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)

    ''' Change password OK '''
    @list_route(methods=['put'],renderer_classes=[renderers.JSONRenderer])
    def change_password(self,request) :
        password = request.data['password']
        new_password = request.data['new_password']
        user = authenticate(username=request.user.username,password=password)
        if user is not None :
            user.set_password(new_password)
            user.save()
            return Response(UserSerializer(request.user).data)
        content = {'detail': 'Password is wrong.'}
        return Response(content,status=status.HTTP_401_UNAUTHORIZED)

    '''Edit OK '''
    @detail_route(methods=['put'],renderer_classes=[renderers.JSONRenderer])
    def edit(self,request,pk=None) :
        if not request.user.is_anonymous :
            if pk==str(request.user.id):
                request.user.first_name = request.data['first_name']
                request.user.last_name = request.data['last_name']
                request.user.email = request.data['email']
                request.user.save()
                return super(UserViewSet, self).retrieve(request,request.user.id)
        return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)

    ''' Delete (destroy) OK '''
    def destroy(self,request,pk=None) :
        return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)

    @list_route(renderer_classes=[renderers.JSONRenderer])
    def is_admin(self,request) :
        if request.user.is_staff :
            return Response({"detail":"True"})
        return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)


class AddressViewSet(viewsets.ModelViewSet) :
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    ''' List OK '''
    def list(self,request) :
        if request.user.is_anonymous :
            return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)
        return Response(AddressSerializer(Address.objects.filter(user=request.user,is_active=True),many=True).data)

    ''' Create OK '''
    def create(self,request) :
        if request.user.is_anonymous :
            return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)
        return super(AddressViewSet,self).create(request)

    ''' Get OK '''
    def retrieve(self,request,pk=None) :
        address = Address.objects.filter(id=pk)
        if len(address)==0 or request.user.is_staff or address[0].user == request.user :
            return super(AddressViewSet,self).retrieve(request,pk)
        return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)

    ''' Update OK '''
    def update(self,request,pk=None) :
        address = Address.objects.filter(id=pk)
        if len(address)==0 or request.user.is_staff or address[0].user == request.user  :
            return super(AddressViewSet,self).update(request,pk)
        return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)

    ''' Deactive OK '''
    def destroy(self,request,pk=None) :
        address = Address.objects.filter(id=pk)
        if len(address)==0 or request.user.is_staff or address[0].user == request.user :
            address.is_active = False
            address.save()
            return Response({"detail" : "Deactive successful"})
        return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
