from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Product
from .models import ProductCategory
from .models import ProductStorageLocation
from .models import ProductStatus
from .models import ProductPrice

class ProductSerializer(serializers.ModelSerializer):

  category = serializers.SlugRelatedField(
    slug_field='name',
    required=False,
    queryset=ProductCategory.objects.all()
  )
  links = serializers.SerializerMethodField(source='get_links')

  class Meta:
    model = Product
    fields = (
      'id',
      'category',
      'name',
      'description',
      'image1',
      'image2',
      'image3',
      'image4',
      'links',
    )
  
  def get_links(self, obj):
    request = self.context['request']
    links = {
      'self': reverse(
        'product-detail',
        kwargs={'pk': obj.pk},
        request=request
      ),
      'category': None,
    }
    if obj.category:
      links['category'] = reverse(
        'productcategory-detail',
        kwargs={'name': obj.category.name},
        request=request
      )
    return links


class ProductCategorySerializer(serializers.ModelSerializer):

  links = serializers.SerializerMethodField(source='get_links')

  class Meta:
    model = ProductCategory
    fields = (
      'id',
      'name',
      'description',
      'links',
    )
  
  def get_links(self, obj):
    request = self.context['request']
    return {
      'self': reverse(
        'productcategory-detail',
        kwargs={'name': obj.name},
        request=request
      ),
      'products': reverse(
        'product-list',
        request=request
      ) + '?category={}'.format(obj.name),
    }

class ProductStorageLocationSerializer(serializers.ModelSerializer):

  links = serializers.SerializerMethodField(source='get_links')

  class Meta:
    model = ProductStorageLocation
    fields = (
      'id',
      'address',
      'links',
    )
  
  def get_links(self, obj):
    request = self.context['request']
    return {
      'self': reverse(
        'productlocation-detail',
        kwargs={'id': obj.id},
        request=request
      ),
    }

class ProductStatusSerializer(serializers.ModelSerializer):

  links = serializers.SerializerMethodField(source='get_links')

  class Meta:
    model = ProductStatus
    fields = (
      'id',
      'in_stock',
      'links',
    )
  
  def get_links(self, obj):
    request = self.context['request']
    return {
      'self': reverse(
        'productstatus-detail',
        kwargs={'id': obj.id},
        request=request
      ),
    }

class ProductPriceSerializer(serializers.ModelSerializer):

  links = serializers.SerializerMethodField(source='get_links')

  class Meta:
    model = ProductPrice
    fields = (
      'id',
      'currency',
      'price',
      'links',
    )
  
  def get_links(self, obj):
    request = self.context['request']
    return {
      'self': reverse(
        'productprice-detail',
        kwargs={'id': obj.id},
        request=request
      ),
    }
