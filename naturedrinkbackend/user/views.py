from django.shortcuts import render
from .models import Address
from .serializers import UserSerializer,AddressSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets,renderers
from rest_framework.response import Response
from rest_framework.decorators import list_route
from .permissions import IsOwnerOrIsAdmin

# Create your views here.
class UserViewSet(viewsets.ModelViewSet) :
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes  = ()

    def retrieve(self, request, pk=None):
        if pk=='0':
            return Response(UserSerializer(request.user,
                context={'request':request}).data)
        return super(UserViewSet, self).retrieve(request, pk)

    @list_route(methods=['put'],renderer_classes=[renderers.JSONRenderer])
    def change_password(self,request) :
        password = request.data['password']
        new_password = request.data['new_password']
        user = authenticate(username=request.user.username,password=password)
        if user is not None :
            user.set_password(new_password)
            user.save()
            return Response(UserSerializer(request.user,
                context={'request':request}).data)
        content = {'detail': 'Password is wrong.'}
        return Response(content,status=status.HTTP_401_UNAUTHORIZED)

    def delete(self,request,pk=None) :
        user = User.objects.get(id=pk)
        user.is_active = False
        user.save()
        return self.delete(request,pk)

class AddressViewSet(viewsets.ModelViewSet) :
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    # permission_classes = ()

    def delete(self,request,pk=None) :
        address = Address.objects.get(id=pk)
        address.is_active = False
        address.save()
        return self.delete(request,pk)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
