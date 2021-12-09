# -*- encoding: utf-8 -*-


from django.db import models
from django.contrib.auth.models import User


class Asset(models.Model):  
    user = models.ForeignKey(User, on_delete = models.CASCADE)   
    orderDate = models.DateTimeField(auto_now_add = True) 
    exchange = models.CharField(max_length=20)   
    token = models.CharField(max_length=20)
    tradeType = models.CharField(max_length=20)
    leverage = models.IntegerField()
    entryPrice = models.FloatField()      
    totalQuantity = models.FloatField(blank=True, null=True)
    tradeSize = models.FloatField(blank=True, null=True)
    exitPrice = models.FloatField(blank=True, null=True)
    exitDate = models.DateTimeField(blank=True, null=True,auto_now = True)    
    lastUpdatedOn = models.DateTimeField(auto_now = True)
    lastUpdatedBy = models.CharField(max_length=20)

    
