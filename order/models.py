from config import settings

from django.db import models
from model_utils.models import TimeStampedModel

# Create your models here.
class Order(TimeStampedModel):
  notes = models.TextField(null=True, blank=True)
  assigned = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
  products = models.ManyToManyField(
    'product.Product', blank=True, through='product.ProductOrder', related_name='ordered_products')

  def __str__(self):
    return '%s' % self.notes
