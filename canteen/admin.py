from django.contrib import admin
from .models import Owner, KitchenStaff, Item, Order, OrderItem, Bill

# Register your models here.
admin.site.register(Owner)
admin.site.register(KitchenStaff)
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Bill)
