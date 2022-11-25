from django.contrib import admin
from .models import Account, Item, Order, OrderItem, Bill

# Register your models here.
admin.site.register(Account)
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Bill)
