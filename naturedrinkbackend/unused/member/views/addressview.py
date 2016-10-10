from rest_framework.response import Response
from rest_framework import viewsets
from ..serializers import AddressSerializer
from ..models import Address
from permissions.permissions import IsOwnerOrIsAdmin

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes  = (IsOwnerOrIsAdmin,)
    def create(self,request) :
        address = Address.objects.create(user=request.user,address=request.data['address'],village=request.data['village'],road=request.data['road'],sub_district=request.data['sub_district'],district=request.data['district'],province=request.data['province'],country=request.data['country'],zipcode=request.data['zipcode'])
        address.save()
        return Response(AddressSerializer(address).data)
    def list(self,request) :
        if request.user.is_superuser :
            return super(AddressViewSet,self).list(request)
        addresses = Address.objects.filter(user=request.user)
        return Response(AddressSerializer(addresses,many=True).data)
