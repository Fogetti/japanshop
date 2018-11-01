from model_utils.models import TimeStampedModel
from django.db import models

class Sale(TimeStampedModel):
  start_date_time = models.DateTimeField()
  period = models.DurationField()
  description = models.TextField()
  products = models.ManyToManyField(
    'product.Product', blank=True, through='product.ProductSale', related_name='sale_products')

  def __str__(self):
    return '%s [%s]' % (self.description, self.start_date_time)

class Campaign(TimeStampedModel):
  start_date_time = models.DateTimeField()
  period = models.DurationField()
  description = models.TextField()
  products = models.ManyToManyField(
    'product.Product', blank=True, through='product.ProductCampaign', related_name='campaign_products')

  def __str__(self):
    return '%s [%s]' % (self.description, self.start_date_time)
