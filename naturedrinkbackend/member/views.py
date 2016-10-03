from rest_framework.response import Response
from rest_framework import viewsets,status,renderers
from .serializers import UserSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import list_route

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, pk=None):
        if request.user.is_anonymous :
            content = {'ERROR_MESSEGE': 'User is unauthorized.'}
            return Response(content,status=status.HTTP_401_UNAUTHORIZED)
        if pk=='0':
            return Response(UserSerializer(request.user,
                context={'request':request}).data)
        return super(UserViewSet, self).retrieve(request, pk)

    @list_route(methods=['post'],renderer_classes=[renderers.JSONRenderer])
    def change_password(self,request) :
        if request.user.is_anonymous :
            content = {'ERROR_MESSEGE': 'User is unauthorized.'}
            return Response(content,status=status.HTTP_401_UNAUTHORIZED)
        password = request.data['password']
        new_password = request.data['new_password']
        user = authenticate(username=request.user.username,password=password)
        if user is not None :
            user.set_password(new_password)
            user.save()
            return Response(UserSerializer(request.user,
                context={'request':request}).data)
        content = {'ERROR_MESSEGE': 'Password is wrong.'}
        return Response(content,status=status.HTTP_401_UNAUTHORIZED)
