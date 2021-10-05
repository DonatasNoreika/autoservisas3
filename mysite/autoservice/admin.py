from django.contrib import admin

# Register your models here.
from .models import Service, CarModel, Car, Order, OrderLine

class OrderLineInline(admin.TabularInline):
    model = OrderLine
    extra = 0 # išjungia placeholder'ius

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderLineInline]
    list_display = ('car', 'due_date')

class CarAdmin(admin.ModelAdmin):
    list_display = ('owner', 'car_model', 'licence_plate', 'vin_code')

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

admin.site.register(Service, ServiceAdmin)
admin.site.register(CarModel)
admin.site.register(Car, CarAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLine)