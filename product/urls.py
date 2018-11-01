from rest_framework.routers import DefaultRouter

from profil.views import UserViewSet
from order.views import OrderViewSet
from shop.views import CampaignViewSet
from shop.views import SaleViewSet
from .views import ProductViewSet
from .views import ProductCategoryViewSet
from .views import ProductPriceViewSet
from .views import ProductStatusViewSet
from .views import ProductStorageLocationViewSet


router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'profile', UserViewSet)
router.register(r'categories', ProductCategoryViewSet)
router.register(r'prices', ProductPriceViewSet)
router.register(r'statuses', ProductStatusViewSet)
router.register(r'storagelocations', ProductStorageLocationViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'sales', SaleViewSet)
router.register(r'campaigns', CampaignViewSet)
