import django_filters

from .models import Product


class NullFilter(django_filters.BooleanFilter):
  """Filter on a field set as null or not."""

  def filter(self, qs, value):
    if value is not None:
      return qs.filter(**{'%s__isnull' % self.field_name: value})
    return qs


class ProductFilter(django_filters.FilterSet):

  uncategorized = NullFilter(field_name='category')
  created_min = django_filters.DateFilter(
    field_name='created',
    lookup_expr='gte'
  )
  created_max = django_filters.DateFilter(
    field_name='created',
    lookup_expr='lte'
  )

  class Meta:
    model = Product
    fields = ('category', 'created_min', 'created_max', )
