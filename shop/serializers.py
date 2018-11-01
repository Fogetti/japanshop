from rest_framework import serializers
from rest_framework.reverse import reverse

from product.models import ProductCampaign
from product.models import ProductSale
from product.models import Product
from .models import Campaign
from .models import Sale

class ProductSaleSerializer(serializers.HyperlinkedModelSerializer):
  id = serializers.ReadOnlyField(source='product.id')
  name = serializers.ReadOnlyField(source='product.name')

  class Meta:
    model = ProductSale
    fields = ('id', 'name', 'remaining_quantity', )


class SaleSerializer(serializers.ModelSerializer):
  links = serializers.SerializerMethodField(source='get_links')
  # products = ProductSaleSerializer(source='ProductSale_set', many=True)
  products = serializers.PrimaryKeyRelatedField(
    queryset=Product.objects.all(), many=True)

  class Meta:
    model = Sale
    fields = (
      'id',
      'start_date_time',
      'period',
      'description',
      'products',
      'links',
    )

  def get_links(self, obj):
    request = self.context['request']
    links = {
      'self': reverse(
        'sale-detail',
        kwargs={'pk': obj.pk},
        request=request
      ),
    }
    return links


class ProductCampaignSerializer(serializers.HyperlinkedModelSerializer):
  id = serializers.ReadOnlyField(source='product.id')
  name = serializers.ReadOnlyField(source='product.name')

  class Meta:
    model = ProductCampaign
    fields = ('id', 'name', 'remaining_quantity', )


class CampaignSerializer(serializers.ModelSerializer):
  links = serializers.SerializerMethodField(source='get_links')
  # products = ProductCampaignSerializer(source='ProductCampaign_set', many=True)
  products = serializers.PrimaryKeyRelatedField(
    queryset=Product.objects.all(), many=True)

  class Meta:
    model = Campaign
    fields = (
      'id',
      'start_date_time',
      'period',
      'description',
      'products',
      'links',
    )

  def get_links(self, obj):
    request = self.context['request']
    links = {
      'self': reverse(
        'campaign-detail',
        kwargs={'pk': obj.pk},
        request=request
      ),
    }
    return links
