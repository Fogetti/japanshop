from django.db import models
from model_utils.models import TimeStampedModel
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class User(AbstractUser, TimeStampedModel):
  other_name = models.TextField(_('other name'))
  profile_image = models.ImageField(_('profile image'), blank=True)

  japanese_address = models.OneToOneField(
      'product.JapaneseAddress',
      on_delete=models.PROTECT,
      null=True,
      blank=True,
      related_name='user_jp_adr',
      verbose_name=_('japanese_address')
    )
  japanese_billing_address = models.OneToOneField(
      'product.JapaneseAddress',
      on_delete=models.PROTECT,
      null=True,
      blank=True,
      related_name='user_jp_bill_adr',
      verbose_name=_('japanese_billing_address')
    )
  hungarian_address = models.OneToOneField(
      'product.HungarianAddress',
      on_delete=models.PROTECT,
      null=True,
      blank=True,
      related_name='user_hu_adr',
      verbose_name=_('hungarian_address')
    )
  hungarian_billing_address = models.OneToOneField(
      'product.HungarianAddress',
      on_delete=models.PROTECT,
      null=True,
      blank=True,
      related_name='user_hu_bill_adr',
      verbose_name=_('hungarian_billing_address')
    )

  class Meta:
    verbose_name = _('User')
    verbose_name_plural = _('Users')

  def __str__(self):
    return '%s %s' % (self.last_name, self.first_name)
