from django.contrib.auth.models import User
from user.models import Address
from .serializers import UserSerializer
from ..permissions import isAdmin
from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet) :
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (isAdmin,)
