import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel

from address.models import AddressField
from shop.models import Sale, Campaign
from order.models import Order

class ProductCategory(TimeStampedModel):

  name = models.CharField(max_length=50, unique=True)
  description = models.CharField(max_length=300, blank=True)

  def __str__(self):
    return self.name


class ProductStorageLocation(TimeStampedModel):
  address = AddressField(on_delete=models.PROTECT)

  def __str__(self):
    return '%s' % self.address


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
