from django.conf.urls import url,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'product', views.ProductViewSet)
router.register(r'category', views.CategoryViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
