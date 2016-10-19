from django.contrib import admin
from .models import Category,Product,ProductOption,ProductChoice
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductOption)
admin.site.register(ProductChoice)
