import uuid
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel

# Create your models here.
class ProductStorageLocation(TimeStampedModel):

  def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
    if (self.japanese_address and self.hungarian_address):
      raise ValidationError('There must be only one address defined')
    return super().save(force_insert, force_update, using, update_fields)

  class Meta:
    verbose_name = _('Product storage location')
    verbose_name_plural = _('Product storage locations')

  def __str__(self):
    return '%s' % self.address


class HungarianAddress(TimeStampedModel):
  city = models.TextField(_('city'), help_text=_('The type of munacipility e.g. city, village, etc'))
  street_name = models.TextField(_('street name'))
  street_type = models.TextField(_('street type'))
  house_number = models.TextField(_('house number'))  # [FLOOR] [APARTMENT]
  postal_code = models.TextField(_('recipient'))
  country = models.TextField(_('country'))

  storage_location = models.OneToOneField(
      ProductStorageLocation,
      on_delete=models.CASCADE,
      related_name='hungarian_address',
      verbose_name=_('storage_location')
    )

  class Meta:
    verbose_name = _('Hungarian address')
    verbose_name_plural = _('Hungarian addresses')
  
  def __str__(self):
    return '%s %s %s %s' % (self.postal_code, self.city, self.street_name, self.house_number)


class JapaneseAddress(TimeStampedModel):
  building = models.TextField(_('building'),
    help_text=_('The name of the building'))
  apartment = models.TextField(_('apartment'),
    help_text=_('Room number'))
  chome = models.TextField(_('chome'),
    help_text=_('The first number in the triplet ◯町目◯番◯号'))
  ban = models.TextField(_('ban'),
    help_text=_('The second number in the triplet ◯町目◯番◯号'))
  go = models.TextField(_('go'),
    help_text=_('The third number in the triplet ◯町目◯番◯号'))
  ward = models.TextField(_('ward'),
    help_text=_('Ward or island'))  # [ISLAND]
  city = models.TextField(_('city'))
  prefecture = models.TextField(_('prefecture'))
  postal_code = models.TextField(_('postal code'))
  country = models.TextField(_('country'))
  p_o_box = models.TextField(_('P.O. box'))
  
  storage_location = models.OneToOneField(
      ProductStorageLocation,
      on_delete=models.CASCADE,
      related_name='japanese_address',
      verbose_name=_('storage_location')
    )

  class Meta:
    verbose_name = _('Japanese address')
    verbose_name_plural = _('Japanese addresses')

  def __str__(self):
    return '%s %s %s %s %s' % (self.postal_code, self.city, self.chome, self.ban, self.go)


class ProductCategory(TimeStampedModel):
  name = models.CharField(_('name'), max_length=50, unique=True)
  description = models.CharField(_('description'), max_length=300, blank=True)

  class Meta:
    verbose_name = _('Product category')
    verbose_name_plural = _('Product categories')

  def __str__(self):
    return self.name


class Product(TimeStampedModel):

  id = models.UUIDField(
    primary_key=True,
    default=uuid.uuid4,
    editable=False,
    db_index=True
  )

  category = models.ForeignKey(
    ProductCategory,
    on_delete=models.SET_NULL,
    null=True,
    related_name='products',
    verbose_name=_('category')
  )

  name = models.CharField(_('name'), max_length=300)

  description = models.TextField(_('description'), blank=True)

  image1 = models.ImageField(_('image1'), blank=True)
  image2 = models.ImageField(_('image2'), blank=True)
  image3 = models.ImageField(_('image3'), blank=True)
  image4 = models.ImageField(_('image4'), blank=True)

  class Meta:
    verbose_name = _('Product')
    verbose_name_plural = _('Products')

  def __str__(self):
    return self.name


class ProductOrder(TimeStampedModel):
  product = models.ForeignKey(
      Product, on_delete=models.CASCADE, verbose_name=_('product'))
  order = models.ForeignKey(
      'order.Order', on_delete=models.CASCADE, verbose_name=_('order'))
  product_quantity = models.IntegerField(_('product quantity'))

  class Meta:
    unique_together = ('product', 'order',)


class ProductSale(TimeStampedModel):
  product = models.ForeignKey(
      Product, on_delete=models.CASCADE, verbose_name=_('product'))
  sale = models.ForeignKey(
      'shop.Sale', on_delete=models.CASCADE, verbose_name=_('sale'))
  remaining_quantity = models.IntegerField(_('remaining quantity'))

  class Meta:
    unique_together = ('product', 'sale',)


class ProductCampaign(TimeStampedModel):
  product = models.ForeignKey(
      Product, on_delete=models.CASCADE, verbose_name=_('product'))
  campaign = models.ForeignKey(
      'shop.Campaign', on_delete=models.CASCADE, verbose_name=_('campaign'))
  remaining_quantity = models.IntegerField(_('remaining quantity'))

  class Meta:
    unique_together = ('product', 'campaign',)


class ProductStatus(TimeStampedModel):
  IN_STOCK = 'IS'
  OUT_OF_STOCK = 'OOS'

  STOCK_CHOICES = (
      (IN_STOCK, _('In Stock')),
      (OUT_OF_STOCK, _('Out of Stock')),
  )

  in_stock = models.CharField(
      _('in stock'),
      choices=STOCK_CHOICES,
      default=IN_STOCK,
      max_length=3
  )

  product = models.OneToOneField(
      Product,
      on_delete=models.CASCADE,
      verbose_name=_('product')
  )

  product_location = models.ForeignKey(
      ProductStorageLocation,
      on_delete=models.CASCADE,
      verbose_name=_('product_location')
  )

  class Meta:
    unique_together = ('product', 'product_location')
    verbose_name = _('Product status')
    verbose_name_plural = _('Product status')

  def __str__(self):
    return '%s' % self.get_in_stock_display()
  

class ProductPrice(TimeStampedModel):
  HUF = 'HUF'
  USD = 'USD'
  JPY = 'JPY'

  CURRENCY_CHOICES = (
      (HUF, _('Hungarian Forint')),
      (USD, _('US Dollar')),
      (JPY, _('Japanese Yen')),
  )

  currency = models.CharField(
      _('currency'),
      choices=CURRENCY_CHOICES,
      default=HUF,
      max_length=3
  )

  price = models.IntegerField(_('price'))

  product = models.OneToOneField(
      Product,
      on_delete=models.CASCADE,
      verbose_name=_('product')
  )

  class Meta:
    unique_together = ('product', 'currency')
    verbose_name = _('Product price')
    verbose_name_plural = _('Product price')

  def __str__(self):
    return '%s [%s]' % (self.price, self.get_currency_display())
