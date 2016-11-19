from .user_service.views import UserViewSet,AddressViewSet
from .product_service.views import ProductViewSet,CategoryViewSet
from .cart_service.views import ItemLineViewSet,PaymentMethodViewSet
from .order_service.views import OrderViewSet
from .design_service.views import DesignBottleViewSet,BottleViewSet,LogoViewSet,BannerViewSet
from .statistic_service.views import stat_product,stat_category,stat_money,stat_user_pay,stat_user_order,stat_user_shipping,stat_address
