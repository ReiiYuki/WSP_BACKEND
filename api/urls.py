from django.conf.urls import url,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^$',views.index)
]
