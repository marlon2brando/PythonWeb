from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request,*args, **kwargs):
    print(args,kwargs)
    print(request.user)
    # return HttpResponse('<h1>Hello World!</h1>')
    return render(request,"home.html",{})

def contact_view(request,*args,**kargs):
    return render(request,'contact.html',{})

def about_view(request,*args,**kargs):
    my_context = {
        "my_text":'This is about us',
        "my_number":123,
        "my_list":[1,2,3,4,5,6,7,8,9,10],
    }

    return render(request,'about.html',my_context)

def social_view(request,*args,**kargs):
    return render(request,'social.html',{})


import json
from trydjango.settings import BASE_DIR

def flutter_api(*arg, **kargs):
    path = BASE_DIR + '/pages/userdata.json'
    print(path)
    with open(path,'r') as jsonfile:
        data = jsonfile.read()
    return HttpResponse(data)
    # return HttpResponse("[{'name':'1','age':27}]")