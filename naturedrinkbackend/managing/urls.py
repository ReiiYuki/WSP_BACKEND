from django.conf.urls import url,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user',views.UserViewSet)
router.register(r'address',views.AddressViewSet)
router.register(r'product',views.ProductViewSet)
router.register(r'category',views.CategoryViewSet)
router.register(r'item_line',views.ItemLineViewSet)
router.register(r'method',views.PaymentMethodViewSet)
router.register(r'order',views.OrderViewSet)
urlpatterns = [
    url(r'^', include(router.urls)),
]
