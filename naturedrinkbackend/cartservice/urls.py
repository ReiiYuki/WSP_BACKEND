from django.conf.urls import url,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'cart',views.CartViewSet)
router.register(r'paymentmethod',views.PaymentMethodViewSet)
urlpatterns = [
    url(r'^', include(router.urls)),
]
