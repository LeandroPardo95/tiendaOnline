from django.contrib import admin

from .models import Category, Product

# Register your models here.
# https://docs.djangoproject.com/en/4.0/ref/contrib/admin/


admin.site.register(Product)
admin.site.register(Category)
