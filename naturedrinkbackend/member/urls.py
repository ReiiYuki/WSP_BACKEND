from django.conf.urls import url,include
from .views import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from django.views.decorators.csrf import csrf_exempt

router = DefaultRouter()
router.register(r'detail', views.UserViewSet)
router.register(r'address',views.AddressViewSet)
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^login/$', csrf_exempt(obtain_auth_token))
]
