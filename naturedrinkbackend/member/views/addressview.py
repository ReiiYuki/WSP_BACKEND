from rest_framework.response import Response
from rest_framework import viewsets
from ..serializers import AddressSerializer
from ..models import Address
from ..permissions import IsOwnerOrIsAdmin

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes  = (IsOwnerOrIsAdmin,)

    def list(self,request) :
        if request.user.is_superuser :
            return super(AddressViewSet,self).list(request)
        addresses = Address.objects.filter(user=request.user)
        return Response(AddressSerializer(addresses,many=True).data)
