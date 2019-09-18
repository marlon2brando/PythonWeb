from django.contrib import admin

# Register your models here.
from blogs.models import Article

admin.site.register(Article)