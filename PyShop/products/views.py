from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
import json
from django.core import serializers


def index(request):

    products = Product.objects.all()
    jsonData = serializers.serialize('json', products)
    return HttpResponse(jsonData)

    jsonlist = []
    for p in products:
        jsondict = {
            "name": p.name,
            "price": p.price,
            "stock": p.stock,
            "image_url": p.image_url
        }
        jsonlist.append(jsondict)

    # data = "[" + str(jsonlist) + "]"

    return HttpResponse(str(jsonlist))

    if request.headers['api_type'] == 'app':
        return HttpResponse(json.dump(products))
    else:
        return render(request, 'index.html', {'products': products})


def product_new(request):
    return HttpResponse('new product')
