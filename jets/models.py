from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Jets(models.Model):
  name = models.CharField(max_length=64)
  country_origin = models.CharField(max_length=64)
  description = models.TextField(default='')
  engine_count = models.IntegerField()
  added_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  added = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name