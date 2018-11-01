from rest_framework import authentication, permissions, viewsets, filters
from django.shortcuts import render

from product.views import DefaultsMixin

from .models import Order
from .serializers import OrderSerializer

# Create your views here.
class OrderViewSet(DefaultsMixin, viewsets.ModelViewSet):
  """ API endpoint for listing and creating order """

  queryset = Order.objects.order_by('assigned')
  serializer_class = OrderSerializer
  search_fields = ('notes', 'assigned', )
  ordering_fields = ('notes', 'assigned', )
