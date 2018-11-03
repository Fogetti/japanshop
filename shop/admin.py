from django.contrib import admin

from product.models import Product
from shop.models import Sale, Campaign

# Register your models here.
class SaleProductInline(admin.TabularInline):
    model = Sale.products.through
    verbose_name = u"Product"
    verbose_name_plural = u"Products"


class SaleAdmin(admin.ModelAdmin):
  exclude = ('products',)
  inlines = (
      SaleProductInline,
  )
  list_display = ('start_date_time', 'period', 'description')


class CampaignProductInline(admin.TabularInline):
    model = Campaign.products.through
    verbose_name = u"Product"
    verbose_name_plural = u"Products"


class CampaignAdmin(admin.ModelAdmin):
  exclude = ('products',)
  inlines = (
      CampaignProductInline,
  )
  list_display = ('start_date_time', 'period', 'description')


admin.site.register(Sale, SaleAdmin)
admin.site.register(Campaign, CampaignAdmin)
