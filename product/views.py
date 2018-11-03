from rest_framework import authentication, permissions, viewsets, filters
import django_filters.rest_framework

from .models import Product
from .models import ProductCategory
from .models import ProductStorageLocation
from .models import ProductStatus
from .models import ProductPrice
from .serializers import ProductSerializer
from .serializers import ProductCategorySerializer
from .serializers import ProductStorageLocationSerializer
from .serializers import ProductStatusSerializer
from .serializers import ProductPriceSerializer
from .filters import ProductFilter

class DefaultsMixin(object):
  """Default settings for view authentication, permissions, filtering and pagination."""
  authentication_classes = (
    authentication.BasicAuthentication,
    authentication.TokenAuthentication,
  )
  permission_classes = (
    permissions.IsAuthenticated,
  )
  paginate_by = 25
  paginate_by_param = 'page_size'
  max_paginate_by = 100

  filter_backends = (
    django_filters.rest_framework.DjangoFilterBackend,
    filters.SearchFilter,
    filters.OrderingFilter,
  )


class ProductViewSet(DefaultsMixin, viewsets.ModelViewSet):
  """ API endpoint for listing and creating products """

  queryset = Product.objects.order_by('name')
  serializer_class = ProductSerializer
  filter_class = ProductFilter
  search_fields = ('name', 'description', )
  ordering_fields = ('name', 'category', )


class ProductCategoryViewSet(DefaultsMixin, viewsets.ModelViewSet):
  """ API endpoint for listing and creating product categories """

  lookup_field = 'name'
  lookup_url_kwarg = 'name'
  queryset = ProductCategory.objects.order_by('name')
  serializer_class = ProductCategorySerializer
  search_fields = ('name', 'description', )
  ordering_fields = ('name', )

class ProductStorageLocationViewSet(DefaultsMixin, viewsets.ModelViewSet):
  """ API endpoint for listing and creating product storage locations """

  lookup_field = 'id'
  lookup_url_kwarg = 'id'
  queryset = ProductStorageLocation.objects.order_by('japanese_address')
  serializer_class = ProductStorageLocationSerializer
  search_fields = ('japanese_address', 'hungarian_address')
  ordering_fields = ('japanese_address', 'hungarian_address')

class ProductStatusViewSet(DefaultsMixin, viewsets.ModelViewSet):
  """ API endpoint for listing and creating product statuses """

  lookup_field = 'id'
  lookup_url_kwarg = 'id'
  queryset = ProductStatus.objects.order_by('in_stock')
  serializer_class = ProductStatusSerializer
  search_fields = ('in_stock', )
  ordering_fields = ('in_stock', )

class ProductPriceViewSet(DefaultsMixin, viewsets.ModelViewSet):
  """ API endpoint for listing and creating product prices """

  lookup_field = 'id'
  lookup_url_kwarg = 'id'
  queryset = ProductPrice.objects.order_by('price')
  serializer_class = ProductPriceSerializer
  search_fields = ('product', 'currency', 'price', )
  ordering_fields = ('product', 'price', )
