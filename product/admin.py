from django.forms import TextInput, Textarea
from django.contrib import admin
from django.db import models

from product.models import Product
from product.models import ProductPrice
from product.models import ProductStatus
from product.models import ProductCategory
from product.models import JapaneseAddress
from product.models import HungarianAddress
from product.models import ProductStorageLocation

# Register your models here.
class ProductPriceInline(admin.TabularInline):
  model = ProductPrice


class ProductStatusInline(admin.TabularInline):
  model = ProductStatus


class ProductAdmin(admin.ModelAdmin):
  inlines = (
      ProductPriceInline,
      ProductStatusInline,
  )
  list_display = ('category', 'name', 'description', 'image1', 'image2', 'image3', 'image4', )
  formfield_overrides = {
      models.CharField: {'widget': TextInput(attrs={'size':'20'})},
      models.TextField: {'widget': Textarea(attrs={'rows':3, 'cols':60})},
  }


class JapaneseAddressInline(admin.StackedInline):
  model = JapaneseAddress
  formfield_overrides = {
      models.CharField: {'widget': TextInput(attrs={'size':'20'})},
      models.TextField: {'widget': Textarea(attrs={'rows':3, 'cols':60})},
  }


class HungarianAddressInline(admin.StackedInline):
  model = HungarianAddress
  formfield_overrides = {
      models.CharField: {'widget': TextInput(attrs={'size':'20'})},
      models.TextField: {'widget': Textarea(attrs={'rows':3, 'cols':60})},
  }


class ProductStorageLocationAdmin(admin.ModelAdmin):
  inlines = (
    JapaneseAddressInline,
    HungarianAddressInline,
  )
  formfield_overrides = {
      models.CharField: {'widget': TextInput(attrs={'size':'20'})},
      models.TextField: {'widget': Textarea(attrs={'rows':3, 'cols':60})},
  }

admin.site.register(ProductCategory)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductStorageLocation, ProductStorageLocationAdmin)
