from .models import DesignBottle,Bottle,Banner,Logo
from .serializers import DesignBottleSerializer,BottleSerializer,BannerSerializer,LogoSerializer
from rest_framework import viewsets,renderers,status
from rest_framework.response import Response
from rest_framework.decorators import list_route,detail_route

PERMISSION_DENIED_CONTENT = { "detail" : "Permission denied."}

class BottleViewSet(viewsets.ReadOnlyModelViewSet) :
    queryset = Bottle.objects.filter(is_active=True)
    serializer_class = BottleSerializer

class BannerViewSet(viewsets.ReadOnlyModelViewSet) :
    queryset = Banner.objects.filter(is_active=True)
    serializer_class = BannerSerializer

class LogoViewSet(viewsets.ReadOnlyModelViewSet) :
    queryset = Logo.objects.filter(is_active=True)
    serializer_class = LogoSerializer

class DesignBottleViewSet(viewsets.ModelViewSet) :
    queryset = DesignBottle.objects.all()
    serializer_class = DesignBottleSerializer

    def list(self,request) :
        if request.user.is_anonymous :
             return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)
        return Response(DesignBottleSerializer(DesignBottle.objects.filter(user=request.user,is_active=True),many=True).data)

    def retrieve(self,request,pk=None) :
        design = DesignBottle.objects.get(id=pk)
        if request.user  is not design.user and design.is_active:
             return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)
        return Response(DesignBottleSerializer(design).data)

    def update(self,request,pk=None) :
        return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)

    def destroy(self,request,pk=None) :
        design = DesignBottle.objects.get(id=pk)
        if request.user is not design.user :
             return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)
        design.is_active = False
        design.save()
        return Response(DesignBottleSerializer(design).data)

    @detail_route(methods=['put'],renderer_classes=[renderers.JSONRenderer])
    def submit(self,request,pk=None) :
        design = DesignBottle.objects.get(id=pk)
        if request.user  is not design.user :
             return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)
        design.is_request = True
        design.save()
        return Response(DesignBottleSerializer(design).data)

    @detail_route(methods=['put'],renderer_classes=[renderers.JSONRenderer])
    def desubmit(self,request,pk=None) :
        design = DesignBottle.objects.get(id=pk)
        if request.user  is not design.user :
             return Response(PERMISSION_DENIED_CONTENT,status=status.HTTP_401_UNAUTHORIZED)
        design.is_request = False
        design.is_confirm = False
        design.save()
        return Response(DesignBottleSerializer(design).data)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
