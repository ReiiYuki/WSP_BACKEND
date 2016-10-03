from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import UserSerializer
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import detail_route
from rest_framework import status


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, pk=None):
        if not request.user.is_anonymous :
            if pk=='0':
                return Response(UserSerializer(request.user,
                    context={'request':request}).data)
            return super(UserViewSet, self).retrieve(request, pk)
        content = {'ERROR_MESSEGE': 'User is unauthorized.'}
        return Response(content,status=status.HTTP_401_UNAUTHORIZED)

    # @login_required
    @detail_route(methods=['post'])
    def change_password(self,request) :
        print (request.user)
        return Response(UserSerializer(request.user,
            context={'request':request}).data)
