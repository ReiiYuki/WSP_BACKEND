from django.conf.urls import url,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'method',views.PaymentMethodViewSet)
router.register(r'cart',views.ItemLineViewSet)
router.register(r'property',views.ItemPropertyViewSet)
router.register(r'order',views.OrderViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
