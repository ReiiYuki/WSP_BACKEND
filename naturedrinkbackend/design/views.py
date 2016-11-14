from .models import DesignBottle, DesignRequest
from .serializers import DesignBottleSerializer,DesignRequestSerializer
from rest_framework import viewsets,renderers,status
from rest_framework.response import Response
from rest_framework.decorators import list_route,detail_route

PERMISSION_DENIED_CONTENT = { "detail" : "Permission denied."}

class DesignBottleViewSet(viewsets.ModelViewSet) :
    queryset = DesignBottle.objects.all()
    serializer_class = DesignBottleSerializer
    
