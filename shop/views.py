from rest_framework import authentication, permissions, viewsets, filters
from django.shortcuts import render

from product.views import DefaultsMixin

from .models import Sale
from .models import Campaign
from .serializers import SaleSerializer
from .serializers import CampaignSerializer

# Create your views here.
class SaleViewSet(DefaultsMixin, viewsets.ModelViewSet):
  """ API endpoint for listing and creating sales """

  queryset = Sale.objects.order_by('start_date_time')
  serializer_class = SaleSerializer
  search_fields = ('start_date_time', 'description', )
  ordering_fields = ('start_date_time', 'description', )

class CampaignViewSet(DefaultsMixin, viewsets.ModelViewSet):
  """ API endpoint for listing and creating campaigns """

  queryset = Campaign.objects.order_by('start_date_time')
  serializer_class = CampaignSerializer
  search_fields = ('start_date_time', 'description', )
  ordering_fields = ('start_date_time', 'description', )
