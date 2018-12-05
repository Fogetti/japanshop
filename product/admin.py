from django.contrib.admin.widgets import AdminFileWidget
from django.utils.translation import ugettext_lazy as _
from django.forms import TextInput, Textarea
from django.utils.html import format_html
from django.contrib import admin
from django.db import models

from product.models import Product
from product.models import ProductPrice
from product.models import ProductStatus
from product.models import ProductCategory
from product.models import JapaneseAddress
from product.models import HungarianAddress
from product.models import ProductStorageLocation

class AdminImageWidget(AdminFileWidget):
  def render(self, name, value, attrs=None, renderer=None, **_kwargs):
    output = []
    if value and getattr(value, "url", None):
      image_url = value.url
      file_name = str(value)
      output.append(u' <a href="%s" target="_blank"><img src="%s" alt="%s" style="max-width: 100&#37;;height: auto;"/></a> %s ' %
                    (image_url, image_url, file_name, _('Change:')))
    output.append(super().render(name, value, attrs))
    return format_html(u''.join(output))


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
      models.ImageField: {'widget': AdminImageWidget},
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
