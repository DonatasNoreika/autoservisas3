from django.contrib import admin

# Register your models here.
from .models import Service, CarModel, Car, Order, OrderLine

class OrderLineInline(admin.TabularInline):
    model = OrderLine
    extra = 0 # išjungia placeholder'ius

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderLineInline]
    list_display = ('car', 'due_date')

admin.site.register(Service)
admin.site.register(CarModel)
admin.site.register(Car)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLine)