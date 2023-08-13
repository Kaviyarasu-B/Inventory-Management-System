from django.contrib import admin
from .models import Product, ProductMovement, Location
from django.contrib.auth.models import Group, User

admin.site.site_header = 'Inventory'
admin.site.site_title = 'Inventory Dashboard'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'location')

class ProductMovementAdmin(admin.ModelAdmin):
    list_display = ('movement_id', 'timestamp', 'from_location', 'to_location', 'product', 'qty')

class LocationAdmin(admin.ModelAdmin):
    list_display = ('name','location_id')

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductMovement, ProductMovementAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.unregister(Group)


