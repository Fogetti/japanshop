from rest_framework import serializers
from rest_framework.reverse import reverse

from product.models import ProductOrder
from product.models import Product
from .models import Order

class ProductOrderSerializer(serializers.HyperlinkedModelSerializer):
  id = serializers.ReadOnlyField(source='product.id')
  name = serializers.ReadOnlyField(source='product.name')

  class Meta:
      model = ProductOrder

      fields = ('id', 'name', 'product_quantity', )

class OrderSerializer(serializers.ModelSerializer):
  links = serializers.SerializerMethodField(source='get_links')
  # products = ProductOrderSerializer(source='productorder_set', many=True)
  products = serializers.PrimaryKeyRelatedField(
      queryset=Product.objects.all(), many=True)

  class Meta:
    model = Order
    fields = (
      'id',
      'notes',
      'assigned',
      'products',
      'links',
    )
  
  def get_links(self, obj):
    request = self.context['request']
    links = {
      'self': reverse(
        'order-detail',
        kwargs={'pk': obj.pk},
        request=request
      ),
    }
    return links

