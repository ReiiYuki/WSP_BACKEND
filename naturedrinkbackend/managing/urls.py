from django.conf.urls import url,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user',views.UserViewSet)
router.register(r'address',views.AddressViewSet)
urlpatterns = [
    url(r'^', include(router.urls)),
]
