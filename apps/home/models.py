# -*- encoding: utf-8 -*-


from django.db import models
from django.contrib.auth.models import User


class Asset(models.Model):     
    orderDate = models.DateTimeField()
    exchange = models.CharField(max_length=20)
    token = models.CharField(max_length=20)
    tradeType = models.CharField(max_length=20)
    leverage = models.IntegerField()
    entryPrice = models.FloatField()
    totalQuantity = models.FloatField()
    exitPrice = models.FloatField(blank=True, null=True)
    lastUpdatedOn = models.DateTimeField()
    lastUpdatedBy = models.CharField(max_length=20)

    
