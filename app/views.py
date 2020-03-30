from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Product

@login_required(login_url="login")
def index(request):
    return render(request, "home.html")

@login_required(login_url="login")
def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product_list.html', context = context)

def insert_to_inventory(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'add_to_inventory.html', context={'product':product})

class ProductList(ListView):
    template_name = 'product_list.html'
    queryset = Product.objects.all()
    # print(queryset)

@login_required(login_url="login")
def inventory_list(request):
    return render(request, 'inventory_list.html')

@login_required(login_url="login")
def sales_list(request):
    return render(request, 'sales_list.html')

@login_required(login_url="login")
def make_sale(request):
    return render(request, 'make_sale.html')

@login_required(login_url="login")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        load_template = request.path.split('/')[-1]
        template = loader.get_template('pages/' + load_template)
        return HttpResponse(template.render(context, request))
    except:
        template = loader.get_template( 'pages/error-404.html' )
        return HttpResponse(template.render(context, request))
