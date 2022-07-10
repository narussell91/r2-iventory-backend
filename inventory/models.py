from django.contrib.auth.models import AbstractUser
from django. db import models

from djmoney.models.fields import MoneyField

class User(AbstractUser):
    pass

class Buyer(models.Model):
    buyer_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class Store(models.Model):
    store_id = models.IntegerField(primary_key=True)
    store_name = models.CharField(max_length=156)
    location = models.CharField(max_length=2)

class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    sku = models.CharField(max_length=50)
    buy_price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    listed_price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    created_at = models.DateField()
    buyer_id = models.ForeignKey(Buyer, on_delete=models.PROTECT)
    store_id = models.ForeignKey(Store, on_delete=models.PROTECT)