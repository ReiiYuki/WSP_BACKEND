from django.conf.urls import url,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'cart',views.CartViewSet)
router.register(r'paymentmethod',views.PaymentMethodViewSet)
router.register(r'order',views.OrderViewSet)
urlpatterns = [
    url(r'^', include(router.urls)),
]
