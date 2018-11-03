from django.contrib import admin

from product.models import Product
from order.models import Order

# Register your models here.
class ProductInline(admin.TabularInline):
    model = Order.products.through
    verbose_name = u"Product"
    verbose_name_plural = u"Products"


class OrderAdmin(admin.ModelAdmin):
  exclude = ('products',)
  inlines = (
      ProductInline,
  )
  list_display = ('remarks', 'assigned')


admin.site.register(Order, OrderAdmin)
