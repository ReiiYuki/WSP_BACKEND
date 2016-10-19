from django.conf.urls import url,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'method',views.PaymentMethodViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
