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
router.register(r'design',views.DesignBottleViewSet)
router.register(r'bottle',views.BottleViewSet)
router.register(r'banner',views.BannerViewSet)
router.register(r'logo',views.LogoViewSet)
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^stat/product',views.stat_product),
    url(r'^stat/category',views.stat_category),
    url(r'^stat/money',views.stat_money),
    url(r'^stat/user/payment',views.stat_user_pay),
    url(r'^stat/user/order',views.stat_user_order),
    url(r'^stat/user/shipping',views.stat_user_shipping),
    url(r'^stat/address',views.stat_address),

]
