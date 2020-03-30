
from django.urls import path, re_path
from . import views

urlpatterns = [
    # Matches any html file 
    re_path(r'^.*\.html', views.pages, name='pages'),

    # The home page
    path('', views.index, name='home'),
    path('inventory/', views.inventory_list, name='inventory_list'),
    path('make-sale/', views.make_sale, name='make_sale'),
    # path('product-list/', views.ProductList.as_view(), name='product_list'),
    path('product-list/', views.product_list, name='product_list'),
    path('product/<int:pk>/insert-to-inventory/', views.insert_to_inventory, name='insert_to_inventory'),
    path('sales/', views.sales_list, name='sales_list'),
]
