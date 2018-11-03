from django.db import models
from model_utils.models import TimeStampedModel
from django.utils.translation import ugettext_lazy as _

class Sale(TimeStampedModel):
  start_date_time = models.DateTimeField(_('start date and time'))
  period = models.DurationField(_('period'))
  description = models.TextField(_('description'))
  products = models.ManyToManyField(
    'product.Product', blank=True, through='product.ProductSale', related_name='sale_products', verbose_name=_('products'))

  class Meta:
    verbose_name = _('Sale')
    verbose_name_plural = _('Sales')

  def __str__(self):
    return '%s [%s]' % (self.description, self.start_date_time)

class Campaign(TimeStampedModel):
  start_date_time = models.DateTimeField(_('start date and time'))
  period = models.DurationField(_('period'))
  description = models.TextField(_('description'))
  products = models.ManyToManyField(
    'product.Product', blank=True, through='product.ProductCampaign', related_name='campaign_products', verbose_name=_('products'))

  class Meta:
    verbose_name = _('Campaign')
    verbose_name_plural = _('Campaign')

  def __str__(self):
    return '%s [%s]' % (self.description, self.start_date_time)
