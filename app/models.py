
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    productId = models.IntegerField(primary_key=True, unique=True, name='product_id')
    product_name = models.CharField(max_length=200)
    product_type = models.CharField(max_length=200)
    product_manufacturer = models.CharField(max_length=200)
    product_category = models.CharField(max_length=200)
    product_distributor = models.CharField(max_length=200)
    wholesale_price = models.CharField(max_length=50)
    retail_price = models.CharField(max_length=200)
    vat = models.CharField(max_length=200)
    product_code = models.CharField(max_length=200)
    sync_status = models.SmallIntegerField(default=1)
    delete_status = models.SmallIntegerField(default=1)
    depot_id = models.IntegerField()

    def __str__(self):
        return f'{self.product_name} - {self.product_type}'
