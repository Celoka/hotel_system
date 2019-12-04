import uuid

from django.db import models
from django.conf import settings

# Create your models here.

class reservation(models.Model):
    """
    This model defines a hotel object
    """

    hotel_name = models.CharField(max_length=50, blank=True)
