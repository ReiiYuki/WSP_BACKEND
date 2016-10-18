from django.conf.urls import url,include
from . import views
from rest_framework.routers import DefaultRouter
from django.views.decorators.csrf import csrf_exempt
from rest_framework_expiring_authtoken.views import obtain_expiring_auth_token

router = DefaultRouter()
router.register(r'user',views.UserViewSet)
router.register(r'address',views.AddressViewSet)
'''Login OK '''
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^login/$', csrf_exempt(obtain_expiring_auth_token))
]
