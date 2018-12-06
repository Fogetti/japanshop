from local import settings

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
  image1 = serializers.SerializerMethodField(source='get_image1')
  image2 = serializers.SerializerMethodField(source='get_image2')
  image3 = serializers.SerializerMethodField(source='get_image3')
  image4 = serializers.SerializerMethodField(source='get_image4')

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

  def get_host(self, request):
    http = 'http'
    if request.is_secure():
      http = 'https'
    domain = settings.SERVER_NAME + ':' + str(settings.SERVER_PORT)
    return http + '://' + domain
  
  def get_image1(self, product):
    request = self.context.get('request')
    if product.image1:
      image1_url = product.image1.url
      return self.get_host(request)+image1_url
    return None
    
  def get_image2(self, product):
    request = self.context.get('request')
    if product.image2:
      image2_url = product.image2.url
      return self.get_host(request)+image2_url
    return None
    
  def get_image3(self, product):
    request = self.context.get('request')
    if product.image3:
      image3_url = product.image3.url
      return self.get_host(request)+image3_url
    return None
    
  def get_image4(self, product):
    request = self.context.get('request')
    if product.image4:
      image4_url = product.image4.url
      return self.get_host(request)+image4_url
    return None
    
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
      'japanese_address',
      'hungarian_address',
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
      'product',
      'product_location',
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
      'product',
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
