from config import settings
from django.db import models
from model_utils.models import TimeStampedModel
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Order(TimeStampedModel):
  remarks = models.TextField(_('remarks'), null=True, blank=True)
  assigned = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    null=True,
    blank=True,
    verbose_name=_('assigned')
  )
  products = models.ManyToManyField(
    'product.Product',
    blank=True,
    through='product.ProductOrder',
    related_name='ordered_products',
    verbose_name=_('products')
  )

  class Meta:
    verbose_name = _('Order')
    verbose_name_plural = _('Orders')

  def __str__(self):
    return '%s' % self.remarks
