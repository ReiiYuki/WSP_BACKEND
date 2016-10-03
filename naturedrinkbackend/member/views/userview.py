from rest_framework.response import Response
from rest_framework import viewsets,status,renderers
from ..serializers import UserSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.decorators import list_route
from utility.utility import anonymous

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, pk=None):
        anonymous(request)
        if pk=='0':
            return Response(UserSerializer(request.user,
                context={'request':request}).data)
        return super(UserViewSet, self).retrieve(request, pk)

    @list_route(methods=['put'],renderer_classes=[renderers.JSONRenderer])
    def change_password(self,request) :
        anonymous(request)
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

    @list_route(methods=['put'],renderer_classes=[renderers.JSONRenderer])
    def edit_info(self,request) :
        anonymous(request)
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        email = request.data['email']
        request.user.first_name = first_name
        request.user.last_name = last_name
        request.user.email = email
        request.user.save()
        return Response(UserSerializer(request.user,
            context={'request':request}).data)
