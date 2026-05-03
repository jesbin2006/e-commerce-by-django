from django.shortcuts import render
from . models import product
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    featured_products =product.objects.order_by('prioriity')[:4]
    latest_products =product.objects.order_by('-id')[:4]
    context={
       'featured_products':featured_products,
       'latest_products':latest_products
    }
    return render(request,'index.html',context)

def products(request):
    page=1
    if request.GET:
        page=request.GET.get('page')
    products_list =product.objects.order_by('-prioriity')
    product_paginator =Paginator(products_list,4)
    products_list = product_paginator.get_page(page)
    com={'products':products_list}
    return render(request,'products.html',com)

def detail_product(request,pk):
    products=product.objects.get(pk=pk)
    context={'product':products}

    return render(request,'product_detail.html',context)