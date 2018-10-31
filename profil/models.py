from django.db import models
from django.contrib.auth.models import AbstractUser
from model_utils.models import TimeStampedModel
from address.models import AddressField

# Create your models here.


class User(AbstractUser, TimeStampedModel):
  other_name = models.TextField()
  
  profile_image = models.ImageField(blank=True)
  address = AddressField(on_delete=models.PROTECT, null=True, blank=True, related_name='user_address')
  billing_address = AddressField(on_delete=models.PROTECT, null=True, blank=True, related_name='user_billing_address')

  def __str__(self):
    return '%s %s' % (self.last_name, self.first_name)
