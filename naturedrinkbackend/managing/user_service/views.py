from django.contrib.auth.models import User
from user.models import Address
from .serializers import UserSerializer,AddressSerializer
from ..permissions import isAdmin
from rest_framework import viewsets,renderers
from rest_framework.decorators import detail_route
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet) :
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (isAdmin,)
    def destroy(self,request,pk=None) :
        user = User.objects.get(id=pk)
        user.is_active = False
        user.save()
        return Response({"detail" : "Deactive successful"})

    @detail_route(methods=['put'],renderer_classes=[renderers.JSONRenderer])
    def reactive(self,request,pk=None) :
        user = User.objects.get(id=pk)
        user.is_active = True
        user.save()
        return Response({"detail" : "Reactive successful"})

    @detail_route(methods=['put'],renderer_classes=[renderers.JSONRenderer])
    def assign_staff(self,request,pk=None):
        user = User.objects.get(id=pk)
        user.is_staff = True
        user.save()
        return Response({"detail" : "Staff Assigned!"})

    @detail_route(methods=['put'],renderer_classes=[renderers.JSONRenderer])
    def fire_staff(self,request,pk=None):
        user = User.objects.get(id=pk)
        user.is_staff = False
        user.save()
        return Response({"detail" : "Staff Fire!"})

class AddressViewSet(viewsets.ModelViewSet) :
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = (isAdmin,)
