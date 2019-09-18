from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def blogs_list(request):
    return HttpResponse("<h1> blogs list </h1>")