from rest_framework.response import Response
from rest_framework import viewsets,status
from ..serializers import AddressSerializer
from ..models import Address
from ..permissions import IsOwnerOrReadOnly
from utility.utility import anonymous

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permissions = [IsOwnerOrReadOnly]

    def list(self,request) :
        anonymous(request)
        addresses = Address.objects.filter(user=request.user)
        return Response(AddressSerializer(addresses,many=True).data)

    def update(self,request,pk=None) :
        anonymous(request)
        if self.get_object().user == request.user :
            return super(AddressViewSet, self).update(request, pk)
        content = {'ERROR_MESSEGE': 'User is unauthorized.'}
        return Response(content,status=status.HTTP_401_UNAUTHORIZED)

    def retrieve(self,request,pk=None) :
        anonymous(request)
        if self.get_object().user == request.user :
            return super(AddressViewSet, self).retrieve(request, pk)
        content = {'ERROR_MESSEGE': 'User is unauthorized.'}
        return Response(content,status=status.HTTP_401_UNAUTHORIZED)

    def destroy(self,request,pk=None) :
        anonymous(request)
        if self.get_object().user == request.user :
            return super(AddressViewSet, self).destroy(request, pk)
        content = {'ERROR_MESSEGE': 'User is unauthorized.'}
        return Response(content,status=status.HTTP_401_UNAUTHORIZED)
