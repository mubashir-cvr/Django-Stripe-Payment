from django.contrib import admin
from .models import OrderDetail,Product


admin.site.register(Product)
admin.site.register(OrderDetail)
# Register your models here.
