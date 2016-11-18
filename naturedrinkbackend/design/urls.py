from django.conf.urls import url,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'design',views.DesignBottleViewSet)
router.register(r'bottle',views.BottleViewSet)
router.register(r'logo',views.LogoViewSet)
router.register(r'banner',views.BannerViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
