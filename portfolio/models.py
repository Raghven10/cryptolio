import django.utils.timezone
from django.db import models

# Create your models here.
class Asset(models.Model):
    date_of_purchase = models.DateTimeField(default=django.utils.timezone.now())
    exchange_name = models.CharField(max_length=255)
    token_name = models.CharField(max_length=255)
    buy_rate = models.FloatField(default=0.0)
    quantity = models.FloatField(default=0.0)
    sale_rate = models.FloatField(default=0.0)
    date_of_sale = models.DateTimeField(default=django.utils.timezone.now())
    modified_by = models.CharField(max_length=255)
    modified_on = models.DateTimeField(default=django.utils.timezone.now())


class User(models.Model):
    fName = models.CharField(max_length=255)
    lName = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    modified_by = models.CharField(max_length=255, default='admin')
    modified_on = models.DateTimeField(default=django.utils.timezone.now())