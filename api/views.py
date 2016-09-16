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

    ''' Login
        1. Get request data
        2. Authenticate is user existed with this username and password
        3. Check is it None
        3.1 if not None Login this user and response "S" for succesing login
        3.2 if None response "F" for Fail to Client
    '''
    @list_route(methods=['post'], url_path='login')
    def login(self, request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        if user is not None :
            login(request,user)
            if request.user.is_authenticated() :
                print ('%s is logged in to server...'%request.user.username)
                return HttpResponse("S", content_type="text/plain")
        return HttpResponse("F", content_type="text/plain")

    # # @login_required
    # @list_route(methods=['put'],url_path='change-password')
    # def change_password(self,request) :
    #     print (request.user)
    #     # old_password = request.data['old_password']
    #     # new_password = request.data['new_password']
    #     # user = authenticate(username=request.user.username,password=old_password)
    #     # if user is not None :
    #     #     user.set_password(new_password)
    #     #     user.save()
    #     #     login(user)
    #     #     if request.user.is_authenticated() :
    #     #         print ('%s is succesing changing password in to server...'%request.user.username)
    #     #         return HttpResponse("S", content_type="text/plain")
    #     return HttpResponse("F", content_type="text/plain")
