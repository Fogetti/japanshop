import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel

from shop.models import Sale, Campaign
from order.models import Order

class ProductCategory(TimeStampedModel):

  name = models.CharField(max_length=50, unique=True)
  description = models.CharField(max_length=300, blank=True)

  def __str__(self):
    return self.name


class ProductStorageLocation(TimeStampedModel):
class HungarianAddress(TimeStampedModel):
  city = models.TextField(_('city'), help_text=_('The type of munacipility e.g. city, village, etc'))
  street_name = models.TextField(_('street name'))
  street_type = models.TextField(_('street type'))
  house_number = models.TextField(_('house number'))  # [FLOOR] [APARTMENT]
  postal_code = models.TextField(_('recipient'))
  country = models.TextField(_('country'))

  storage_location = models.OneToOneField(
      ProductStorageLocation, on_delete=models.CASCADE, related_name='hungarian_address')

  class Meta:
    verbose_name = _('Hungarian address')
    verbose_name_plural = _('Hungarian addresses')
  
  def __str__(self):
    return '%s' % self.address
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
      ProductStorageLocation, on_delete=models.CASCADE, related_name='japanese_address')

  class Meta:
    verbose_name = _('Japanese address')
    verbose_name_plural = _('Japanese addresses')

  def __str__(self):
    return '%s %s %s %s %s' % (self.postal_code, self.city, self.chome, self.ban, self.go)




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
    related_name='products'
  )

  name = models.CharField(max_length=300)

  description = models.TextField(blank=True)

  image1 = models.ImageField(blank=True)
  image2 = models.ImageField(blank=True)
  image3 = models.ImageField(blank=True)
  image4 = models.ImageField(blank=True)

  def __str__(self):
    return self.name


class ProductOrder(TimeStampedModel):
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  order = models.ForeignKey(Order, on_delete=models.CASCADE)
  product_quantity = models.IntegerField()

  class Meta:
    unique_together = ('product', 'order',)


class ProductSale(TimeStampedModel):
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
  remaining_quantity = models.IntegerField()

  class Meta:
    unique_together = ('product', 'sale',)


class ProductCampaign(TimeStampedModel):
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
  remaining_quantity = models.IntegerField()

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
      choices=STOCK_CHOICES,
      default=IN_STOCK,
      max_length=3
  )

  product = models.ForeignKey(
      Product,
      on_delete=models.CASCADE
  )

  product_location = models.ForeignKey(
      ProductStorageLocation,
      on_delete=models.CASCADE
  )

  def __str__(self):
    return '%s' % self.get_in_stock_display()
  
  class Meta:
    unique_together = ('product', 'product_location')


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
      choices=CURRENCY_CHOICES,
      default=HUF,
      max_length=3
  )

  price = models.IntegerField()

  product = models.ForeignKey(
      Product,
      on_delete=models.CASCADE
  )

  def __str__(self):
    return '%s [%s]' % (self.price, self.get_currency_display())

  class Meta:
    unique_together = ('product', 'currency')
