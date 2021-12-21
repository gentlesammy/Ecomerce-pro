from django.contrib import admin

# Register your models here.
from ecomerce.inventory.models import Category
from ecomerce.inventory.models import Product
admin.site.register(Category)
admin.site.register(Product)