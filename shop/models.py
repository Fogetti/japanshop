from model_utils.models import TimeStampedModel
from django.db import models

class Sale(TimeStampedModel):
  start_date_time = models.DateTimeField()
  period = models.DurationField()
  description = models.TextField()

  def __str__(self):
    return '%s [%s]' % (self.description, self.start_date_time)

class Campaign(TimeStampedModel):
  start_date_time = models.DateTimeField()
  period = models.DurationField()
  description = models.TextField()

  def __str__(self):
    return '%s [%s]' % (self.description, self.start_date_time)