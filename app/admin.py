
from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id','product_name', 'product_type', 'product_manufacturer',)
    exclude = ('product_id',)        

admin.site.register(Product, ProductAdmin)
