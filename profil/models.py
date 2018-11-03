from django.db import models
from django.contrib.auth.models import AbstractUser
from model_utils.models import TimeStampedModel

# Create your models here.

  japanese_address = models.OneToOneField(
      'product.JapaneseAddress', on_delete=models.PROTECT, null=True, blank=True, related_name='user_jp_adr')
  japanese_billing_address = models.OneToOneField(
      'product.JapaneseAddress', on_delete=models.PROTECT, null=True, blank=True, related_name='user_jp_bill_adr')
  hungarian_address = models.OneToOneField(
      'product.HungarianAddress', on_delete=models.PROTECT, null=True, blank=True, related_name='user_hu_adr')
  hungarian_billing_address = models.OneToOneField(
      'product.HungarianAddress', on_delete=models.PROTECT, null=True, blank=True, related_name='user_hu_bill_adr')

class User(AbstractUser, TimeStampedModel):
  other_name = models.TextField()
  
  profile_image = models.ImageField(blank=True)

  def __str__(self):
    return '%s %s' % (self.last_name, self.first_name)
