from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset= User.objects.all()
    serializer_class  = UserSerializer
# Create your views here.
def index(request):
    customer = User.objects.create_user('jodasdsaddddhnadsdsadsdasdassdaa', 'lennon@thebeatles.com', 'johnpassword',first_name='John',last_name='Lenon')
    print (customer.first_name,customer.last_name,customer.email,customer.password)

    return HttpResponse("Test API")
