from django.shortcuts import render
from .models import Product
from .forms import Product_add_form

# Create your views here.

def products_view(request):
    items = Product.objects.get(id=2)
    context = {
        'objects':items
    }
    return render(request, 'products/product_detail.html',context)


def products_view_add(request):
    form = Product_add_form(request.POST or None)
    if form.is_valid():
        form.save()
        form = Product_add_form()

    context = {
        'form':form
    }
    return render(request, 'products/product_detail_add.html',context)
