from django.contrib.auth.models import User
from user.models import Address
from .serializers import UserSerializer,AddressSerializer
from ..permissions import isAdmin
from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet) :
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (isAdmin,)

class AddressViewSet(viewsets.ModelViewSet) :
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = (isAdmin,)
