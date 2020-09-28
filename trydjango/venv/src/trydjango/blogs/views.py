from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# 新增文章
# 删除文章
# 修改文章
# 展示文章列表

def blogs_list(request):
    return HttpResponse("<h1> blogs list </h1>")