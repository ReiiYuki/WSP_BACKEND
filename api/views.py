from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer
from rest_framework.decorators import list_route
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

class UserViewSet(viewsets.ModelViewSet):
    queryset= User.objects.all()
    serializer_class  = UserSerializer
    @list_route(methods=['post'], url_path='login')
    def login(self, request):
        print (request.data)
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        if user is not None :
            login(request,user)
            if request.user.is_authenticated() :
                print ('%s is logged in to server...')
                return HttpResponse("S", content_type="text/plain")
        return HttpResponse("F", content_type="text/plain")
