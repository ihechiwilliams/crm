from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Customer)

# class ProductAdmin(admin.ModelAdmin):
#     list_display = [
#         'name',
#         'price',
#         'category',
#     ]

admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Order)
