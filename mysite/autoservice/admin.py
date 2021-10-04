from django.contrib import admin

# Register your models here.
from .models import Service, CarModel, Car, Order, OrderLine

admin.site.register(Service)
admin.site.register(CarModel)
admin.site.register(Car)
admin.site.register(Order)
admin.site.register(OrderLine)